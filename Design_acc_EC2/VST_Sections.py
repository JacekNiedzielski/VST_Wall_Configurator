import math
from Design_acc_EC2.RC import Concrete, Reinforcing_Steel


class CrossSection:

    def __init__(self, height, reinforcement = Reinforcing_Steel, concrete = Concrete, width=1, exp = "XC1", Hat_Profile_50 = False, Hat_Profile_30 = False):
        self.width = width
        self.height = height
        self.Hat_Profile_30 = Hat_Profile_30
        self.Hat_Profile_50 = Hat_Profile_50
        self.reinforcement = reinforcement
        self.concrete = concrete
        self.exposition_class = exp
        self.reinforcement = reinforcement
        self.concrete = concrete
        self.reinforcement.hor_rebar_diam = None
        self.reinforcement.vert_rebar_diam = None
        
        
   #def define_reinforcing_steel(self, steel_class = 500, E = 200):
    #    self.reinforcement = self.reinforcement(steel_class)
       
     
        
    def define_rebars_main(self, rebar_diameter = 0.01, rebar_number = 2, axial_distance = 0.4, type_of_reinforcing = "classic", number_of_rebars_per_distance = 1):
        
        """
        accepted arguments:
            rebar_diameter, 
            rebar_number, 
            axial_distance,
            type_of_reinforcing == "classic" or "Per meter",
            number_of_rebars_per_distance
        """
        
        
        
        self.type_of_reinforcing = type_of_reinforcing
        
        
        if self.type_of_reinforcing == "classic":
            

            try:
                self.reinforcement.rebar_diameter = rebar_diameter
                self.reinforcement.axial_distance = None
                self.reinforcement.rebar_number = rebar_number
                self.reinforcement.number_of_rebars_per_distance = None
                
                self.reinforcement.As = self.reinforcement.rebar_diameter**2 * math.pi / \
                    4 * self.reinforcement.rebar_number
                
                
            except(AttributeError):
                print("Method unavailable - prior definition of the reinforcing steel class is required!")    
            
        elif self.type_of_reinforcing == "Per meter":    
            
            try:
                self.reinforcement.rebar_diameter = rebar_diameter
                self.reinforcement.axial_distance = axial_distance
                self.reinforcement.rebar_number = None
                self.reinforcement.number_of_rebars_per_distance = number_of_rebars_per_distance
                
                self.reinforcement.As = self.reinforcement.rebar_diameter**2 * math.pi /  \
                4 * self.reinforcement.number_of_rebars_per_distance / \
                self.reinforcement.axial_distance
                
                
            except(AttributeError):
                print("Method unavailable - prior definition of the reinforcing steel class is required!")
                
                
            
    def define_rebars_quer(self, rebar_diameter = 0.01, rebar_number = 2, axial_distance = 0.4, type_of_reinforcing = "classic", number_of_rebars_per_distance = 1):
        
        """
        accepted arguments:
            rebar_diameter, 
            rebar_number, 
            axial_distance,
            type_of_reinforcing == "classic" or "Per meter",
            number_of_rebars_per_distance
        """
        
        
        
        self.type_of_reinforcing = type_of_reinforcing
        
        
        if self.type_of_reinforcing == "classic":
            

            try:
                self.reinforcement.rebar_diameter_quer = rebar_diameter
                self.reinforcement.axial_distance_quer = None
                self.reinforcement.rebar_number_quer = rebar_number
                self.reinforcement.number_of_rebars_per_distance_quer = None
                
                self.reinforcement.As_quer = self.reinforcement.rebar_diameter_quer**2 * math.pi / \
                    4 * self.reinforcement.rebar_number_quer
                
                
            except(AttributeError):
                print("Method unavailable - prior definition of the reinforcing steel class is required!")    
            
        elif self.type_of_reinforcing == "Per meter":    
            
            try:
                self.reinforcement.rebar_diameter_quer = rebar_diameter
                self.reinforcement.axial_distance_quer = axial_distance
                self.reinforcement.rebar_number_quer = None
                self.reinforcement.number_of_rebars_per_distance_quer = number_of_rebars_per_distance
                
                self.reinforcement.As_quer = self.reinforcement.rebar_diameter_quer**2 * math.pi /  \
                4 * self.reinforcement.number_of_rebars_per_distance_quer / \
                self.reinforcement.axial_distance_quer
                
                
            except(AttributeError):
                print("Method unavailable - prior definition of the reinforcing steel class is required!")
    


    def get_section_properties(self, assummed_rebar_diameter = None, assummed_rebar_diameter_quer = None, deviatoric = 0.01):
        
        self.deviatoric = deviatoric
        self.assummed_rebar_diameter = assummed_rebar_diameter
        self.assummed_rebar_diameter_quer = assummed_rebar_diameter_quer
        self.moment_of_inertia = self.width * self.height**3 / 12
        self.first_moment_of_area = self.width * self.height**2 / 2
        
        """Table 4.4 DE"""
        if self.exposition_class == "X0" or self.exposition_class == "XC1":
            self.c_mindur = 0.01
            self.c_dur_gamma = 0
        
        if self.exposition_class == "XC2" or self.exposition_class == "XC3":
            self.c_mindur = 0.02
            self.c_dur_gamma = 0
        
        if self.exposition_class == "XC4":
            self.c_mindur = 0.025
            self.c_dur_gamma = 0
            
        if self.exposition_class == "XD1" or self.exposition_class == "XS1":
            self.c_mindur = 0.03
            self.c_dur_gamma = 0.01
            
        if self.exposition_class == "XD2" or self.exposition_class == "XS2":
            self.c_mindur = 0.035
            self.c_dur_gamma = 0.005

        if self.exposition_class == "XD3" or self.exposition_class == "XS3":
            self.c_mindur = 0.04
            self.c_dur_gamma = 0
            
            
        """Table 4.3 DE"""    
        if self.exposition_class == "XC0" or self.exposition_class == "XC1":
            self.c_mindur = self.c_mindur

        if (self.exposition_class == "XC2" and self.concrete.strength_class >= 25) or \
            (self.exposition_class == "XC3" and self.concrete.strength_class >= 30) or \
            (self.exposition_class == "XC4" and self.concrete.strength_class >= 35) or \
             ((self.exposition_class == "XD1" or self.concrete.strength_class == "XS1") and self.concrete.strength_class >= 40) or\
             ((self.exposition_class == "XD2" or self.concrete.strength_class == "XS2") and self.concrete.strength_class >= 45) or\
             ((self.exposition_class == "XD3" or self.concrete.strength_class == "XS3") and self.concrete.strength_class >= 45):
            self.c_mindur = self.c_mindur - 5


        if self.assummed_rebar_diameter:
            self.concrete_cover = max(0.01, self.c_mindur+self.c_dur_gamma, self.assummed_rebar_diameter)
            
        else:
            if self.reinforcement.hor_rebar_diam and self.reinforcement.vert_rebar_diam:
                self.concrete_cover = max(0.01, self.c_mindur+self.c_dur_gamma, self.reinforcement.vert_rebar_diam)
            else:
                self.concrete_cover = max(0.01, self.c_mindur+self.c_dur_gamma, self.reinforcement.rebar_diameter)                


        if self.assummed_rebar_diameter:
            self.effektive_height = (self.height - self.concrete_cover - self.assummed_rebar_diameter*0.5 - self.deviatoric) 
            
            
        elif self.assummed_rebar_diameter and self.assummed_rebar_diameter_quer:
            
            self.effektive_height = (self.height - self.concrete_cover - self.assummed_rebar_diameter*0.5 - self.deviatoric) 
            
            self.effektive_height_quer = (self.height - self.concrete_cover - self.assummed_rebar_diameter - self.assummed_rebar_diameter_quer*0.5 - self.deviatoric) 
            
            
        else:
            if self.reinforcement.hor_rebar_diam and self.reinforcement.vert_rebar_diam:
                self.effektive_height = (self.height - self.concrete_cover - self.reinforcement.vert_rebar_diam*0.5 - self.deviatoric)    
            else:    
                self.effektive_height = (self.height - self.concrete_cover - self.reinforcement.rebar_diameter*0.5 - self.deviatoric)
                
                if self.reinforcement.rebar_diameter_quer:
                    
                    self.effektive_height_quer = (self.height - self.concrete_cover - self.reinforcement.rebar_diameter - self.reinforcement.rebar_diameter_quer*0.5 - self.deviatoric)
                    


        if self.Hat_Profile_30:
            
            if self.concrete_cover <= 18:
                print("The factory reinforcement can be considered")
                self.effektive_height_factory = self.height - 0.023
                
            else:
                print("The factory reinoforcement cannot be considered")
                self.effektive_height_factory = 0
                
            
            if self.concrete_cover + self.deviatoric < 30 and self.assummed_rebar_diameter:
                
                self.effektive_height = self.height - 0.03 - 0.5*self.assummed_rebar_diameter
                self.effektive_height_quer = self.effektive_height - 0.5*self.assummed_rebar_diameter - 0.5*self.assummed_rebar_diameter_quer
                
            elif self.concrete_cover + self.deviatoric < 30 and self.reinforcement.rebar_diameter:
                
                self.effektive_height = self.height - 0.03 - 0.5*self.reinforcement.rebar_diameter
                self.effektive_height_quer = self.effektive_height - 0.5*self.reinforcement.rebar_diameter - 0.5*self.reinforcement.rebar_diameter_quer
            
            self.effektive_height = (self.reinforcement.As * self.effektive_height + 3.92/10000 * self.effektive_height_factory) / (self.reinforcement.As + 3.92/10000)
            
            if self.concrete_cover <= 18:
                
                self.reinforcement.As = self.reinforcement.As + 3.92/10000
            
            
        if self.Hat_Profile_50:
            
            if self.concrete_cover <= 37:
                print("The factory reinforcement can be considered")
                self.effektive_height_factory = self.height - 0.042
                
            else:
                print("The factory reinoforcement cannot be considered")
                self.effektive_height_factory = 0
            
            if self.concrete_cover + self.deviatoric < 50 and self.assummed_rebar_diameter:
                
                self.effektive_height = self.height - 0.05 - 0.5*self.assummed_rebar_diameter
                self.effektive_height_quer = self.effektive_height - 0.5*self.assummed_rebar_diameter - 0.5*self.assummed_rebar_diameter_quer
                
            elif self.concrete_cover + self.deviatoric < 30 and self.reinforcement.rebar_diameter:
                
                self.effektive_height = self.height - 0.05 - 0.5*self.reinforcement.rebar_diameter
                self.effektive_height_quer = self.effektive_height - 0.5*self.reinforcement.rebar_diameter - 0.5*self.reinforcement.rebar_diameter_quer
                
            
            self.effektive_height = (self.reinforcement.As * self.effektive_height + 3.92/10000 * self.effektive_height_factory) / (self.reinforcement.As + 3.92/10000)

            if self.concrete_cover <= 37:
                
                self.reinforcement.As = self.reinforcement.As + 3.92/10000


                   
        self.rel_compressionLimit = (0.8*self.concrete.ultimate_strain) / \
            (self.concrete.ultimate_strain + 
             ((self.reinforcement.yield_strength / self.reinforcement.gamma) / (self.reinforcement.E*10**3))*10**3)
        
        
        self.absolute_compression_limit = self.effektive_height * self.rel_compressionLimit
        if self.effektive_height_quer:
            self.absolute_compression_limit_quer = self.effektive_height_quer * self.rel_compressionLimit   
        self.cracking_moment = self.concrete.f_ctm*10**3 * self.width * self.height**2 / 6



    def get_moment_of_resistance(self):
        
        
        self.compressionZone = (self.reinforcement.yield_strength / self.reinforcement.gamma)*10**6 * \
        self.reinforcement.As / ((self.concrete.f_ck / self.concrete.gamma)*10**6*self.width)
        
        return round(((self.concrete.f_ck / self.concrete.gamma)*10**6 * self.width * self.compressionZone * \
            (self.effektive_height-0.5*self.compressionZone)) / 10**3, 2)
            
            
    def get_moment_of_resistance_transverse_reinf(self):
        
        
        self.compressionZone = (self.reinforcement.yield_strength / self.reinforcement.gamma)*10**6 * \
        self.reinforcement.As_quer / ((self.concrete.f_ck / self.concrete.gamma)*10**6*self.width)
        
        return round(((self.concrete.f_ck / self.concrete.gamma)*10**6 * self.width * self.compressionZone * \
            (self.effektive_height_quer-0.5*self.compressionZone)) / 10**3, 2)            
             

        
            
class VST_Wall_CS(CrossSection):
    
    def __init__(self, height, wall_height, N_ed, M_ed, V_ed, reinforcement = Reinforcing_Steel, concrete = Concrete, width = 1, exp = "XC1", mesh = "Q_188A", A = 0.7, B = 1.1, C = 0.7, β = 1):
        super().__init__(height, reinforcement, concrete, width, exp)
        self.mesh = mesh
        self.N_ed = N_ed
        self.M_ed = M_ed
        self.V_ed = V_ed
        self.A = A
        self.B = B
        self.C = C
        self.β = β
        self.wall_height = wall_height 
        self.height = height-2*0.024
        self.e_i = wall_height * β / 400
        self.M_imp = N_ed * self.e_i


    def slenderness_check(self):
        self.limit_slenderness = 20*self.A*self.B*self.C / math.sqrt(self.N_ed*1000 / (self.height*self.width*(self.concrete.f_ck*10**6 / self.concrete.gamma)))
        
        radius_gyr_y = math.sqrt( (self.height**3*self.width/12) / (self.height*self.width) )
        radius_gyr_z = math.sqrt( (self.width**3*self.height/12) / (self.height*self.width) )
        
        slenderness_y = self.β*self.wall_height / radius_gyr_y
        slenderness_z = self.β*self.wall_height / radius_gyr_z
        
        self.slender = max(slenderness_y, slenderness_z)
        
        if self.slender >= self.limit_slenderness:
            print("Wall is slender")
            self.slender == True
        else:
            print("Wall is stocky")
            self.slender == False
        
    def define_rebars(self, hor_rebar_diam = 0.006, vert_rebar_diam = 0.006, axial_distance = 0.15):
              
        try:
            self.reinforcement.hor_rebar_diam = hor_rebar_diam
            self.reinforcement.vert_rebar_diam = vert_rebar_diam
            self.reinforcement.axial_distance = axial_distance
            #self.reinforcement.distance_to_edge = distance_to_edge
            'Dopisac metode Na As'
        except(AttributeError):
            print("Method unavailable - prior definition of the reinforcing steel class is required!")

    def min_vert_reinforcement_check(self):
        
        if (self.slender) or (self.N_ed*1000 >= 0.3 * (self.concrete.f_ck*10**6 / self.concrete.gamma) * self.height * self.width):
            
            self.Asm_vert = 0.003 * self.height * self.width
            
        else:
            self.Asm_vert = 0.0015 * self.height * self.width
                        
            
        if 2*( math.pi*(self.reinforcement.vert_rebar_diam**2/4) / self.reinforcement.axial_distance ) >= self.Asm_vert:
            print("Minimum vertical reinforcement has been provided")
        
        else:
            print("Minimum vertical reinforcement condition not fullfilled!")

    def min_hor_reinforcement_check(self):
        
        if (self.slender) or (self.N_ed*1000 >= 0.3 * (self.concrete.f_ck*10**6 / self.concrete.gamma) * self.height * self.width):
            
            self.Asm_hor = 0.5 * self.Asm_vert
        else:
            self.Asm_hor = 0.2 * self.Asm_vert
            
            
        if 2*( math.pi*(self.reinforcement.hor_rebar_diam**2/4) / self.reinforcement.axial_distance ) >= self.Asm_hor:
            print("Minimum horizontal reinforcement has been provided")
        
        else:
            print("Minimum horizontal reinforcement condition not fullfilled!") 

"""            
   def calculate_eccentricity(self.N_ed, self.M_ed, self.wall_height, self.height, self.width):
       
       #minimal eccentricity ist equal to either height / 30 or 0.02 (maximum among these values)  #Seite 63 und 92
    
     
       self.static_eccentricity = M_ed / N_ed
       self.imperfection_eccentrictity = max(self.height / 30, 0.02, self.β*self.wall_height/400)
       
"""    


    
       
        
       
       
          
          
            
            
            
            
            
            
         
            
            
            
            
            
            
            
            
        
        
        





             
             