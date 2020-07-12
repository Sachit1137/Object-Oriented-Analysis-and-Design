import inventory
import guitar
import guitarSpec
import enum


class Type(enum.Enum):
    ACOUSTIC = "ACOUSTIC"
    ELECTRIC = "ELECTRIC"


class Builder(enum.Enum):
    FENDER = "FENDER"
    MARTIN = "MARTIN"
    GIBSON = "GIBSON"


class Wood(enum.Enum):
    CEDAR = "CEDAR"
    MAPLE = "MAPLE"
    COCOBOLO = "COCOBOLO"
    ALDER = "ALDER"


class FindGuitarTester():
    def main(self):
        num_of_strings = 12
        self.inv = inventory.Inventory()

        customer_guitar = guitarSpec.GuitarSpec(
            Builder.FENDER, "Sratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, num_of_strings)
        self.initialize_inventory()

        gtrs_found = self.inv.search(customer_guitar)
        print("Not found") if not gtrs_found else self.inv.display_guitar(gtrs_found)

    def initialize_inventory(self):
        guitar_spec1 = guitarSpec.GuitarSpec(Builder.FENDER,
                                             "abc", Type.ELECTRIC, Wood.ALDER, Wood.ALDER,12)
        guitar_spec2 = guitarSpec.GuitarSpec(Builder.FENDER,
                                             "sratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER,12)
        self.inv.add_guitar("V95693", 1499.95, guitar_spec1)
        self.inv.add_guitar("V95123", 1543.95, guitar_spec2)
        self.inv.add_guitar("V54312", 1249.95, guitar_spec2)
        


obj = FindGuitarTester()
obj.main()
