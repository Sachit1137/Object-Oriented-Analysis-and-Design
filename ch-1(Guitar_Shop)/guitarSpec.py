class GuitarSpec:
    
    def __init__(self, builder, model, guitar_type, b_wood, t_wood, num):
        self.builder = builder
        self.model = model
        self.g_type = guitar_type
        self.back_wood = b_wood
        self.top_wood = t_wood   
        self.num_strings = num 
    
    def match_specs(self,guitar_inv,gtr_to_search):
        if gtr_to_search.builder and gtr_to_search.builder != "" and gtr_to_search.builder != guitar_inv.guitar_spec.builder:
            return 0
        if gtr_to_search.model and gtr_to_search.model != "" and gtr_to_search.model.lower() != guitar_inv.guitar_spec.model:
            return 0
        if gtr_to_search.g_type and gtr_to_search.g_type != "" and gtr_to_search.g_type != guitar_inv.guitar_spec.g_type:
            return 0
        if gtr_to_search.back_wood and gtr_to_search.back_wood != "" and gtr_to_search.back_wood != guitar_inv.guitar_spec.back_wood:
            return 0
        if gtr_to_search.top_wood and gtr_to_search.top_wood != "" and gtr_to_search.top_wood != guitar_inv.guitar_spec.top_wood:
            return 0
        if gtr_to_search.num_strings and gtr_to_search.num_strings != 0 and gtr_to_search.num_strings != guitar_inv.guitar_spec.num_strings:
            return 0
        
        return 1