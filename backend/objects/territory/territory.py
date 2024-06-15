

from tools.colors import colors_dict
class Territory:
    def __init__(self, configuration_dict):
        self.configuration = configuration_dict
        self.levels_num = self.configuration['levels_num']
        self.levels_hight = self.configuration['level_height']
        self.square_size = self.configuration['square_size']
        self.human_capacity = self.configuration['human_capacity']
        self.objects = []


    def create_ground_polygon(self):
        polygon_points = self.configuration['polygon_points']
        self.ground_polygon = polygon_points

    def build_ground_object(self, depth = 0.3):
        points = []
        for i in self.ground_polygon:
            points.append( {'x': 1*i[0], 'z': 1*i[1]})
        self.objects.append({
                'type': 'polygon',
                'depth': depth,
                'color': colors_dict['chartreuse'],
                'position': {'x': 0, 'y': -0.1, 'z': 0},
                'points':  points,
                'name': 'ground'})