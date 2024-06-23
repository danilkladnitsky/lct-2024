import math


def lat_lon_to_meters(lat, lon):
    """Преобразование географических координат в метры с использованием проекции Меркатора."""
    origin_shift = 2 * math.pi * 6378137 / 2.0
    mx = lon * origin_shift / 180.0
    my = math.log(math.tan((90 + lat) * math.pi / 360.0)) / (math.pi / 180.0)
    my = my * origin_shift / 180.0
    return mx, my


def meters_to_custom_units(mx, my, scale=100):
    """Преобразование метров в пользовательские единицы, где 1 = 100 метров."""
    return mx / scale, my / scale


def convert_coordinates(lat, lon, scale=100):
    """Функция для преобразования координат."""
    mx, my = lat_lon_to_meters(lat, lon)
    ux, uy = meters_to_custom_units(mx, my, scale)
    return ux, uy


def map_coords_convert(map_coords):
    min_lon, min_lat = 99999999, 9999999
    for i in range(len(map_coords)):
        map_coords[i][0], map_coords[i][1] = convert_coordinates(
            map_coords[i][0], map_coords[i][1])
        min_lon = map_coords[i][0] if map_coords[i][0] < min_lon else min_lon
        min_lat = map_coords[i][1] if map_coords[i][1] < min_lat else min_lat
    # print(min_lon, min_lat)
    for i in range(len(map_coords)):
        map_coords[i][0], map_coords[i][1] = round(
            map_coords[i][0] - min_lon, 6), round(map_coords[i][1] - min_lat, 6)

    return map_coords


# coords =[[30.321874417664986,59.93173348692616], [30.32544184925149, 59.93239014996115], [30.31950058666655,59.93421708175586], [30.318523290673937,59.93342823216392]]
#
# print(map_coords_convert(coords))
