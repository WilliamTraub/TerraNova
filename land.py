import math

class Land:
    def __init__(self, zoning_description = "", zoning_type = "", zoning_subtype = "", landval = 0, lat = 0, lon = 0, sqft = 0):
        self.zoning_desc = zoning_description
        self.zoning_type = zoning_type
        self.zoning_sub = zoning_subtype
        self.land_val = int(landval)
        self.lat = float(lat)
        self.lon = float(lon)
        self.sqft = int(sqft)

    def __str__(self):
        return f"{self.sqft}"
    
    def add_haversine(self, other, r = 6371000):
        lat1, lat2 = math.radians(self.lat), math.radians(other.lat)
        long1, long2 = math.radians(self.lon), math.radians(other.lon)

        lat_delta = lat2 - lat1
        long_delta = long2 - long1

        a = (math.sin(lat_delta / 2)) ** 2 + math.cos(lat1) * math.cos(lat2) * \
        (math.sin(long_delta / 2)) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        self.haversine = c * r


    
