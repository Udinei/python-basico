import matplotlib.pyplot as plt
import random

vetor = []
for i in range(100):
    numero_aleatorio = random.randint(0, 100)
    vetor.append(numero_aleatorio)
    
# Esse grafico mostra a distribuição dos dados em quartis
# O boxplot exibe o valor mínimo, o primeiro quartil (Q1), a mediana (Q2), o terceiro quartil (Q3) e o valor máximo dos dados.
# Os "bigodes" do boxplot indicam a extensão dos dados, enquanto os pontos fora dos bigodes são considerados outliers.
# No primeiro quartil (Q1), 25% dos dados estão abaixo desse valor.
# Na mediana (Q2), 50% dos dados estão abaixo desse valor.      
# No terceiro quartil (Q3), 75% dos dados estão abaixo desse valor.
# Esse comando cria um boxplot com 100 pontos aleatórios
plt.boxplot(vetor)
plt.title("Boxplot: Gráfico de Quartis")
plt.show()
