import math

class Land:
    def __init__(self, lat, lon, land_value = 0):
        self.lat = lat
        self.lon = lon
        self.land_value = land_value

    def __str__(self):
        return f"{self.haversine}"
    
    def add_haversine(self, other):
        lat1, lat2 = math.radians(self.lat), math.radians(other.lat)
        long1, long2 = math.radians(self.lon), math.radians(other.lon)

        lat_delta = lat2 - lat1
        long_delta = long2 - long1

        a = (math.sin(lat_delta / 2)) ** 2 + math.cos(lat1) * math.cos(lat2) * \
        (math.sin(long_delta / 2)) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        self.haversine = c * r

    def dist(self, other):
        return ((self.lat - other.lat) ** 2 + (self.lon - other.lon) ** 2) ** 0.5
    
    def calculate_suitability_score(self):
        score = 100 - (self.pollution * 0.5) - (self.crime_rate * 0.3) + (self.green_space * 0.7) + ((100 - self.traffic) * 0.5)
        return max(0, min(score, 100))
    
