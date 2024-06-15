from shapely.geometry import Polygon, box
from shapely.affinity import rotate, translate
import math

def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
def calculate_angle(rectangle):
    # Вычисляем угол между первой и второй точками прямоугольника
    dx = rectangle[1][0] - rectangle[0][0]
    dy = rectangle[1][1] - rectangle[0][1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

def calculate_T_shape(rectangle):
    # Создаем полигон из координат прямоугольника
    rectangle_polygon = Polygon(rectangle)

    # Вычисляем угол поворота прямоугольника
    angle = calculate_angle(rectangle)

    # Вращаем прямоугольник так, чтобы его стороны были параллельны осям координат
    rotated_rectangle = rotate(rectangle_polygon, -angle, use_radians=False)

    # Находим минимальные и максимальные координаты x и y повернутого прямоугольника
    min_x, min_y, max_x, max_y = rotated_rectangle.bounds

    # Определяем толщину линий буквы "П" (например, 20% от меньшей стороны прямоугольника)
    thickness_x = 0.2 * (max_x - min_x)
    thickness_y = 0.2 * (max_y - min_y)

    # Создаем координаты для фигуры "П" внутри повернутого прямоугольника
    p_shape_coords = [
        (min_x, max_y), # Верхний левый угол
        (min_x, min_y),
        (min_x + thickness_x, min_y),
        (min_x + thickness_x, min_y + thickness_y),
        (max_x - thickness_x, min_y + thickness_y),
        (max_x - thickness_x, min_y),# Нижний левый угол верхней горизонтальной линии
        (max_x, min_y), # Нижний левый угол нижней горизонтальной линии
        (max_x, max_y), # Нижний левый угол
    ]

    # Создаем полигон для фигуры "П"
    p_shape_polygon = Polygon(p_shape_coords)

    # Вращаем фигуру "П" обратно на первоначальный угол поворота
    p_shape_rotated_back = rotate(p_shape_polygon, angle, use_radians=False, origin='centroid')

    # Возвращаем координаты фигуры "П"
    return list(p_shape_rotated_back.exterior.coords)[:-1]


def get_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def generate_smaller_rectangles(rectangle, smaller_width, smaller_height):
    # Создаем полигон из координат прямоугольника
    rectangle_polygon = Polygon(rectangle)

    # Вычисляем угол поворота прямоугольника
    angle = calculate_angle(rectangle)

    # Вращаем прямоугольник так, чтобы его стороны были параллельны осям координат
    rotated_rectangle = rotate(rectangle_polygon, -angle, use_radians=False)

    # Находим минимальные и максимальные координаты x и y повернутого прямоугольника
    min_x, min_y, max_x, max_y = rotated_rectangle.bounds

    # Определяем меньшие стороны прямоугольника
    width = max_x - min_x
    height = max_y - min_y

    if width < height:
        # Меньшие стороны - вертикальные
        side1_midpoint = get_midpoint((0, min_y), (min_x, max_y))
        side2_midpoint = get_midpoint((min_x, min_y), (0, max_y))
        smaller_rect1 = box(side1_midpoint[0] - smaller_width / 2, side1_midpoint[1] - smaller_height / 2,
                            side1_midpoint[0] + smaller_width / 2, side1_midpoint[1] + smaller_height / 2)
        smaller_rect2 = box(side2_midpoint[0] - smaller_width / 2, side2_midpoint[1] - smaller_height / 2,
                            side2_midpoint[0] + smaller_width / 2, side2_midpoint[1] + smaller_height / 2)
    else:
        # Меньшие стороны - горизонтальные
        side1_midpoint = get_midpoint((min_x, min_y), (max_x, min_y))
        side2_midpoint = get_midpoint((min_x, max_y), (max_x, max_y))
        smaller_rect1 = box(side1_midpoint[0] - smaller_width / 2, side1_midpoint[1] - smaller_height / 2,
                            side1_midpoint[0] + smaller_width / 2, side1_midpoint[1] + smaller_height / 2)
        smaller_rect2 = box(side2_midpoint[0] - smaller_width / 2, side2_midpoint[1] - smaller_height / 2,
                            side2_midpoint[0] + smaller_width / 2, side2_midpoint[1] + smaller_height / 2)

    # Вращаем меньшие прямоугольники обратно на первоначальный угол поворота
    smaller_rect1_rotated_back = rotate(smaller_rect1, angle, use_radians=False, origin='centroid')
    smaller_rect2_rotated_back = rotate(smaller_rect2, angle, use_radians=False, origin='centroid')

    # Возвращаем координаты меньших прямоугольников
    return list(smaller_rect1_rotated_back.exterior.coords)[:-1], list(smaller_rect2_rotated_back.exterior.coords)[:-1]
