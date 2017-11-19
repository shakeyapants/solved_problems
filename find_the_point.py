"""
The problem about point reflection
"""

num_sets = int(input().strip())

coordinates = []
for line in range(num_sets):
    points = [int(x) for x in input().strip().split()]
    coordinates.append(points)

for point in coordinates:
    diff_x = point[2] - point[0]
    diff_y = point[3] - point[1]
    print(point[2] + diff_x, point[3] + diff_y)
