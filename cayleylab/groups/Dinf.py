
class R:
    name = "r"
    
    def apply(self, s):
        k, e = s
        return (k + 1, e)


class Rinv:
    name = "R"
    
    def apply(self, s):
        k, e = s
        return (k - 1, e)


class S:
    name = "s"
    
    def apply(self, s):
        k, e = s
        return (-k, 1 - e)


class Dinf:
    name = "D∞"
    
    def identity(self):
        return (0, 0)
    
    def default_generators(self):
        return [R(), Rinv(), S()]
    
    def parse_options(self, opts):
        return Dinf()
    
    def pretty(self, s):
        k, e = s
        return f"k={k}|eps={e}"
