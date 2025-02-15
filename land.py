class Land:
    def __init__(self, lat, lon, land_value, zoning_law, crime_rate, pop_density):
        self.lat = lat
        self.land_value = land_value
        self.pollution = []
        self.zoning_law = zoning_law
        self.lon = lon
        self.crime_rate = crime_rate
        self.pop_density = pop_density

    def add_pollution(self, var):
        self.pollution.append(var)

    def dist(self, other):
        return ((self.lat - other.lat) ** 2 + (self.lon - other.lon) ** 2) ** 0.5
    
    def calculate_suitability_score(self):
        score = 100 - (self.pollution * 0.5) - (self.crime_rate * 0.3) + (self.green_space * 0.7) + ((100 - self.traffic) * 0.5)
        return max(0, min(score, 100))
    
