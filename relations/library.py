"""Relations offered to a neural network as node functions.

A network built from ReLUs approximates x^2 + y^2 with a great many kinked units; a
node that computes x^2 + y^2 does it in one. This file lists relations known to have
predicted something well, written as functions a node can compute. The network is
not told where they apply. It is given them beside its ordinary units, and training
decides which inputs feed each one, whether it is used, and where its output goes
(relations/README.md).

Only the relation goes into the network. What is recorded about it - where it has
predicted well, who found it, what can make it misbehave numerically - stays here.

Every relation below is a FORM: its constants (a rate, a half-saturation, an
exponent) are learnable parameters of the node, so nothing here is a typed value
about the world. Laws whose constants are fixed by measurement are a second tier, to
be added from reference implementations or pinned sources, never retyped.

Inputs are assumed roughly unit-scale, as the layer before will make them. Every
function stays finite for any real input and any real parameter: a node that can
overflow is abandoned by training instead of tried.

Each fn takes the node's inputs, then its parameters in the order of `params`, and
an array module `xp` (numpy by default; torch works the same way where the names
agree).

    python3 relations/library.py      # checks every relation stays finite
"""
from dataclasses import dataclass, field

import numpy as np

# Numerical guards shared by every form: an exponent is clipped so exp() stays
# finite in float32, and a denominator never reaches zero.
EXP_CLIP = 30.0
EPS = 1e-6


def _exp(z, xp):
    return xp.exp(xp.clip(z, -EXP_CLIP, EXP_CLIP))


def _pos(z, xp):
    """A smooth positive version of z (softplus), for anything a form needs > 0."""
    return xp.maximum(z, 0) + xp.log1p(_exp(-xp.abs(z), xp))


@dataclass
class Relation:
    key: str
    name: str
    form: str                 # the relation in the node's own variables
    arity: int                # inputs the node takes
    params: tuple             # learnable constants, in fn's order
    fn: object
    uses: list = field(default_factory=list)   # (field, what it predicts, reference)
    caution: str = ""


R = []


def rel(**kw):
    R.append(Relation(**kw))


rel(key="product", name="Product", form="x·y", arity=2, params=(),
    fn=lambda x, y, xp=np: x * y,
    uses=[("chemistry", "reaction rate proportional to the product of concentrations",
           "Guldberg & Waage 1864 (mass action)"),
          ("transport", "flux as concentration times velocity", "textbook")])

rel(key="ratio", name="Ratio", form="x / y⁺", arity=2, params=(),
    fn=lambda x, y, xp=np: x / (_pos(y, xp) + EPS),
    uses=[("oceanography", "nutrient ratios as limitation indices", "Redfield 1934"),
          ("general", "rates per unit area, time or mass", "textbook")],
    caution="the denominator is made positive (softplus); the network supplies its sign-free size")

rel(key="square", name="Square", form="x²", arity=1, params=(),
    fn=lambda x, xp=np: x * x,
    uses=[("mechanics", "kinetic energy against speed", "textbook"),
          ("waves", "wave energy against wave height", "textbook")])

rel(key="radial", name="Squared distance", form="x² + y²", arity=2, params=(),
    fn=lambda x, y, xp=np: x * x + y * y,
    uses=[("geometry", "distance from a centre: a ring is one threshold on it", "textbook")])

rel(key="power", name="Power law", form="a · (x⁺)ᵇ", arity=1, params=("a", "b"),
    fn=lambda x, a, b, xp=np: a * _exp(b * xp.log(_pos(x, xp) + EPS), xp),
    uses=[("biology", "metabolic rate against body mass", "Kleiber 1932"),
          ("language", "word frequency against frequency rank", "Zipf 1935"),
          ("language", "vocabulary size against text length", "Heaps 1978")])

rel(key="decay", name="Exponential decay", form="e^(−k·x)", arity=1, params=("k",),
    fn=lambda x, k, xp=np: _exp(-k * x, xp),
    uses=[("optics", "light against depth in water", "Lambert 1760; Beer 1852"),
          ("physics", "radioactive decay against time", "Rutherford & Soddy 1902"),
          ("water quality", "oxygen demand exerted over time", "Streeter & Phelps 1925")])

rel(key="growth", name="Exponential temperature factor", form="e^(k·x)", arity=1, params=("k",),
    fn=lambda x, k, xp=np: _exp(k * x, xp),
    uses=[("phytoplankton", "maximum growth rate against temperature", "Eppley 1972"),
          ("physiology", "rate multiplied by a fixed factor per ten degrees (Q10)", "van 't Hoff 1884")])

rel(key="arrhenius", name="Arrhenius", form="e^(−a / x⁺)", arity=1, params=("a",),
    fn=lambda x, a, xp=np: _exp(-a / (_pos(x, xp) + EPS), xp),
    uses=[("chemistry", "reaction rate against absolute temperature", "Arrhenius 1889")],
    caution="meaningful when the input stands for an absolute temperature")

rel(key="saturation", name="Hyperbolic saturation", form="x⁺ / (K⁺ + x⁺)", arity=1, params=("K",),
    fn=lambda x, K, xp=np: _pos(x, xp) / (_pos(K, xp) + _pos(x, xp) + EPS),
    uses=[("biochemistry", "enzyme rate against substrate", "Michaelis & Menten 1913"),
          ("microbiology", "growth against a limiting nutrient", "Monod 1949"),
          ("surface chemistry", "adsorption against pressure", "Langmuir 1918")])

rel(key="tanh", name="Tanh saturation", form="tanh(a·x)", arity=1, params=("a",),
    fn=lambda x, a, xp=np: xp.tanh(a * x),
    uses=[("phytoplankton", "photosynthesis against light", "Jassby & Platt 1976")])

rel(key="logistic", name="Logistic", form="1 / (1 + e^(−k(x − x₀)))", arity=1, params=("k", "x0"),
    fn=lambda x, k, x0, xp=np: 1.0 / (1.0 + _exp(-k * (x - x0), xp)),
    uses=[("ecology", "population growth towards a carrying capacity", "Verhulst 1838"),
          ("toxicology", "share responding against dose", "textbook")])

rel(key="periodic", name="Periodic", form="sin(ω·x + φ)", arity=1, params=("w", "phi"),
    fn=lambda x, w, phi, xp=np: xp.sin(w * x + phi),
    uses=[("climate", "daily and seasonal cycles of light and temperature", "textbook"),
          ("oceanography", "tidal constituents", "textbook")])

rel(key="log", name="Logarithm", form="log(x⁺)", arity=1, params=(),
    fn=lambda x, xp=np: xp.log(_pos(x, xp) + EPS),
    uses=[("perception", "sensation against stimulus strength", "Fechner 1860"),
          ("boundary layers", "wind speed against height above ground", "Prandtl and von Kármán (log law)"),
          ("information", "information in an outcome against its probability", "Shannon 1948"),
          ("chemistry", "acidity as pH", "Sørensen 1909")])

rel(key="gaussian", name="Gaussian bump", form="e^(−(x − μ)² / 2s⁺²)", arity=1, params=("mu", "s"),
    fn=lambda x, mu, s, xp=np: _exp(-(x - mu) ** 2 / (2 * (_pos(s, xp) + EPS) ** 2), xp),
    uses=[("ecology", "species response along an environmental gradient", "ter Braak & Looman 1986"),
          ("physics", "spread from a point by diffusion", "textbook")])

rel(key="hinge", name="Smooth threshold", form="(x − x₀)⁺", arity=1, params=("x0",),
    fn=lambda x, x0, xp=np: _pos(x - x0, xp),
    uses=[("agronomy", "degree-days above a base temperature", "textbook"),
          ("general", "an effect that begins at a threshold", "textbook")])

rel(key="inverse_square", name="Inverse square", form="1 / (x² + c⁺)", arity=1, params=("c",),
    fn=lambda x, c, xp=np: 1.0 / (x * x + _pos(c, xp) + EPS),
    uses=[("physics", "gravity and light from a point source against distance", "Newton 1687"),
          ("dispersion", "dilution away from a point discharge", "textbook")])

rel(key="softmin", name="Soft minimum", form="−(1/k⁺) log(e^(−k⁺x) + e^(−k⁺y))", arity=2, params=("k",),
    fn=lambda x, y, k, xp=np: (xp.minimum(x, y)
                                - xp.log1p(_exp(-(_pos(k, xp) + EPS) * xp.abs(x - y), xp))
                                / (_pos(k, xp) + EPS)),
    uses=[("agronomy", "growth set by the scarcest resource", "Liebig 1840, after Sprengel 1828")],
    caution="approaches min(x, y) as k grows; smooth so a gradient reaches both inputs")

RELATIONS = {r.key: r for r in R}


def _check():
    """Every relation stays finite for ordinary, extreme and degenerate inputs and
    for any parameter values."""
    rng = np.random.default_rng(0)
    cases = [rng.standard_normal(1000), 1e3 * rng.standard_normal(1000),
             np.zeros(1000), np.full(1000, -1e6), np.full(1000, 1e6)]
    bad = []
    for r in R:
        for x in cases:
            ins = [x] + [rng.permutation(x) for _ in range(r.arity - 1)]
            for _ in range(20):
                ps = [rng.standard_normal() * s for s in rng.choice([1.0, 10.0, 100.0], len(r.params))]
                with np.errstate(all="ignore"):
                    out = np.asarray(r.fn(*ins, *ps, xp=np), dtype=float)
                if not np.all(np.isfinite(out)):
                    bad.append(r.key)
                    break
    return sorted(set(bad))


if __name__ == "__main__":
    bad = _check()
    print(f"{len(R)} relations; not finite everywhere: {bad or 'none'}")
    raise SystemExit(1 if bad else 0)
