from objects.buldings.bulding import Building
from tools.colors import colors_dict
from tools.shape import calculate_u_shape

class ShoolMain(Building):
    color = colors_dict['gray']


    def build(self, coords):
        print(coords)
        self.coords = coords
        coords = calculate_u_shape(coords)
        points = []
        for j in coords:
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

