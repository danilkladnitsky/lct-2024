from objects.buldings.bulding import Building
from tools.polygons_action import sort_polygon_points
from tools.colors import colors_dict


class MeetSquare(Building):
    color = colors_dict['burlywood']

    def build(self, coords):

        self.coords = coords
        points = []
        for j in self.coords:
            points.append({'x': j[0], 'z': j[1]})


        self.objects.append(
                {
                    'type': 'polygon',
                    'depth': self.levels_hight,
                    'color': self.color,
                    'position': {'x': 0, 'y': 0, 'z': 0},
                    'points': points,
                })