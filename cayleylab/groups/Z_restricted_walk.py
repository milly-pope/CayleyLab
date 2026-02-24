class StepGenerator:
    def __init__(self, name, step):
        self.name = name
        self.step = step
    
    def apply(self, n):
        return n + self.step


class Z_RestrictedWalk:
    name = "Z"
    
    def __init__(self, steps=None):
        self.steps = steps or {'a': 1}
    
    def identity(self):
        return 0
    
    def default_generators(self):
        gens = []
        for name, step in sorted(self.steps.items()):
            gens.append(StepGenerator(name, step))
            inverse_name = name.upper() if name.islower() else name.lower()
            gens.append(StepGenerator(inverse_name, -step))
        return gens
    
    def parse_options(self, opts):
        steps = opts.get('steps', None)
        if steps is None:
            steps = opts.get('offsets', self.steps)
        return Z_RestrictedWalk(steps)
    
    def pretty(self, n):
        return f"{n}"
