import math
import random
from shapely.geometry import Polygon, box
from shapely.affinity import rotate
from shapely.affinity import translate
from shapely.geometry import Polygon, MultiPolygon


def find_polygon_center(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    center_x = sum(x_coords) / len(points)
    center_y = sum(y_coords) / len(y_coords)
    return center_x, center_y

def angle_from_center(center, point):
    return math.atan2(point[1] - center[1], point[0] - center[0])

def sort_polygon_points(points):
    center = find_polygon_center(points)
    sorted_points = sorted(points, key=lambda p: angle_from_center(center, p))
    return sorted_points

############################################################################################
def generate_polygon(sides, radius=1, center=(0, 0)):
    angle_step = 2 * math.pi / sides
    points = [
        (
            center[0] + radius * math.cos(i * angle_step),
            center[1] + radius * math.sin(i * angle_step)
        )
        for i in range(sides)
    ]
    return points


def multiply_polygon_vertices(points, multiplier):
    if multiplier < 2:
        raise ValueError("Multiplier must be 2 or greater")

    new_points = []
    num_points = len(points)

    for i in range(num_points):
        p1 = points[i]
        p2 = points[(i + 1) % num_points]  # Следующая точка (с учётом замыкания полигона)

        new_points.append(p1)

        # Создание дополнительных точек между p1 и p2
        for j in range(1, multiplier):
            factor = j / multiplier
            mid_point = (
                p1[0] + (p2[0] - p1[0]) * factor,
                p1[1] + (p2[1] - p1[1]) * factor
            )
            new_points.append(mid_point)

    return new_points


def generate_random_polygon(num_vertices, x_range=(0, 10), y_range=(0, 10)):
    points = [
        (random.uniform(*x_range), random.uniform(*y_range))
        for _ in range(num_vertices)
    ]

    center_x = sum(p[0] for p in points) / num_vertices
    center_y = sum(p[1] for p in points) / num_vertices
    center = (center_x, center_y)

    sorted_points = sorted(points, key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))

    return sorted_points


def polygon_area(coords):
    n = len(coords)
    if n < 3:
        return 0  # Площадь неопределена для менее чем 3 точек

    area = 0.0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    area = abs(area) / 2.0
    return area


def place_rectangles(polygon_coords, rectangles):
    # Создаем полигон из входных координат
    polygon = Polygon(polygon_coords)
    if not polygon.is_valid:
        raise ValueError("Невалидные координаты полигона")

    # Список для хранения размещенных прямоугольников
    placed_rectangles = []

    # Стартовые координаты для размещения
    start_x, start_y = polygon.bounds[0], polygon.bounds[1]

    # Функция для попытки размещения прямоугольника в полигоне с разными углами
    def try_place_rectangle(polygon, rect_width, rect_height):
        minx, miny, maxx, maxy = polygon.bounds
        for angle in range(0, 360, 10):  # Пробуем углы с шагом в 10 градусов
            for _ in range(100):  # Попытки разместить прямоугольник
                rect_x = random.uniform(minx, maxx - rect_width)
                rect_y = random.uniform(miny, maxy - rect_height)
                rect = box(rect_x, rect_y, rect_x + rect_width, rect_y + rect_height)
                rect = rotate(rect, angle, origin='centroid')
                if polygon.contains(rect):
                    return rect
        return None

    # Функция для попытки размещения прямоугольника состыкованным
    def try_place_rectangle_stacked(polygon, rect_width, rect_height, current_x, current_y):
        rect = box(current_x, current_y, current_x + rect_width, current_y + rect_height)
        if polygon.contains(rect):
            return rect
        return None

    current_x, current_y = start_x, start_y
    max_y_in_row = start_y

    for rect_width, rect_height in rectangles:
        rect = try_place_rectangle_stacked(polygon, rect_width, rect_height, current_x, current_y)
        if rect:
            placed_rectangles.append(rect)
            polygon = polygon.difference(rect)
            current_x += rect_width
            max_y_in_row = max(max_y_in_row, current_y + rect_height)

            # Если мы достигли края полигона по X, переходим на новую строку
            if current_x >= polygon.bounds[2]:
                current_x = start_x
                current_y = max_y_in_row
        else:
            # Попробуем разместить прямоугольник произвольным образом
            rect = try_place_rectangle(polygon, rect_width, rect_height)
            if rect:
                placed_rectangles.append(rect)
                polygon = polygon.difference(rect)
            else:
                raise ValueError(f"Не удалось разместить прямоугольник размером {(rect_width, rect_height)}")

    # Возвращаем координаты размещенных прямоугольников
    return [list(rect.exterior.coords)[:-1] for rect in placed_rectangles]

def calculate_area(polygon):
    return polygon.area


def align_rectangles(rectangles):
    # Преобразуем входные координаты в объекты Polygon и вычисляем их площади
    polygons = [(Polygon(rect), calculate_area(Polygon(rect))) for rect in rectangles]

    # Находим наибольший прямоугольник
    largest_polygon, largest_area = max(polygons, key=lambda x: x[1])
    polygons.remove((largest_polygon, largest_area))

    # Список для хранения сдвинутых прямоугольников
    aligned_rectangles = [list(largest_polygon.exterior.coords)[:-1]]

    for polygon, _ in polygons:
        # Перемещаем текущий прямоугольник, чтобы он присоединился к большому по внешней грани
        min_dist = float('inf')
        best_translation = None

        for lpt in largest_polygon.exterior.coords[:-1]:
            for rpt in polygon.exterior.coords[:-1]:
                dx = lpt[0] - rpt[0]
                dy = lpt[1] - rpt[1]
                translated_polygon = translate(polygon, xoff=dx, yoff=dy)
                if largest_polygon.touches(translated_polygon):
                    dist = math.hypot(dx, dy)
                    if dist < min_dist:
                        min_dist = dist
                        best_translation = (dx, dy)

        if best_translation:
            translated_polygon = translate(polygon, xoff=best_translation[0], yoff=best_translation[1])
            aligned_rectangles.append(list(translated_polygon.exterior.coords)[:-1])
            largest_polygon = largest_polygon.union(translated_polygon)

    return aligned_rectangles


def get_random_dimensions(area):
    # Генерируем случайное число от 1 до корня из площади
    width = random.uniform(1, area ** 0.5)

    # Вычисляем длину, деля площадь на ширину
    height = area / width

    return width, height