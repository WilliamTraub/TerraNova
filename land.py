import math
import sklearn
import numpy as np

class Land:
    def __init__(self, zoning_description = 0, zoning_type = 0, zoning_subtype = 0, lbcs_structure_desc = 0,
                 lat = 0, lon = 0, ll_gissqft = 0, county = 0):
        self.lbcs_structure_desc = self.quant_zoning(lbcs_structure_desc)

        self.county = quant_county(county)
        self.lat = float(lat)
        self.lon = float(lon)
        self.ll_gissqft = float(ll_gissqft)
        self.haversine = self.add_haversine([42.3394, -71.0940])

    def __str__(self):
        return f"{self.county}"
    
    def __array__(self):
        return np.array([[self.haversine, self.county, self.ll_gissqft], [self.lbcs_structure_desc]])

    def add_haversine(self, other, r = 6371000):
        print(other)
        lat1, lat2 = math.radians(self.lat), math.radians(other[0])
        long1, long2 = math.radians(self.lon), math.radians(other[1])

        lat_delta = lat2 - lat1
        long_delta = long2 - long1

        a = (math.sin(lat_delta / 2)) ** 2 + math.cos(lat1) * math.cos(lat2) * \
        (math.sin(long_delta / 2)) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return c * r
   
    def quant_county(self, county):
        COUNTIES = ["barnstable", "berkshire", "bristol", "dukes", "essex", \
            "franklin", "hampden", "hampshire", "middlesex", "nantucket", \
            "norfolk", "plymouth", "suffolk", "worcester"]
        return COUNTIES.index(county)
    def quant_zoning(self):
        zoning_map = {
            "Residential": 0,
            "Commercial": 2,
            "Mixed": 1,
            "Special": 3,
            "Industrial": 4
        }
        if self.zoning_type in zoning_map:
            return zoning_map[self.zoning_type]
        else:
            return 0