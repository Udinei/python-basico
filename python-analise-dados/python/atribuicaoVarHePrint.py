
# Atribuição de Variáveis
print("Atribuição de Variáveis")
a=1
b=2
c=3

d= a+b+c
print(d)
print(a)
print(b)
print(c)

# Cálculo de Vencimento Mensal
print("Cálculo de Vencimento Mensal")   

valorHora=4
dias= 30
horasTrabalho=8
vencimentoMensal= valorHora * horasTrabalho * dias
nome = "João"

print(nome)
print(vencimentoMensal)

nome = "João"

print(nome)
print(vencimentoMensal)
print("O funcionário", nome, "tem um vencimento mensal de R$", vencimentoMensal)    

# Exemplo de Print com Concatenação
print("Exemplo de Print com Concatenação")  

num1 = 10
num2 = 20

resultado = num1 + num2
print("Resultado " + str(resultado))
      

print (float(valorHora))
print (float(num2))

# Manipulação de Strings    
print("Manipulação de Strings")

nome = "João Silva "
print(nome)

print(nome[0:5])
print(nome[0:7])

print (nome+nome)
print (nome*3)

print ("t" in nome)
print("Silva" in nome)

# Listas em Python
print("Listas em Python")   

lista=[1, 4, 7, "udinei", 3.5 ,4, 20      ]
print(lista)

#lista.append adiciona um elemento na lista 
lista.append("novo valor")
print(lista)    


lista.append(99)
lista.append('joana')   
lista.append(True)
lista.append(False)
lista.append(None)

print(lista)

# lista.index retorna o índice da primeira ocorrência do valor passado como parametro   
print(lista.index("udinei"))
print(lista.count(lista))

lista.remove('udinei')
print(lista)    

# lista.count conta quantos elementos tem a lista com
#  o valor valor passado como parametro
print(lista.count(4))


# list.remove remove a primeira ocorrência do valor passado como parametro  
lista.remove(4)
print(lista)    

lista.remove(4)
print(lista)

lista2=[1, 4, 7, 2, 9, 8, 10,13,20,12,30]
print(lista2)

# lista2.sort() ordena a lista em ordem crescente
lista2.sort()
print(lista2)

#lista2.extend adiciona todos os elementos da lista passada como parametro
lista2.extend(lista)
print(lista2)


# Dicionários em Python
print("Dicionários em Python")  
telefones={"João Silva": 123456789, "Joana Silva": 987654321, "Maria Silva": 876543210}
print(telefones)

telefones['Udinei']=1234567890
print(telefones)

del telefones['Maria Silva']
print(telefones)

# tuplas em Python
print("tuplas em Python")

tuplas=("tiago", "silva", "joao")
# tuplas são imutáveis
print(tuplas[0])

# fatiamento de tuplas
print(tuplas[0:1])

# len() retorna o tamanho da tupla
print(len(tuplas))    

#  concatenação de tuplas
tuplas2=(1,2,3,4,5,6,7,8,9,10)
print(tuplas+tuplas)

# repetição de tuplas
tuplasx= tuplas*5
print(tuplasx)  

print('silva' in tuplas)

# conversão de listas em tuplas 
listaNum = [1.4, 10, "teste"]
print(listaNum)

tuplas2 = tuple(listaNum) 
print(tuplas2)

# Estruturas Condicionais em Python
print("Estruturas Condicionais em Python")

nome = "tiago"
numero = 1
if(numero == 1):
    print("Número é 1")


if(numero == 2):
    print("Número é 2")
else:
    print("Número é diferente de 2")
    


nome = "tiago"

if("x" in nome):
    print("Nome contém a letra t")  
elif("g" in nome):
    print("Nome contém a letra g")  
elif("a" in nome):
    print("Nome contém a letra a")
else:
    pass

print()

# Laços de Repetição em Python
print("Laços de Repetição em Python")   

# for loop  range
for x in range(0,5):
    print("valor de x e: ", x)

nome="tiago"   

#for loop  in   
for letra in nome:
    print("Letra: ", letra)

# for loop em listas
lista =["tiago", "silva", "joao"]
for valor in lista:
    print("Nome: ", valor)

# while loop
contador = 5
while(contador > 0):
    print("Contador: ", contador)
    contador -=1

numero=20
while True:
    numero=numero-1
    print("Número: ", numero)
    if(numero ==2):
        break


numero2=10
while True:
    numero2=numero2-1
    
    if(numero2 == 4):
       print("Número x: ", numero2)
       continue
    if(numero2 == 2):
       break   