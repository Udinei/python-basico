# refatore o codigo abaixo em funções
# Comparando RNAs Humano e Bactéria 
# acessando arquivos FASTA
entrada = open("../dados/human.fasta").read()

# criando arquivo de saída
saida = open("human.html", "w")

# dicionário para contar dinucleotídeos 
cont = {}

# lista para armazenar as letras dos nucleotídeos   
lista = ['A', 'T', 'C', 'G']

# criando chaves do dicionário para todos os dinucleotídeos possíveis
for i in lista:
    for j in lista:
        cont[i+j] = 0


print(cont)
# saida
# {'AA': 0, 'AT': 0, 'AC': 0, 'AG': 0, 'TA': 0, 'TT': 0, 'TC': 0, 'TG': 0, 'CA': 0, 'CT': 0, 'CC': 0, 'CG': 0, 'GA': 0, 'GT': 0, 'GC': 0, 'GG': 0}   

entrada = entrada.replace("\n", "") 

for k in range(len(entrada)-1):
   # k é o índice do primeiro caractere do par de dinucleotídeos
   # forma o par de dinucleotídeos, ex: AG
    par = entrada[k] + entrada[k+1]
    if par in cont:  # verifica se o par é válido antes de contar
       cont[par] += 1 # incrementa a contagem do dinucleotídeo no dicionário
       
          
print(cont)
# saída

# criando o gráfico de dinucleotídeos em HTML
i=1

# k é o par de dinucleotídeos ex: 'AG'
# e cont[k] é a contagem do par ex: 125
for k in cont:
    # obtem o maior valor de pares de dinucleotídeos
    # transparencia = o valor de cada par dividido pelo par de maior valor, para cria a transparência proporcional à contagem
    transparencia = cont[k]/max(cont.values())
        
    saida.write(
        # usando f-string para formatar a quebra de linha do codigo
        f"<div style='width:100px; border:1px solid #111; height:100px; float:left;"
        f" background-color:rgba(0, 0, 255, "+str(transparencia)+")'>" + k + " " + str(cont[k]) + "</div>"
     )
    
    # a cada 4 divs, cria uma nova linha
    if i%4 == 0:
       saida.write("<div style='clear:both'></div>\n")
    
    # incrementa o contador
    i+=1

saida.close()


