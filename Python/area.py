def f(x):
    return x ** 2


def area_bajo_curve(inferior, superior, numero):
    h = (superior - inferior) / numero
    areas = [0.5 * (f(inferior + i * h) + f(inferior + (i + 1) * h)) * h for i in range(numero)]
    area_total = sum(areas)
    return area_total

inferior = 1
superior = 5
numero = 5000

area = area_bajo_curve(inferior, superior, numero)
print("Area bajo la curva:", area)