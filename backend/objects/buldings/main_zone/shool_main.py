from objects.buldings.bulding import Building
from tools.colors import colors_dict
from tools.shape import calculate_T_shape

class ShoolMain(Building):
    color = colors_dict['gray']
    door_color = colors_dict['red']


    def build(self, coords, configuration):
        print(coords)
        self.coords = coords
        coords = calculate_T_shape(coords)
        points = []
        for j in coords:
            points.append({'x': j[0], 'z': j[1]})

        for i in range(self.levels_num):
            self.objects.append(
                    {
                        'type': 'polygon',
                        'depth': self.levels_hight,
                        'color': self.color,
                        'position':
                            {'x': 0,
                             'y': (i+1)*self.levels_hight + 0.01*i,
                             'z': 0},
                        'points': points,
                    })

        window_size = (0.009, self.levels_hight*0.6)
        for i in range(len(coords)):

            ...

        # print(coords[4][0])
        door_coords = [ (coords[4][0] + coords[5][0])/2 , (coords[4][1] + coords[5][1])/2  ]
        print(door_coords)
        door_coords = [
            (door_coords[0] + 0.01, door_coords[1] - 0.01),
            (door_coords[0] + 0.01, door_coords[1] + 0.01),
            (door_coords[0] - 0.01, door_coords[1] + 0.01),
            (door_coords[0] - 0.01, door_coords[1] - 0.01)
        ]

        points = []
        for j in door_coords:
            points.append({'x': j[0], 'z': j[1]})

        self.objects.append(
            {
                'type':     'polygon',
                'depth':    0.021,
                'color':    self.door_color,
                'position': {'x': 0,
                             'y': 0.021,
                             'z': 0
                             },
                'points':   points,
            })

        if configuration['has_junior'] and configuration['has_junior_hight_connection']:
            door_coords = [(coords[2][0] + coords[3][0]) / 2, (coords[2][1] + coords[3][1]) / 2]
            print(door_coords)
            door_coords = [
                (door_coords[0] + 0.01, door_coords[1] - 0.01),
                (door_coords[0] + 0.01, door_coords[1] + 0.01),
                (door_coords[0] - 0.01, door_coords[1] + 0.01),
                (door_coords[0] - 0.01, door_coords[1] - 0.01)
            ]

            points = []
            for j in door_coords:
                points.append({'x': j[0], 'z': j[1]})

            self.objects.append(
                {
                    'type': 'polygon',
                    'depth': 0.021,
                    'color': self.door_color,
                    'position': {'x': 0,
                                 'y': 0.021,
                                 'z': 0
                                 },
                    'points': points,
                })

