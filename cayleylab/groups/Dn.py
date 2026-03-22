class Rn:
    def __init__(self, n):
        self.name = "r"
        self.n = n

    def apply(self, s):
        k, e = s
        return ((k + 1) % self.n, e)


class RnInv:
    def __init__(self, n):
        self.name = "R"
        self.n = n

    def apply(self, s):
        k, e = s
        return ((k - 1) % self.n, e)


class Sn:
    name = "s"

    def __init__(self, n):
        self.n = n

    def apply(self, s):
        k, e = s
        return ((-k) % self.n, 1 - e)


class Dn:
    name = "Dn"

    def __init__(self, n=5):
        self.n = n

    def identity(self):
        return (0, 0)

    def default_generators(self):
        return [Rn(self.n), RnInv(self.n), Sn(self.n)]

    def parse_options(self, opts):
        n = int(opts.get("n", 5))
        if n < 2:
            n = 2
        return Dn(n=n)

    def pretty(self, s):
        k, e = s
        if e == 0:
            return f"r^{k}" if k != 0 else "e"
        return f"r^{k}s" if k != 0 else "s"
