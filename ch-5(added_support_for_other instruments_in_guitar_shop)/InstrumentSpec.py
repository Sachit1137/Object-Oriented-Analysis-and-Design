import collections

class InstrumentSpec():
    def __init__(self, spec):
        self.spec = spec

    def get_all_specs(self):
        return self.specs

    def get_spec(self, key_spec):
        return self.specs[key_spec]

    def match_spec(self, instrument_spec):
        for key in self.spec.keys():
            if key in instrument_spec and self.spec[key] != instrument_spec[key]:
                return 0
        return 1