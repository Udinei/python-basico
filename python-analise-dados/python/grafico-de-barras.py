import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo  = "Gráfico de Barras Simples"
eixox   = "Eixo X"  
eixoy   = "Eixo Y"

#Legenda
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.bar(x, y)
plt.show()
