import math

class Tire:
    """
    Ture represents a tire that would be used with an automobile.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand = '', construction = 'R'):
         self.tire_type = tire_type
         self.width = width
         self.ratio = ratio
         self.diameter = diameter
         self.brand = brand
         self.construction = construction
    
    def circumference(self):
        """
       The circumference of the tire in inches.

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """

        side_wall_inches = self._side_wall_inches()
        total_diameter = side_wall_inches * 2 + self.diameter
        return round(total_diameter * math.pi, 1)
    
    def _side_wall_inches(self):
        return self.width * (self.ratio / 100)/25.4

    def __repr__(self):
        """
        Represent the tire's information in the standard notation present
        on the side of the tire. Example: 'P215/65R15'
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}" + f"{self.construction}{self.diameter}")

    

class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand=brand, construction=construction)
        self.chain_thickeness = chain_thickness

    def __repr__(self):
        return super().__repr__() + "  (Snow)"






if __name__ == "__main__":
    import doctest
    doctest.testmod()