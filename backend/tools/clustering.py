import numpy as np
from sklearn.cluster import KMeans
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union


def get_centroid(triangle):
    return np.mean(triangle, axis=0)


def kmeans_clustering(triangles, target_count):
    # Вычисляем центроиды треугольников
    centroids = np.array([get_centroid(tri) for tri in triangles])

    # Применяем K-means кластеризацию
    kmeans = KMeans(n_clusters=target_count, random_state=0).fit(centroids)
    labels = kmeans.labels_

    # Объединяем треугольники внутри каждого кластера
    clusters = [[] for _ in range(target_count)]
    for i, label in enumerate(labels):
        clusters[label].append(triangles[i])

    # Проверка на пересечение и объединение треугольников
    merged_polygons = []
    for cluster in clusters:
        merged_polygon = merge_cluster_triangles(cluster)
        merged_polygons.append(merged_polygon)

    # Преобразуем объединенные полигоны в списки координат
    merged_polygons_coords = []
    for poly in merged_polygons:
        if isinstance(poly, MultiPolygon):
            for sub_poly in poly.geoms:
                if sub_poly.is_valid:
                    merged_polygons_coords.append(list(sub_poly.exterior.coords))
        elif isinstance(poly, Polygon) and poly.is_valid:
            merged_polygons_coords.append(list(poly.exterior.coords))

    return merged_polygons_coords


def merge_cluster_triangles(cluster_triangles):
    # Объединяем все треугольники в кластере в одну фигуру
    polygons = [Polygon(tri) for tri in cluster_triangles]
    merged_polygon = unary_union(polygons)
    return merged_polygon