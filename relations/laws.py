"""Laws with measured constants, offered as first-layer nodes wired to named inputs.

The forms in library.py take whatever inputs the network feeds them and learn their
constants. A law here is different in both respects: its constants were fixed by
measurement and are part of the law, and its inputs are physical quantities in stated
units, so the node is wired to the record columns that carry them rather than to
learned combinations.

Nothing here retypes a constant. Every law calls the reference implementation of the
TEOS-10 standard, the Gibbs SeaWater (GSW) Oceanographic Toolbox (the `gsw` package),
and each entry's caution repeats what that implementation says about its own limits.

`columns` names, for documentation only, where the inputs are found in the ODA CTD
extract used by copenhagen-waterways; a reader of another dataset maps their own.

    ~/.venvs/relations/bin/python relations/laws.py   # physical invariants on a grid

Requires numpy and gsw (relations/requirements.txt); library.py needs numpy only.
"""
from dataclasses import dataclass, field

import numpy as np
import gsw


@dataclass
class Law:
    key: str
    name: str
    inputs: tuple             # (quantity, unit), in fn's order
    output: tuple             # (quantity, unit)
    fn: object
    source: str
    caution: str = ""
    columns: dict = field(default_factory=dict)
    per_record: bool = True   # False: needs a whole profile, not one record


L = []


def law(**kw):
    L.append(Law(**kw))


law(key="pressure", name="Sea pressure from depth",
    inputs=(("depth", "m, positive down"), ("lat", "degrees N")), output=("p", "dbar"),
    fn=lambda depth, lat: gsw.p_from_z(-np.asarray(depth, dtype=float), lat),
    source="TEOS-10 via gsw.p_from_z (Roquet et al. 2015 expression)",
    caution="gsw takes height, negative in the ocean, so depth is negated here",
    columns={"depth": "Dybde (m)", "lat": "the station's position (stations register)"})

law(key="absolute_salinity", name="Absolute Salinity from Practical Salinity",
    inputs=(("SP", "PSS-78, unitless"), ("p", "dbar"), ("lon", "degrees E"), ("lat", "degrees N")),
    output=("SA", "g/kg"), fn=gsw.SA_from_SP,
    source="TEOS-10 via gsw.SA_from_SP",
    caution="gsw sets negative Practical Salinity to zero. ODA reports salinity in "
            "'promille'; reading it as PSS-78 Practical Salinity is an assumption to state",
    columns={"SP": "Parameter 'Salinitet', Enhed 'promille'", "p": "law 'pressure'",
             "lon": "the station's position", "lat": "the station's position"})

law(key="conservative_temperature", name="Conservative Temperature from in-situ temperature",
    inputs=(("SA", "g/kg"), ("t", "degrees C, ITS-90"), ("p", "dbar")), output=("CT", "degrees C"),
    fn=gsw.CT_from_t, source="TEOS-10 via gsw.CT_from_t",
    columns={"SA": "law 'absolute_salinity'", "t": "Parameter 'Temperatur', Enhed 'grader C'",
             "p": "law 'pressure'"})

law(key="density", name="In-situ density",
    inputs=(("SA", "g/kg"), ("CT", "degrees C"), ("p", "dbar")), output=("rho", "kg/m^3"),
    fn=gsw.rho, source="TEOS-10 via gsw.rho (Roquet et al. 2015 expression)",
    caution="fitted in a restricted range of parameter space and most accurate inside the "
            "'oceanographic funnel' (McDougall et al. 2003); check brackish water with in_funnel()")

law(key="sigma0", name="Potential density anomaly at the surface",
    inputs=(("SA", "g/kg"), ("CT", "degrees C")), output=("sigma0", "kg/m^3 minus 1000"),
    fn=gsw.sigma0, source="TEOS-10 via gsw.sigma0",
    caution="the same restricted range as density; the difference between two depths is the "
            "stratification a water column must overcome to mix")

law(key="oxygen_solubility", name="Oxygen solubility at equilibrium with air",
    inputs=(("SP", "PSS-78, unitless"), ("pt", "degrees C, potential temperature")),
    output=("O2sol", "umol/kg"), fn=gsw.O2sol_SP_pt,
    source="gsw.O2sol_SP_pt: Benson and Krause (1984) data as fitted by Garcia and Gordon "
           "(1992, 1993)",
    caution="the implementation notes that the algorithm has not been approved by IOC and is "
            "included as oceanographic best practice. Its unit is umol/kg; ODA oxygen is in "
            "mg/l, and converting needs density and the molar mass of oxygen, from a source",
    columns={"SP": "Parameter 'Salinitet'", "pt": "gsw.pt0_from_t(SA, t, p)"})

law(key="buoyancy_frequency", name="Buoyancy frequency squared", per_record=False,
    inputs=(("SA", "g/kg"), ("CT", "degrees C"), ("p", "dbar"), ("lat", "degrees N")),
    output=("N2", "1/s^2"), fn=gsw.Nsquared, source="TEOS-10 via gsw.Nsquared",
    caution="computed from vertical differences, so it takes a whole cast ordered by pressure "
            "and returns one value between each pair of levels")

LAWS = {x.key: x for x in L}


def in_funnel(SA, CT, p):
    """Whether each point lies where TEOS-10's density expression is most accurate."""
    return np.asarray(gsw.infunnel(SA, CT, p), dtype=bool)


def record_state(SP, t, depth, lon, lat):
    """The per-record laws chained from what a CTD record carries: the node values a
    first layer would receive for one measurement."""
    p = LAWS["pressure"].fn(depth, lat)
    SA = gsw.SA_from_SP(SP, p, lon, lat)
    CT = gsw.CT_from_t(SA, t, p)
    pt = gsw.pt0_from_t(SA, t, p)
    return {"p": p, "SA": SA, "CT": CT, "rho": gsw.rho(SA, CT, p),
            "sigma0": gsw.sigma0(SA, CT), "O2sol": gsw.O2sol_SP_pt(SP, pt),
            "in_funnel": in_funnel(SA, CT, p)}


def _check():
    """Physical invariants on a grid of brackish-to-marine states, not reference
    values: density rises with salinity and with depth, and falls with temperature
    in this range; oxygen solubility falls with temperature and with salinity."""
    lon, lat = 12.0, 55.5
    S = np.linspace(5, 35, 13)
    T = np.linspace(2, 20, 10)
    problems = []
    for depth in (1.0, 20.0):
        s = record_state(S[:, None], T[None, :], depth, lon, lat)
        if not np.all(np.diff(s["rho"], axis=0) > 0): problems.append(f"density not rising with salinity at {depth} m")
        if not np.all(np.diff(s["O2sol"], axis=1) < 0): problems.append(f"solubility not falling with temperature at {depth} m")
        if not np.all(np.diff(s["O2sol"], axis=0) < 0): problems.append(f"solubility not falling with salinity at {depth} m")
        if not all(np.all(np.isfinite(v)) for k, v in s.items() if k != "in_funnel"): problems.append("not finite")
    a, b = record_state(20.0, 10.0, 1.0, lon, lat), record_state(20.0, 10.0, 20.0, lon, lat)
    if not b["rho"] > a["rho"]: problems.append("density not rising with depth")
    return problems


if __name__ == "__main__":
    bad = _check()
    print(f"{len(L)} laws; invariants broken: {bad or 'none'}")
    raise SystemExit(1 if bad else 0)
