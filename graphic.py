import matplotlib.pyplot as plt
import numpy as np

# Supongamos que estas son tus listas de datos
x = hcn = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160]
y = []

for i in range(len(x)):
    y.append(i)

# Crear el gráfico
plt.figure(figsize=(10, 5))  # Ajustar el tamaño de la figura para acomodar las etiquetas
plt.plot(x, y, 'o')  

# Agregar números a los puntos
for i, txt in enumerate(hcn):
    plt.text(x[i], y[i], txt, fontsize=8)  # Puedes ajustar el tamaño de la fuente con el parámetro fontsize

# Etiquetas de los ejes
plt.xlabel('Highly composite numbers')
plt.ylabel('H(x)')

# Título del gráfico
plt.title('Distribution of Highly Composite Numbers')

# Ajustar el layout para evitar que las etiquetas se corten
plt.tight_layout()

# Mostrar el gráfico
plt.show()