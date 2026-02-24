# Cayley Graphs

This is a tool for exploring infinite groups. For infinite groups you can't build the whole Cayley graph, this tool lets you compute balls of radius n. From there, you can then analyze properties like growth rates and visualize these balls. If selected the tool will output an image of the ball. Other specific functionalities can be seen from the interactive menu.

## Setup

Clone it and cd in:
```bash
git clone https://github.com/yourusername/cayleylab.git
cd cayleylab
```

**Requirements to run this code:**
- Python 3.8+
- matplotlib (for plotting graphs)
- numpy (for numerical operations)

Install with:
```bash
pip install matplotlib numpy
```

## Using it

### Interactive mode

```bash
python -m cayleylab
```

Pops up a terminal where you can:
- pick a group and generators
- compute Cayley balls
- export graphs (dot, png, json)
- look at growth
- check dead ends

### Check if wreath products are k-generated

```bash
python prob_genSet.py "Z/2 x Z/2 wr Z/3" --k 2
```


### Wreath products in code

```python
from cayleylab.groups.wreath import WreathProduct
from cayleylab.core.growth import analyze_growth

group = WreathProduct()
group.parse_options({"spec": "Z/2 wr Z"})
gens = group.default_generators()

result = analyze_growth(group, gens, radius=5)
print(result['omega'])
```

## What groups are in here

### Free groups F_n

Just the free group on n generators. Elements are words in the generators and their inverses, no relations. 

```python
group = FreeGroup(rank=2)  # F_2, two generators a and b
gens = group.default_generators()
```

### Cyclic groups

**ℤ** - integers, one generator that moves you around infinitely in both directions. Polynomial growth.

**ℤ/n** - cyclic group of order n. Only n elements total.

```python
group = Z()           # The integers
group = Zmod(5)       # ℤ/5, cyclic of order 5
group = Zmod(2)**3    # (ℤ/2)^3, direct product
```

### Dihedral groups

**D_n** - symmetries of an n-gon (rotations + reflection). Order 2n.

**D_∞** - infinite dihedral group, like symmetries of an infinite line. Polynomial growth like ℤ.

```python
group = Dihedral(n=4)  # D_4, dihedral group of order 8
```

### Wreath products 

**Example: Lamplighter group** is ℤ/2 ≀ ℤ. At each position on the integer line, there's a lightbulb (on/off). You can walk left/right and toggle bulbs.

```python
# C_2 wreath Z (lamplighter)
group = WreathProduct()
group.parse_options({"spec": "Z/2 wr Z"})

# C_3 wreath Z/5
group = WreathProduct()
group.parse_options({"spec": "Z/3 wr Z/5"})

# More complex: (Z/2 x Z/2) wreath (Z/3)
group = WreathProduct()
group.parse_options({"spec": "Z/2 x Z/2 wr Z/3"})
```

For wreath products, the spec is `"base wr walking"` where:
- `base` can be things like `Z/2`, `Z/3`, `Z/2 x Z/3`, `free_2` (free group on 2 gens)
- `walking` is usually `Z`, `Z/n`, `D_k`, or `Z/a x Z/b`

State is represented as `(head, tape)` where `head` is your position in the walking group and `tape` is a dict of lamp positions to lamp states. Only non-identity lamps are stored (for efficiency).

### Z with custom steps

Just ℤ but the generators move you by different amounts:

```python
group = Z_RestrictedWalk(steps={'a': 1, 'b': 2})
# Generator 'a' moves by 1, generator 'b' moves by 2
```

## How generators work

Each generator in a wreath product is one of:

- **MoveGen**: moves the walker in the base group (e.g., go left/right)
- **ToggleGen**: toggle a lamp at a specific position
- **CompositeGen**: combination of moves (move + toggle lamps at nearby positions)

Default generators are usually:
- For C ≀ ℤ: move left, move right, toggle at position 0, toggle at position 1
- For C ≀ D where D has multiple generators: move generators from D, plus toggle generators

You can specify custom generators when you create the group.

## Growth functions

The growth function σ_r = number of elements at distance exactly r (in the Cayley graph).

Growth exponent ω = lim σ_r^(1/r). This tells you:
- ω > 1: exponential growth (like free groups)
- ω = 1: subexponential growth, usually polynomial (like ℤ, wreath products with ℤ base)

The code can compute ω exactly for some groups (free groups, ℤ, wreath products with ℤ walking group) and estimate it by BFS up to some radius.

## How it's organized

```
cayleylab/
├── groups/       - group definitions
│   ├── wreath.py         - wreath products
│   ├── free.py           - free groups
│   ├── Z_restricted_walk.py - Z with custom steps
│   └── (other groups)
├── core/         - algorithms
│   ├── bfs.py    - compute Cayley balls (BFS)
│   ├── growth.py - analyze growth, compute exponents
│   └── export.py - save to dot/png/json
└── ui/           - terminal interface
    └── main.py
```

## What you can do

- Build Cayley balls with BFS
- Get growth exponents (exact or estimate)
- Check if generators actually generate the whole group
- Export to dot/png for pictures
- Find dead ends 
