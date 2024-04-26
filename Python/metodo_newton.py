def f(x):
  return x**3 + 3

def derivada_f(x):
  return 3*x**2

def metodo_newton(x0, tol=1e-5, max_iteracion=100):
  for i in range(max_iteracion):
    fx = f(x0)
    dfx = derivada_f(x0)
    if abs(fx) < tol:
      return x0
    x0 = x0 - fx / dfx
  print("No se encontro la raiz en el maximo numero de iteraciones")
  return x0
x0 = -1
root = metodo_newton(x0)
print(f"La raiz de la funcion f(x) = x^3 + 3 se encuentra en x = {root:.5f}")
