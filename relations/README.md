# Relations offered to a network

A network made of ReLUs approximates `x² + y²` with a great many kinked units. A node
that computes `x² + y²` does it in one, and a ring that no straight line can separate
becomes one threshold on it. Humanity already knows many relations that predict well:
decay with depth, saturation with supply, power laws in size and in language. They
should be available to a network as building blocks, not rediscovered from scratch
as piles of kinks.

## The Shoulders of Giants

A published trained network - weights anyone may download - is what has been learnt
from a civilization's text, images and measurements, stored implicitly. It is the
Civilizational Tower of Knowledge in the form one publishes it today. The relations
in this library are the same tower in its explicit form: laws someone found, tested
and published, from Beer and Lambert to Zipf.

Neither half has to be rebuilt. The work here starts from both - a published network
as the base, published relations offered to it as nodes - and adds a floor: which
relations the network chooses to use, where, and how much it still learns without
them. That result is itself something to publish back onto the tower, for the next
builder to stand on.

**What goes into the network is the relation, and nothing else.** A relation is
offered as a node function beside the network's ordinary units. Training decides
which inputs feed it, whether it is used at all, and where its output goes: the
implicit part of the network puts the explicit relation in its place. Nothing about
where the relation is known to hold is imposed.

**What stays here** is what is recorded about each relation: where it has predicted
well, who found it, and what can make it misbehave numerically. That record is for
people reading the network afterwards - which relations it chose to use, and how much
it still had to learn without them - not for the network.

## The library

[`library.py`](library.py) holds the relations. Each is a **form**: its constants - a
rate, a half-saturation, an exponent - are the node's learnable parameters, so the
file types no value about the world. Each records:

| field | what it holds |
|---|---|
| `form` | the relation in the node's own variables |
| `arity`, `params` | the inputs the node takes, and its learnable constants |
| `fn` | the function, written to stay finite for any real input and parameter |
| `uses` | where it has predicted well: field, what it predicted, reference |
| `caution` | anything about its inputs a reader should know |

Every form also carries an applefication (see §1 of the [main README](../README.md)):
a saturation treats all uptake as one saturating process, a power law treats a
range of sizes as one scaling. The network's choice to use a form is evidence that
the assumption holds in that place, not a licence to assume it elsewhere.

Run `python3 relations/library.py` to check that every relation stays finite on
ordinary, extreme and degenerate inputs.

## Using it

Give the network's first layers these nodes next to ordinary units, with a mild
sparsity penalty so that a relation that fits is preferred over a pile of units that
imitates it. Then read the network: which relations carry weight, on which inputs,
and how much the ordinary units still do. The last is the measure of what known
relations leave unexplained.

Two practical points. Forms that can explode are written with guards (clipped
exponents, positive denominators), so training can try them without breaking.
And ordinary units train more easily than exotic ones, so a relation may need a head
start - initial weight, or a lower penalty - to be tried where it fits.

## Not yet here

- **Laws with measured constants** - seawater density (TEOS-10), oxygen solubility,
  gas transfer across the surface. Their constants are part of the law, so they come
  from the reference implementations (TEOS-10's `gsw`) or from pinned sources, not
  from memory.
- **Operators across records** - cumulative sums, moving averages, lags: relations
  in time, such as degree-days or antecedent rainfall, that need a sequence rather
  than one record.
- **Structural relations in language** - agreement, recursion, word order - are
  rules over structures rather than functions of numbers. They enter a network as
  structure (a network that builds a parse as it goes), not as a node function.
