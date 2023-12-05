with open("./input.txt", "r") as f:
	lines = f.read().split('\n')

seeds = map(int, lines[0].split(':')[1].strip().split())

class Map:
	def __init__(self, dst_start, src_start, range_length):
		self.dst_start = dst_start
		self.src_start = src_start
		self.range_length = range_length

	def map_src_to_dst(self, source):
		if self.src_start <= source < self.src_start + self.range_length:
			offset = source - self.src_start
			return self.dst_start + offset
		else:
			return source

class Alamanac:
	def __init__(self):
		self.seed_to_soil_maps = []
		self.soil_to_fertilizer_maps = []
		self.fertilizer_to_water_maps = []
		self.water_to_light_maps = []
		self.light_to_temperature_maps = []
		self.temperature_to_humidity_maps = []
		self.humidity_to_location_maps = []
	
	def add_map(self, dst_start, src_start, range_length, maps_array):
		mapping = Map(dst_start, src_start, range_length)
		maps_array.append(mapping)

	def map_seed_to_location(self, seed):
		soil = self.map_seed_to_soil(seed)
		fert = self.map_soil_to_fert(soil)
		water = self.map_fert_to_water(fert)
		light = self.map_water_to_light(water)
		temp = self.map_light_to_temp(light)
		humid = self.map_temp_to_humidity(temp)
		loc = self.map_humid_to_loc(humid)
		print(f"Seed {seed}, soil {soil}, fertilizer {fert}, water {water}, light {light}, temperature {temp}, humidity {humid}, location {loc}")
		return loc

	def map_seed_to_soil(self, seed):
		for mapping in self.seed_to_soil_maps:
			soil = mapping.map_src_to_dst(seed)
			if soil != seed:
				break
		return soil
	
	def map_soil_to_fert(self, soil):
		for mapping in self.soil_to_fertilizer_maps:
			fert = mapping.map_src_to_dst(soil)
			if fert != soil:
				break
		return fert
	
	def map_fert_to_water(self, fert):
		for mapping in self.fertilizer_to_water_maps:
			water = mapping.map_src_to_dst(fert)
			if water != fert:
				break
		return water

	def map_water_to_light(self, water):
		for mapping in self.water_to_light_maps:
			light = mapping.map_src_to_dst(water)
			if light != water:
				break
		return light

	def map_light_to_temp(self, light):
		for mapping in self.light_to_temperature_maps:
			temp = mapping.map_src_to_dst(light)
			if temp != light:
				break
		return temp

	def map_temp_to_humidity(self, temp):
		for mapping in self.temperature_to_humidity_maps:
			humid = mapping.map_src_to_dst(temp)
			if humid != temp:
				break
		return humid

	def map_humid_to_loc(self, temp):
		for mapping in self.humidity_to_location_maps:
			loc = mapping.map_src_to_dst(temp)
			if loc != temp:
				break
		return loc

almanac = Alamanac()

map_type = None
for line in lines:
	if not line.strip():
		continue
	
	if line.startswith('seed-to-soil'):
		map_type = 0
		continue
	elif line.startswith('soil-to-fertilizer'):
		map_type = 1
		continue
	elif line.startswith('fertilizer-to-water'):
		map_type = 2
		continue
	elif line.startswith('water-to-light'):
		map_type = 3
		continue
	elif line.startswith('light-to-temperature'):
		map_type = 4
		continue
	elif line.startswith('temperature-to-humidity'):
		map_type = 5
		continue
	elif line.startswith('humidity-to-location'):
		map_type = 6
		continue
	
	if (map_type == 0):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.seed_to_soil_maps)
	elif (map_type == 1):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.soil_to_fertilizer_maps)
	elif (map_type == 2):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.fertilizer_to_water_maps)
	elif (map_type == 3):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.water_to_light_maps)
	elif (map_type == 4):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.light_to_temperature_maps)
	elif (map_type == 5):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.temperature_to_humidity_maps)
	elif (map_type == 6):
		values = map(int, line.split())
		almanac.add_map(*values, almanac.humidity_to_location_maps)

locations = []
for seed in seeds:
	locations.append(almanac.map_seed_to_location(seed))

print(min(locations))