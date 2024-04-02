# Code to perform 2D transformations like translation, rotation, scaling, and shearing

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

def matrix_multiplication(matrix_a, matrix_b):
  result_rows = len(matrix_a)
  result_cols = len(matrix_b[0])
  result_matrix = [[0] * result_cols for _ in range(result_rows)]
  for i in range(result_rows):
    for j in range(result_cols):
      result_matrix[i][j] = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
  return result_matrix

def transformations(matrix, points):
  homogenous_points = np.array([[point[0], point[1], 1] for point in points])
  transformed_points = np.dot(homogenous_points, np.array(matrix).T)
  transformed_points = [[point[0] / point[2], point[1] / point[2]] for point in transformed_points]
  return transformed_points
  transformed_points = matrix_multiply(homogenous_points, matrix)
  transformed_points = [[points[0] / point[2], point[1] / point[2]] for point in transformed_points]
  return transformed_points

def plot_polygon(ax, points, color, label):
  polygon = Polygon(points, closed = True, fill = None, edgecolor = color, linewidth = 2, label = label)
  ax.add_patch(polygon)

original_polygon = [[0, 1], [0, 0], [1, 0], [1, 1]]
print("Choose a transformation: ")
print("1. Translation")
print("2. Rotation")
print("3. Scaling")
print("4. Shearing")
print(" ")
choice = int(input("Your choice: "))
print(" ")

# Translation
if (choice == 1):
  translation_x = float(input("Enter translation in the x-axis: "))
  translation_y = float(input("Enter translation in the y-axis: "))
  transformation_matrix = [[1, 0, translation_x], [0, 1, translation_y], [0, 0, 1]]

# Rotation
elif (choice == 2):
  theta = float(input("Enter rotation angle (in degrees): "))
  angle = np.radians(theta)
  transformation_matrix = [[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]]

# Scaling
elif (choice == 3):
  scaling_x = float(input("Enter scaling factor in the x-axis: ")) 
  scaling_y = float(input("Enter scaling factor in the y-axis: ")) 
  transformation_matrix = [[scaling_x, 0, 0], [0, scaling_y, 0], [0, 0, 1]]

# Shearing
elif (choice == 4):
  shear_x = float(input("Enter shear factor in the x-axis: "))
  shear_y = float(input("Enter shear factor in the y-axis: "))
  transformation_matrix = [[1, shear_x, 0], [shear_y, 1, 0], [0, 0, 1]]

else:
  print("Invalid choice!")
  exit()

transformed_polygon = transformations(transformation_matrix, original_polygon)

fig, ax = plt.subplots()
plot_polygon(ax, original_polygon, 'blue', 'Original figure')
plot_polygon(ax, transformed_polygon, 'green', 'Transformed figure')
ax.set_aspect('equal', adjustable = 'box')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.legend()
plt.title("2D Transformations")
plt.show()

print("Original polygon: ", original_polygon)
print("Transformed polygon: ", transformed_polygon)
