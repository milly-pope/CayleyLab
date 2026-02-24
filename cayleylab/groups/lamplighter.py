
from .wreath import WreathProduct
#As lamplighter is just a special case of wreath product, we essentially just call the wreath product code with some special options. 

class Lamplighter:
    name = "Lamplighter"
    
    def __init__(self, spec="Z/2 wr Z", offsets=None):
        self.wreath = WreathProduct()
        self.wreath.is_lamplighter = True  
        self.spec = spec #i.e what group to use for the lamp and the base. E.g. "Z/2 wr Z" or "Z/3 wr Z^2"
        self.offsets = offsets #brought in so could implement restricted walk lamplighter variants
        self._configured = None
    
    def identity(self):
        if not self._configured:
            self._configure()
        return self._configured.identity()
    
    def _configure(self):
        # Configure the underlying wreath product
        opts = {'spec': self.spec}
        if self.offsets is not None:
            opts['offsets'] = self.offsets
        self._configured = self.wreath.parse_options(opts)
    
    def default_generators(self):
        if not self._configured:
            self._configure()
        return self._configured.default_generators()
    
    def parse_options(self, opts):
        # Parse user input
        spec = opts.get("spec", "Z/2 wr Z")
        offsets = opts.get("offsets", None)
        
        # Create and configure new instance
        lamp = Lamplighter(spec=spec, offsets=offsets)
        lamp._configure()
        return lamp._configured  
    
    def pretty(self, s):
        if not self._configured:
            self._configure()
        return self._configured.pretty(s)


