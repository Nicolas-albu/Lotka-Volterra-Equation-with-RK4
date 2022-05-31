import matplotlib.pyplot as plt
import numpy as np

def RK4_Lotka_Volterra(function_population_one: object, function_population_two: object, 
                      x0: float, y0: float, t0: float, h: float, n: int) -> tuple:
  x: list = [x0]
  y: list = [y0]
  t: list = [t0]

  for i in range(1, n-1):
    t.append(t[i-1] + h)
    K1X: float = h*function_population_one(t[i-1], x[i-1], y[i-1])
    K1Y: float = h*function_population_two(t[i-1], x[i-1], y[i-1])

    K2X: float = h*function_population_one(t[i-1] + h/2, x[i-1] + (h/2) * K1X, y[i-1] + (h/2) * K1Y)
    K2Y: float = h*function_population_two(t[i-1] + h/2, x[i-1] + (h/2) * K1X, y[i-1] + (h/2) * K1Y)

    K3X: float = h*function_population_one(t[i-1] + h/2, x[i-1] + (h/2) * K2X, y[i-1] + (h/2) * K2Y)
    K3Y: float = h*function_population_two(t[i-1] + h/2, x[i-1] + (h/2) * K2X, y[i-1] + (h/2) * K2Y)

    K4X: float = h*function_population_one(t[i-1] + h, x[i-1] + h * K3X, y[i-1] + h * K3Y)
    K4Y: float = h*function_population_two(t[i-1] + h, x[i-1] + h * K3X, y[i-1] + h * K3Y)

    x.append(x[i-1] + (h/6) * (K1X + 2*K2X + 2*K3X + K4X))
    y.append(y[i-1] + (h/6) * (K1Y + 2*K2Y + 2*K3Y + K4Y))

  return x, y, t


if __name__ == '__main__':
  function_population_x = lambda T, X, Y: 0.3*X - 0.7*X*Y
  function_population_y = lambda T, X, Y: X*Y - Y

  x, y, t = RK4_Lotka_Volterra(function_population_one=function_population_x, function_population_two=function_population_y, 
                              x0=1.5, y0=1.5, t0=0, h=0.5, n=100)

  figure, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 10))
  
  ax0.plot(t, x, label="x")
  ax0.plot(t, y, label="y")
  ax0.set(xlabel="t", ylabel="Population", title="Modelo Presa-Predador")
  ax0.legend()
  
  ax1.plot(x, y)
  ax1.set(xlabel="x", ylabel="y", title="Espaço de Fase")

  plt.show()
