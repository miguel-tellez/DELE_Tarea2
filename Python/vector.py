import numpy as np

def projection(a, b):
  a = np.asarray(a)
  b = np.asarray(b)

  if a.shape != b.shape:
    raise ValueError("Los vectores de entrada deben tener las mismas dimensiones.")

  dot_product = np.dot(a, b)

  magnitude_b_squared = np.dot(b, b)

  if not np.any(b):
    return np.zeros_like(a)
  projection_vec = (dot_product / magnitude_b_squared) * b
  return projection_vec

vector_a = np.array([2, 3])
vector_b = np.array([1, 4])

projection_result = projection(vector_a, vector_b)

print(f"proyeccion de un vector a({vector_a}) vector b ({vector_b}) es:")
print(projection_result)
