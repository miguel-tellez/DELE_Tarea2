import math

def rotate_vector(vector, angle):

  angle = math.radians(angle) if not isinstance(angle, float) else angle


  rotation_matrix = [[math.cos(angle), -math.sin(angle)],
                     [math.sin(angle),  math.cos(angle)]]


  vector_matrix = [[vector[0]], [vector[1]]]

  rotated_vector = np.matmul(rotation_matrix, vector_matrix)

  return [rotated_vector[0][0], rotated_vector[1][0]]

vector = [2, 3]
angle = 45

rotated_vector = rotate_vector(vector, angle)

print(f"vector original: {vector}")
print(f"rotacion vector (angulo: {angle} grados): {rotated_vector}")
