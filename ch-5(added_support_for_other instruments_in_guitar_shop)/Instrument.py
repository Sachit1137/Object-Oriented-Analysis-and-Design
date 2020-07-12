class Instrument():
    
    def __init__(self, srl_num, price, spec):
        self.srl_num = srl_num
        self.price = price
        self.instrument_spec = spec
    
    def get_spec(self):
        return self.instrument_spec