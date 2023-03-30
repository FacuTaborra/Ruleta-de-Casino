import random
import matplotlib.pyplot as plt
import numpy as np

# Número de tiradas
num_tiradas = 1000

# Lista para almacenar los resultados de las tiradas
resultados = []

# Realizar las tiradas
for i in range(num_tiradas):
    resultados.append(random.randint(0, 36))

# Cálculo de estadísticas
promedio = sum(resultados)/num_tiradas
mediana = np.median(resultados)
varianza = np.var(resultados)
desvio_estandar = np.std(resultados)

# Cálculo de la frecuencia relativa
frecuencia_relativa = [resultados.count(i)/num_tiradas for i in range(37)]

# Gráfico del promedio por número de tiradas
promedio_por_tirada = []
for i in range(num_tiradas):
    promedio_por_tirada.append(sum(resultados[0:i+1])/(i+1))

plt.plot(range(1, num_tiradas+1), promedio_por_tirada)
plt.title('Promedio por número de tiradas')
plt.xlabel('Número de tiradas')
plt.ylabel('Promedio')
plt.show()

# Gráfico de la varianza por número de tiradas
varianza_por_tirada = []
for i in range(num_tiradas):
    varianza_por_tirada.append(np.var(resultados[0:i+1]))

plt.plot(range(1, num_tiradas+1), varianza_por_tirada)
plt.title('Varianza por número de tiradas')
plt.xlabel('Número de tiradas')
plt.ylabel('Varianza')
plt.show()

# Gráfico del desvío estándar por número de tiradas
desvio_por_tirada = []
for i in range(num_tiradas):
    desvio_por_tirada.append(np.std(resultados[0:i+1]))

plt.plot(range(1, num_tiradas+1), desvio_por_tirada)
plt.title('Desvío estándar por número de tiradas')
plt.xlabel('Número de tiradas')
plt.ylabel('Desvío estándar')
plt.show()

# Gráfico de la frecuencia relativa
plt.bar(range(37), frecuencia_relativa)
plt.title('Frecuencia relativa')
plt.xlabel('Número')
plt.ylabel('Frecuencia relativa')
plt.show()