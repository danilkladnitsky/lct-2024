from objects.buldings.bulding import Building
from tools.colors import colors_dict
from tools.shape import generate_smaller_rectangles

class FootBallField(Building):
    color = colors_dict['olive']
    gate_color = colors_dict['white']

    def build(self, coords):

        self.coords = coords

        rec1, rec2 = generate_smaller_rectangles(coords, 0.08, 0.03)

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
                }
        )

        points = []
        for j in rec1:
            points.append({'x': j[0], 'z': j[1]})

        self.objects.append(
                {
                    'type': 'polygon',
                    'depth': 0.03,
                    'color': self.gate_color,
                    'position': {'x': 0, 'y': 0.03, 'z': 0},
                    'points': points,
                }
        )

        points = []
        for j in rec2:
            points.append({'x': j[0], 'z': j[1]})

        self.objects.append(
                {
                    'type': 'polygon',
                    'depth': 0.03,
                    'color': self.gate_color,
                    'position': {'x': 0, 'y': 0.03, 'z': 0},
                    'points': points,
                }
        )