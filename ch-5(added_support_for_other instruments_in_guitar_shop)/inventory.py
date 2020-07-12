class Inventory:
    def __init__(self):
        self.store = []

    def add_instrument(self, instrument):
        self.store.append(instrument)

    def get_instrument(self, srl_num):
        for instrument in self.store:
            if instrument.srl_num == srl_num:
                return instrument
        return None

    def search(self, specs_to_search):
        instruments_found = []
        for instrument in self.store:
            if specs_to_search.match_spec(instrument.get_spec()):
                instruments_found.append(instrument)
        return instruments_found