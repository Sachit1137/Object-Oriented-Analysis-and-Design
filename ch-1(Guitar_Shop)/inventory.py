import guitar
import guitarSpec
class Inventory(guitarSpec.GuitarSpec):
    def __init__(self):
        self.guitar_list = []

    def add_guitar(self, srl_num, price, guitar_spec):
        self.guitar_list.append(guitar.Guitar(srl_num, price, guitar_spec))

    def display_guitar(self, gtrs_list):
        for i in range(len(gtrs_list)):
            print("Guitar :", i+1)
            print("serial number:", gtrs_list[i].serial_num)
            print("builder version = ", gtrs_list[i].guitar_spec.builder)
            print("type = ", gtrs_list[i].guitar_spec.g_type)
            print("backwood = ", gtrs_list[i].guitar_spec.back_wood)
            print("topWood = ", gtrs_list[i].guitar_spec.top_wood)
            print("price = ", gtrs_list[i].price)
            print("num of strings = ", gtrs_list[i].guitar_spec.num_strings)

    def get_guitar(self, srl_num):
        for gtr in self.guitar_list:
            if gtr.srl_num == srl_num:
                return gtr
        return None

    def search(self, gtr_to_search):
        gtrs_found = []
        for i in range(len(self.guitar_list)):
            if self.match_specs(self.guitar_list[i], gtr_to_search):
                gtrs_found.append(self.guitar_list[i])
        return gtrs_found
