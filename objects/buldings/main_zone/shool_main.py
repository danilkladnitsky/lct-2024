from objects.buldings.bulding import Building
from tools.polygons_action import sort_polygon_points
from tools.colors import colors_dict


class ShoolMain(Building):
    color = colors_dict['gray']

    def build(self, coords):

        self.coords = coords
        points = []
        for j in self.coords:
            points.append({'x': j[0], 'z': j[1]})

        for i in range(self.levels_num):
            self.objects.append(
                    {
                        'type': 'polygon',
                        'depth': self.levels_hight,
                        'color': self.color,
                        'position': {'x': 0, 'y': (i+1)*self.levels_hight + 0.01*i, 'z': 0},
                        'points': points,
                    })