

def build_inverses_map(rank):
    inverses = {}
    for i in range(rank):
        lower = chr(ord('a') + i)
        upper = chr(ord('A') + i)
        inverses[lower] = upper
        inverses[upper] = lower
    return inverses


def reduce_word(word, inverses):
    stack = []
    
    for letter in word:
        if stack and stack[-1] == inverses.get(letter, None):
            stack.pop()
        else:
            stack.append(letter)
    
    return tuple(stack)


class FreeGen:
    def __init__(self, name, letter, inverses):
        self.name = name
        self.letter = letter
        self.inverses = inverses
    
    def apply(self, s):
        return reduce_word(s + (self.letter,), self.inverses)


class FreeGroup:
    
    def __init__(self, rank=2):
        self.rank = rank
        self.inverses = build_inverses_map(rank)
        self.name = f"F_{rank} (Free Group)"
    
    def identity(self):
        return ()
    
    def default_generators(self):
        gens = []
        for i in range(self.rank):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            gens.append(FreeGen(lower, lower, self.inverses))
            gens.append(FreeGen(upper, upper, self.inverses))
        return gens
    
    def parse_options(self, opts):
        rank = opts.get("rank", 2)
        return FreeGroup(rank=rank)
    
    def pretty(self, s):
        if not s:
            return "e"
        return "".join(s)
