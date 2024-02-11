import math
import matplotlib.pyplot as plt

def bresenham_circle(radius):
    x = 0
    y = radius
    P = 3 - (2 * radius)
    points = []
    points.append([x, y])
    print(f"Point ({x}, {y})")

    while (x < y):
        print("P:", P)
        if (P < 0):
            P = P + (4 * x) + 6
        else:
            y -= 1
            P = P + (4 * x) - (4 * y) + 10  
        x += 1
        print(f"Point ({x}, {y})")
        points.append([x, y])

    reflect_xy = [[0, 1], [1, 0]]
    reflect_x = [[1, 0], [0, -1]]
    reflect_y = [[-1, 0], [0, 1]]

    final_45 = matrix_multiply(points, reflect_xy)
    points.extend(final_45)

    final_x = matrix_multiply(points, reflect_x)
    points.extend(final_x)

    final_y = matrix_multiply(points, reflect_y)
    points.extend(final_y)

    print(" ")
    print(final_y, "\n\n")
    return points

def matrix_multiply(points, reflect):
    result = []
    for i in range(len(points)):
        row = []
        for j in range(len(reflect[0])):
            sum = 0
            for k in range(len(reflect)):
                sum += points[i][k] * reflect[k][j]
            row.append(sum)
        result.append(row)
    return result

def plot_points(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.scatter(x_values, y_values)
    plt.title('Bresenham Circle with Reflections')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

radius = int(input("Enter radius: "))
final_points = bresenham_circle(radius)
plot_points(final_points)