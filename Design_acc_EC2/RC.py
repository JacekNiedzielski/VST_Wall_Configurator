import math


class Concrete:
    """\nPlease type the first part of the class as an intiger.
For instance:
            20 for C20/25
            30 for C30/37
and so on...
        """

    def __init__(self, strength_class, gamma=1.5, α_ccpl=1, α_ctpl=1, η=1, ultimate_strain=3.5):

        self.strength_class = strength_class
        self.gamma = gamma
        self.α_ccpl = α_ccpl
        self.α_ctpl = α_ctpl
        self.ultimate_strain = ultimate_strain

        if self.strength_class == 12:

            self.f_ck = 12
            self.f_cm = 20
            self.f_ctm = 1.6
            self.f_ctk005 = 1.1
            self.f_ctk095 = 2
            self.E_Modul = 27000
            self.η = η
            self.name = "C12/15"

        elif self.strength_class == 16:

            self.f_ck = 16
            self.f_cm = 24
            self.f_ctm = 1.9
            self.f_ctk005 = 1.3
            self.f_ctk095 = 2.5
            self.E_Modul = 29000
            self.η = η
            self.name = "C16/20"

        elif self.strength_class == 20:

            self.f_ck = 20
            self.f_cm = 28
            self.f_ctm = 2.2
            self.f_ctk005 = 1.5
            self.f_ctk095 = 2.9
            self.E_Modul = 30000
            self.η = η
            self.name = "C20/25"

        elif self.strength_class == 25:

            self.f_ck = 25
            self.f_cm = 33
            self.f_ctm = 2.6
            self.f_ctk005 = 1.8
            self.f_ctk095 = 3.3
            self.E_Modul = 31000
            self.η = η
            self.name = "C25/30"

        elif self.strength_class == 30:

            self.f_ck = 30
            self.f_cm = 38
            self.f_ctm = 2.9
            self.f_ctk005 = 2
            self.f_ctk095 = 3.8
            self.E_Modul = 32000
            self.η = η
            self.name = "C30/37"

        elif self.strength_class == 35:

            self.f_ck = 35
            self.f_cm = 43
            self.f_ctm = 3.2
            self.f_ctk005 = 2.2
            self.f_ctk095 = 4.2
            self.E_Modul = 34000
            self.η = η
            self.name = "C35/45"

        elif self.strength_class == 40:

            self.f_ck = 40
            self.f_cm = 48
            self.f_ctm = 3.5
            self.f_ctk005 = 2.5
            self.f_ctk095 = 4.6
            self.E_Modul = 35000
            self.η = η
            self.name = "C40/50"

        elif self.strength_class == 45:

            self.f_ck = 45
            self.f_cm = 53
            self.f_ctm = 3.8
            self.f_ctk005 = 2.7
            self.f_ctk095 = 4.9
            self.E_Modul = 36000
            self.η = η
            self.name = "C45/55"

        elif self.strength_class == 50:

            self.f_ck = 50
            self.f_cm = 58
            self.f_ctm = 4.1
            self.f_ctk005 = 2.9
            self.f_ctk095 = 5.3
            self.E_Modul = 37000
            self.η = η
            self.name = "C50/60"

        elif self.strength_class == 55:

            self.f_ck = 55
            self.f_cm = 63
            self.f_ctm = 4.2
            self.f_ctk005 = 3.0
            self.f_ctk095 = 5.5
            self.E_Modul = 38000
            self.η = 1 - (self.f_ck - 50) / 200
            self.name = "C55/67"

        elif self.strength_class == 60:

            self.f_ck = 60
            self.f_cm = 68
            self.f_ctm = 4.4
            self.f_ctk005 = 3.1
            self.f_ctk095 = 5.7
            self.E_Modul = 39000
            self.η = 1 - (self.f_ck - 50) / 200
            self.name = "C60/75"

        elif self.strength_class == 70:

            self.f_ck = 70
            self.f_cm = 78
            self.f_ctm = 4.6
            self.f_ctk005 = 3.2
            self.f_ctk095 = 6.0
            self.E_Modul = 41000
            self.η = 1 - (self.f_ck - 50) / 200
            self.name = "C70/85"

        elif self.strength_class == 80:

            self.f_ck = 80
            self.f_cm = 88
            self.f_ctm = 4.8
            self.f_ctk005 = 3.4
            self.f_ctk095 = 6.3
            self.E_Modul = 42000
            self.η = 1 - (self.f_ck - 50) / 200
            self.name = "C80/95"

        elif self.strength_class == 90:

            self.f_ck = 90
            self.f_cm = 98
            self.f_ctm = 5
            self.f_ctk005 = 3.5
            self.f_ctk095 = 6.6
            self.E_Modul = 44000
            self.η = 1 - (self.f_ck - 50) / 200
            self.name = "C90/105"


class Reinforcing_Steel:
    """\nPlease type the intiger as a class of steel.
For instance:
            500 for steel with yield strength 500 MPa
        """

    def __init__(self, steel_class=500, E=200, gamma=1.15):
        self.E = E
        self.yield_strength = steel_class
        self.gamma = gamma
        self.name = str(steel_class)
        # self.rebar_diameter = rebar_diameter
        # self.rebar_number = rebar_number
        # self.axial_distance = axial_distance
        # self.distance_to_edge = distance_to_edge