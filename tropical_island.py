"""
The island of size m * n has different heights represented by the number.
Find how much water will stay on the island after the rain.
"""


import collections


def get_water_volume(island):
    m = len(island[0])
    n = len(island)

    if m <= 2 or n <= 2:
        return 0

    border = set([(i, 0) for i in range(n)] +
                 [(i, m - 1) for i in range(n)] +
                 [(0, i) for i in range(m)] +
                 [(n - 1, i) for i in range(m)])

    lowest_on_border = min(island[i][j] for (i, j) in border)
    highest_on_island = max(map(max, island))

    edges = collections.defaultdict(set)

    for (i, j) in border:
        edges[island[i][j]].add((i, j))

    water_on_island = [[0 for i in range(m)] for j in range(n)]

    for level in range(lowest_on_border, highest_on_island + 1):
        while edges[level]:
            (i, j) = edges[level].pop()
            water_on_island[i][j] = level
            for ii, jj in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= ii < n and m > jj >= 0 == water_on_island[ii][jj]:
                    edges[max(level, island[ii][jj])].add((ii, jj))

    water = sum(water_on_island[i][j] - island[i][j] for i in range(n) for j in range(m))
    return water

