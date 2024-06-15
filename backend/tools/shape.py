from shapely.geometry import Polygon
from shapely.affinity import rotate, translate
import math

def calculate_angle(rectangle):
    # Вычисляем угол между первой и второй точками прямоугольника
    dx = rectangle[1][0] - rectangle[0][0]
    dy = rectangle[1][1] - rectangle[0][1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

def calculate_u_shape(rectangle):
    # Создаем полигон из координат прямоугольника
    rectangle_polygon = Polygon(rectangle)

    # Вычисляем угол поворота прямоугольника
    angle = calculate_angle(rectangle)

    # Вращаем прямоугольник так, чтобы его стороны были параллельны осям координат
    rotated_rectangle = rotate(rectangle_polygon, -angle, use_radians=False)

    # Находим минимальные и максимальные координаты x и y повернутого прямоугольника
    min_x, min_y, max_x, max_y = rotated_rectangle.bounds

    # Определяем толщину линий буквы "П" (например, 20% от меньшей стороны прямоугольника)
    thickness_x = 0.3 * (max_x - min_x)
    thickness_y = 0.3 * (max_y - min_y)

    # Создаем координаты для фигуры "П" внутри повернутого прямоугольника
    p_shape_coords = [
        (min_x, max_y), # Верхний левый угол
        (min_x, min_y),
        (min_x + thickness_x, min_y),
        (min_x + thickness_x, min_y- thickness_y),
        (max_x - thickness_x, min_y- thickness_y),
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