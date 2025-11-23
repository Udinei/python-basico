import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

# cada  ponto tem um tamanho de s diferente
SizePtos = [15, 200, 30, 400, 150]

titulo  = "Scatterplot: Gráfico de Dispersão"
eixox   = "Eixo X"  
eixoy   = "Eixo Y"

#Legenda
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

 # Gráfico de Dispersão, com pontos e linha, s é o tamanho dos pontos   
plt.scatter(x, y, color='red', linestyle='--', label='Meus Pontos', s=SizePtos) 
plt.plot(x, y)   

#plt.show()
#plt.savefig("figura1.png", dpi=300) #salva a figura em png  
plt.savefig("figura1.pdf", dpi=300) #salva a figura em png  
