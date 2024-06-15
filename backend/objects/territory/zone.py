from tools.polygons_action import sort_polygon_points
from tools.polygons_action import polygon_area
from tools.polygons_action import find_polygon_center
from tools.colors import colors_dict

class Zone:
    def __init__(self, coords):
        self.color = colors_dict['white']
        self.name = 'unnamed_zone'
        self.object = None
        self.coords = coords
        self.area_size = polygon_area(self.coords)
        x, z = find_polygon_center(coords)
        self.center_coords = {'x': x, 'z':z}

    def buld_model(self, depth = 0.3 ):

        self.coords = sort_polygon_points(self.coords)
        points = []
        for j in self.coords:
            points.append({'x': j[0], 'z': j[1]})
        # print(random_polygons[i])
        # if i < len(colors):
        #     color = colors[i]
        # else:
        #     color = '0xf0ffff'

        self.object =\
            {
            'type': 'polygon',
            'depth': depth,
            'color': self.color,
            'position': {'x': 0, 'y': -0.01, 'z': 0},
            'points': points,
            }




