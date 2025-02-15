class Land:
    def __init__(self, location, land_value):
        self.location = location
        self.land_value = land_value
        self.pollution = []
    def add_pollution(self, var):
        self.pollution.append(var)