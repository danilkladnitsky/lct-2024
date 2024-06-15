import random
from backend.tools.polygons_action import sort_polygon_points

def is_point_in_triangle(pt, v1, v2, v3):
    # Проверка, находится ли точка pt внутри треугольника (v1, v2, v3)
    d1 = (pt[0] - v2[0]) * (v1[1] - v2[1]) - (v1[0] - v2[0]) * (pt[1] - v2[1])
    d2 = (pt[0] - v3[0]) * (v2[1] - v3[1]) - (v2[0] - v3[0]) * (pt[1] - v3[1])
    d3 = (pt[0] - v1[0]) * (v3[1] - v1[1]) - (v3[0] - v1[0]) * (pt[1] - v1[1])
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

def is_convex(v1, v2, v3):
    # Проверка, является ли угол (v1, v2, v3) выпуклым
    return (v2[0] - v1[0]) * (v3[1] - v1[1]) > (v2[1] - v1[1]) * (v3[0] - v1[0])

def triangulate_polygon(polygon_points):
    n = len(polygon_points)
    if n < 3:
        return []  # Невозможно триангулировать менее чем 3 точки

    indices = list(range(n))
    triangles = []

    while len(indices) > 3:
        possible_ears = []
        for i in range(len(indices)):
            i_prev = indices[i - 1]
            i_curr = indices[i]
            i_next = indices[(i + 1) % len(indices)]

            v_prev = polygon_points[i_prev]
            v_curr = polygon_points[i_curr]
            v_next = polygon_points[i_next]

            if is_convex(v_prev, v_curr, v_next):
                is_ear = True
                for j in indices:
                    if j not in [i_prev, i_curr, i_next] and is_point_in_triangle(polygon_points[j], v_prev, v_curr, v_next):
                        is_ear = False
                        break

                if is_ear:
                    possible_ears.append((i_prev, i_curr, i_next, i))

        if not possible_ears:

            return triangulate_polygon( sort_polygon_points(polygon_points) )
            # raise ValueError("The polygon is not simple and cannot be triangulated")

        # Выбираем случайное "ухо"
        ear = random.choice(possible_ears)
        triangles.append((polygon_points[ear[0]], polygon_points[ear[1]], polygon_points[ear[2]]))
        del indices[ear[3]]

    triangles.append((polygon_points[indices[0]], polygon_points[indices[1]], polygon_points[indices[2]]))
    return triangles