class Building:
    def __init__(self, levels_num, levels_hight, square_size):
        self.levels_num = levels_num
        self.levels_hight = levels_hight
        self.square_size = square_size
        self.objects = []


    def build(self, coords):
        ...


        # for i in range(self.levels_num):
        #     self.objects.append({
        #         'type': 'box',
        #          'size': (size[0], self.levels_hight, size[1]),
        #          'color': '0xffffff',
        #          'position': {'x': position['x'], 'y':i*self.levels_hight, 'z': position['z'],
        #         'name': 'level_box_'+str(i)},
        #     })
            # if i == 0:
            #     self.objects.append(
            #             {
            #                 'type': 'box',
            #                 'size': (
            #                     self.levels_hight/10,
            #                     self.levels_hight/1.5,
            #                     self.levels_hight/4),
            #                 'color': '0xff000f',
            #                 'position': {'x': self.levels_hight/2,
            #                              'y': 0,
            #                              'z': 0},
            #                 'name': 'main_door'}
            #         )

        # objects.append(
        #     {'type': 'polygon',
        #      'color': '0xffffff',
        #      'position': {'x': -2, 'y': -2, 'z': 0},
        #     'points': [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 0, 'y': 1}]})


