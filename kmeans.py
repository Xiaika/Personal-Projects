# Unsupervised Machine Learning Using K-means - From bigideaslittlecode course

from math import fsum, sqrt
from random import sample
from pprint import pprint
from typing import *
from collections import defaultdict
from functools import partial

# Aliasing
Point = Tuple[int, ...]
Centroid = Point


def transpose(data: Iterable[Point]) -> list[Point]:
    """Transpose a matrix: swap rows and columns."""
    return list(zip(*data))


def mean(data: Iterable[float]) -> float:
    """Accurate arithmetic mean"""
    data = list(data)
    return fsum(data) / len(data)


def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt) -> float:
    """Euclidean distance function for multi-dimensional points."""
    return sqrt(fsum([((x - y) ** 2) for x, y in zip(p, q)]))


def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> dict[Centroid, List[Point]]:
    """Group the data points to the closest centroid."""
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))                   # <- Equivalent code
                                        # key=lambda centroid: dist(point, centroid))   <- Equivalent code
        d[closest_centroid].append(point)
    return dict(d)


def compute_centroids(groups: Iterable[Sequence[Point]]) -> list[tuple[float, ...]]:
    """Compute the centroid of each group."""
    return [tuple(map(mean, transpose(group))) for group in groups]
        #  Each centroid is the mean of the transpose of the points in the group


def k_means(data: Iterable[Point], k: int = 2, iterations: int = 50) -> List[Centroid]:
    """Pick arbitrary points as guesses for the center of each group.
       Assign each point to the closest group.
       Average the points in each group to get a new guess for the center.
       Repeat."""
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids


def quality(labeled: Dict[Centroid, Sequence[Point]]) -> float:
    """Mean value of squared distances from data to its assigned centroid"""
    return mean(dist(c, p) ** 2 for c, pts in labeled.items() for p in pts)


if __name__ == '__main__':

    data = [(10, 30),
            (12, 50),
            (14, 70),

            (9, 150),
            (20, 175),
            (8, 200),
            (14, 240),

            (50, 35),
            (40, 50),
            (45, 60),
            (55, 45),

            (60, 130),
            (60, 220),
            (70, 150),
            (60, 190),
            (90, 160), ]

    print('k     quality')
    print('-     -------')
    for k in range(1, 8):
        centroids = k_means(data, k, iterations=50)
        d = assign_data(centroids, data)

        print(f'{k}    {quality(d) :8,.1f}')








