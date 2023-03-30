import random
import matplotlib.pyplot as plt
import numpy as np

# Definición de la función para simular el lanzamiento de la ruleta
def lanzamiento_ruleta():
    return random.randint(0, 36)

# Definición de la cantidad de lanzamientos
num_lanzamientos = 100

# Simulación de los lanzamientos de la ruleta y almacenamiento de los resultados en una lista
resultados = [lanzamiento_ruleta() for i in range(num_lanzamientos)]

# Cálculo de las estadísticas de los resultados
promedio = np.mean(resultados)
mediana = np.median(resultados)
desviacion_estandar = np.std(resultados)

# Impresión de las tiradas
print("resultados: ", resultados)

# Cálculo de la tabla de frecuencias
valores, frecuencias = np.unique(resultados, return_counts=True)
tabla_frecuencias = np.column_stack((valores, frecuencias))

# Impresión de la tabla de frecuencias
print("Tabla de frecuencias:")
print(tabla_frecuencias)

# Cálculo de la frecuencia absoluta acumulada
frec_abs_acum = np.cumsum(frecuencias)

# Agregar la frecuencia relativa y la frecuencia relativa acumulada a la tabla de frecuencias
tabla_frecuencias_acum = np.column_stack((tabla_frecuencias, frec_abs_acum))

# Impresión de la tabla de frecuencias
print("Tabla de frecuencias acumuladas:")
print(tabla_frecuencias_acum)

# Cálculo de la frecuencia relativa y la frecuencia relativa acumulada
frec_relativa = frecuencias / num_lanzamientos
frec_relativa_acum = np.cumsum(frec_relativa)

# Agregar la frecuencia relativa y la frecuencia relativa acumulada a la tabla de frecuencias
tabla_frecuencias_rel = np.column_stack((tabla_frecuencias, frec_relativa))

# Impresión de la tabla de frecuencias relativas
print("Tabla de frecuencias relativa:")
print(tabla_frecuencias_rel)

# Impresión de las estadísticas
print("Promedio: ", promedio)
print("Mediana: ", mediana)
print("Desviación estándar: ", desviacion_estandar)

# Graficación de los resultados
plt.hist(resultados, bins=range(0, 37, 1))
plt.title("Histograma de resultados de la ruleta")
plt.xlabel("Número")
plt.ylabel("Frecuencia")
plt.show()

# Graficación de los resultados
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 16))

# Gráfica de la frecuencia relativa
ax1.bar(valores, frec_relativa)
ax1.set_title("Frecuencia relativa")
ax1.set_xlabel("Número")
ax1.set_ylabel("Frecuencia relativa")

# Gráfica del valor promedio de las tiradas
ax2.plot([1, num_lanzamientos], [promedio, promedio], 'r--')
ax2.set_title("Valor promedio de las tiradas")
ax2.set_xlabel("Número de tiradas")
ax2.set_ylabel("Valor promedio")

# Gráfica del valor del desvío
desvio_por_tirada = np.zeros(num_lanzamientos)
for i in range(num_lanzamientos):
    desvio_por_tirada[i] = np.std(resultados[:i+1])
ax3.plot(range(num_lanzamientos), desvio_por_tirada)
ax3.set_title("Valor del desvío")
ax3.set_xlabel("Número de tiradas")
ax3.set_ylabel("Valor del desvío")

# Gráfica de la varianza
varianza_por_tirada = np.zeros(num_lanzamientos)
for i in range(num_lanzamientos):
    varianza_por_tirada[i] = np.var(resultados[:i+1])
ax4.plot(range(num_lanzamientos), varianza_por_tirada)
ax4.set_title("Varianza")
ax4.set_xlabel("Número de tiradas")
ax4.set_ylabel("Valor de la Varianza")

plt.tight_layout()
plt.show()