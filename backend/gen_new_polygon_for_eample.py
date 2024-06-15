from tools.polygons_action import generate_polygon
from tools.polygons_action import generate_random_polygon
import json

# objects = [
#     {'type': 'box', 'size': (1,1, 3), 'color': '0x00ff00', 'position': {'x': 0, 'y': 0, 'z': 0}},
#     {'type': 'box', 'size': (1,1, 2), 'color': '0xff0000', 'position': {'x': 0, 'y': 1, 'z': 0}},
#     {'type': 'box', 'size': (1,1, 1), 'color': '0x0000ff', 'position': {'x': 0, 'y': 2, 'z': 0}}
# ]
# polygons = [[(0, 0), (-1, 0), (-1, 1), (-2, 1), (-2, -1),(0,-1), (2,-1), (2,1), (1,1), (1,0)],
#             generate_polygon(12, 2, (0,0)),
#             [(0, 0), (0.5, 1.5), (1.5, 2), (2.5, 1.5), (3, 0.5), (2, -0.5), (1, -1)]]
#
# ground_polygon = generate_random_polygon(13, x_range=(0, 5), y_range=(0, 4))


with open('example_request.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data['polygon_points'] = generate_polygon(12, 1.6, (0,0))

with open('example_request.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent = 4)