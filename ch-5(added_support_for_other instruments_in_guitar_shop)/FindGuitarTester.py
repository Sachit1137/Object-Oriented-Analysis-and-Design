import inventory
import InstrumentSpec
import Instrument
import enum

class Type(enum.Enum):
    ACOUSTIC = "ACOUSTIC"
    ELECTRIC = "ELECTRIC"

class Builder(enum.Enum):
    FENDER = "FENDER"
    MARTIN = "MARTIN"
    GIBSON = "GIBSON"

class InstrumentCategory(enum.Enum):
    GUITAR = "GUITAR"
    MANDOLIN = "MANDOLIN"
    BANJO = "BANJO"    
    DOBROS = "DOBROS"
    FIDDLES = "FIDDLES"
    
class Wood(enum.Enum):
    CEDAR = "CEDAR"
    MAPLE = "MAPLE"
    COCOBOLO = "COCOBOLO"
    ALDER = "ALDER"

class Style(enum.Enum):
    STYLE1 = "BOLLYWOOD"
    STYLE2 = "HOLLYWOOD"

class FindGuitarTester():
    def main(self):
        self.num_of_strings = 12
        self.inv = inventory.Inventory()

        customer_specs = {"model":"abc"}
        instr_spec = InstrumentSpec.InstrumentSpec(customer_specs)
        self.initialize_inventory()

        instruments_found = self.inv.search(instr_spec)
        
        print("Instrument Not found") if not instruments_found else [print(i.srl_num) for i in instruments_found]

    def initialize_inventory(self):
        specs1 = {"instrument":InstrumentCategory.GUITAR,"strings":12,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument1 = Instrument.Instrument("1", 1499.95, specs1)

        specs2 = {"instrument":InstrumentCategory.GUITAR,"strings":10,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"abc","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument2 = Instrument.Instrument("2", 1543.95, specs2)
        
        specs3 = {"instrument":InstrumentCategory.GUITAR,"strings":12,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument3 = Instrument.Instrument("3", 1249.95, specs3)
        
        specs4 = {"instrument":InstrumentCategory.MANDOLIN,"style":Style.STYLE1,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"abc","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument4 = Instrument.Instrument("4", 1543.95, specs4)
        
        specs5 = {"instrument":InstrumentCategory.MANDOLIN,"style":Style.STYLE2,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument5 = Instrument.Instrument("5", 1249.95, specs5)
        
        specs6 = {"instrument":InstrumentCategory.BANJO,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"abc","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument6 = Instrument.Instrument("6", 1543.95, specs6)
        
        specs7 = {"instrument":InstrumentCategory.BANJO,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
        instrument7 = Instrument.Instrument("7", 1249.95, specs7)
        
        self.inv.add_instrument(instrument1)
        self.inv.add_instrument(instrument2)
        self.inv.add_instrument(instrument3)
        self.inv.add_instrument(instrument4)
        self.inv.add_instrument(instrument5)
        self.inv.add_instrument(instrument6)
        self.inv.add_instrument(instrument7)

obj = FindGuitarTester()
obj.main()