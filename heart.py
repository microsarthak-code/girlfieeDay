import math

def heart_points(scale=18):

    points = []

    for i in range(2000):

        t = i / 2000 * 2 * math.pi

        x = 16 * math.sin(t) ** 3

        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        points.append((x * scale, -y * scale))

    return points
