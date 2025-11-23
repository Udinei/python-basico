# Análise de Dados: Comparação de Sequências de RNA 🧬

Projeto educacional que demonstra conceitos básicos de Python através da análise e visualização de sequências genéticas (DNA/RNA).

## 📚 Sobre este Projeto

Este é um **projeto de aprendizado** desenvolvido como parte do curso:

### 🎓 Curso de Origem
**Visualização de Dados com Python**

- **Instrutor:** Diego Mariano, Ph.D.
- **Plataforma:** Udemy
- **Link do Curso:** https://www.udemy.com/course/visualizacao-de-dados-com-python/

Este projeto aplica os conceitos aprendidos no curso, focando em **análise de dados com Python Básico**.

---

## 📋 Descrição

Este é um **projeto de aprendizado** que utiliza **comandos básicos de Python** para:
- ✅ Carregar e processar arquivos FASTA (DNA/RNA)
- ✅ Contar frequência de dinucleotídeos (pares de bases)
- ✅ Gerar visualizações em HTML com gradiente de cores
- ✅ Comparar sequências de diferentes organismos (humano vs bactéria)

## 🎓 Objetivos Educacionais

Através deste projeto, você aprenderá:

### Conceitos Python Básicos
- ✅ **Variáveis e tipos de dados** — strings, listas, dicionários
- ✅ **Funções** — definição, parâmetros, retorno
- ✅ **Loops** — `for`, `while`, iteração
- ✅ **Condicionais** — `if/else`, lógica booleana
- ✅ **Manipulação de strings** — `.replace()`, `.strip()`, `.join()`, `.startswith()`
- ✅ **Estruturas de dados** — dicionários e operações
- ✅ **Leitura de arquivos** — `open()`, `with`, `.readlines()`
- ✅ **Processamento de texto** — parsing e normalização
- ✅ **List comprehensions** — sintaxe compacta
- ✅ **F-strings** — formatação de strings

### Análise de Dados
- 🧬 **Processamento de dados biológicos** — FASTA parsing
- 📊 **Contagem e frequência** — análise estatística básica
- 📈 **Visualização** — geração de gráficos em HTML/CSS
- 🔍 **Comparação** — análise entre conjuntos de dados

## 📁 Estrutura do Projeto

```
Python-Basico/
└── python-analise-dados/
    ├── python/
    │   ├── funcao-compara-rna.py          # Implementação principal
    │   ├── visualizacaoGraficos.py        # Exemplos de visualização
    │   ├── bacteria.html                  # Resultado: RNA bactéria
    │   └── human.html                     # Resultado: RNA humano
    ├── java/
    │   ├── FuncaoComparaRna.java          # Implementação em Java (comparação)
    │   ├── FuncaoComparaRna.class         # Compilado
    │   ├── bacteria.html
    │   └── human.html
    ├── groovy/
    │   ├── ComparandoRna.groovy           # Implementação em Groovy (comparação)
    │   ├── bacteria.html
    │   └── human.html
    └── dados/
        ├── bacteria.fasta                 # Sequência de bactéria
        └── human.fasta                    # Sequência humana
```

## 🚀 Como Usar

### Executar o Projeto

**1. Navegar até a pasta Python:**
```bash
cd python-analise-dados/python
```

**2. Executar o script:**
```bash
python funcao-compara-rna.py
```

**3. Resultado:**
- Arquivo `bacteria.html` gerado
- Arquivo `human.html` gerado
- Abra no navegador para visualizar os gráficos

### Estrutura do Código Python

```python
# 1. Carrega arquivo FASTA
sequencia = carregar_sequencia("caminho/arquivo.fasta")

# 2. Cria dicionário de dinucleotídeos
dicionario = criar_dicionario_dinucleotideos()

# 3. Conta frequências
dicionario = contar_dinucleotideos(sequencia, dicionario)

# 4. Gera visualização HTML
gerar_html(dicionario, "saida.html")
```

## 🔧 Funções e Comandos Básicos Utilizados

### 1. `carregar_sequencia(caminho_fasta)` — Leitura de Arquivo

**Comandos Python utilizados:**
```python
with open(caminho_fasta) as arquivo:    # Abre arquivo
    linhas = arquivo.readlines()         # Lê todas as linhas

sequencia = "".join(linha.strip()        # .strip() remove \n
                    for linha in linhas  # Loop com gerador
                    if not linha.startswith(">"))  # Filtra cabeçalhos
```

**Conceitos:**
- ✅ `with` — gerenciador de contexto
- ✅ `.readlines()` — lê linhas
- ✅ `.strip()` — remove espaços
- ✅ `.join()` — junta strings
- ✅ `.startswith()` — verifica início
- ✅ List comprehension com `if`

### 2. `criar_dicionario_dinucleotideos()` — Estrutura de Dados

**Comandos Python utilizados:**
```python
dicionario = {}                    # Cria dicionário vazio
for i in nucleotideos:            # Loop externo
    for j in nucleotideos:        # Loop aninhado
        dicionario[i + j] = 0     # Adiciona chave-valor
```

**Conceitos:**
- ✅ Dicionários — criação e inserção
- ✅ Loops aninhados
- ✅ String concatenation (`i + j`)

### 3. `contar_dinucleotideos(sequencia, dicionario)` — Contagem e Lógica

**Comandos Python utilizados:**
```python
for k in range(len(sequencia) - 1):           # Loop com índice
    par = sequencia[k] + sequencia[k + 1]     # Acesso a índices
    if par in dicionario:                     # Verifica existência
        dicionario[par] += 1                  # Incrementa
```

**Conceitos:**
- ✅ `range()` — iteração com índices
- ✅ `len()` — comprimento
- ✅ Slicing de strings
- ✅ `in` — verificação de chave
- ✅ Operador `+=` — incremento

### 4. `gerar_html(contagem, arquivo_saida)` — Escrita de Arquivo

**Comandos Python utilizados:**
```python
with open(arquivo_saida, "w") as saida:  # Abre para escrita
    saida.write("<html><body>\n")        # Escreve string
    
    for dinucleotideo, valor in contagem.items():  # Loop em dict
        transparencia = valor / max_valor if max_valor > 0 else 0
        
        saida.write(
            f"<div>...</div>\n"  # F-string com formatação
        )
```

**Conceitos:**
- ✅ Abre arquivo para escrita (`"w"`)
- ✅ `.write()` — escreve conteúdo
- ✅ `.items()` — itera sobre chave-valor
- ✅ Operador ternário — `if/else` em linha
- ✅ F-strings — `f"...{variavel}..."`
- ✅ Divisão e validação

### 5. `analisar_rna(caminho_fasta, arquivo_saida)` — Orquestração

**Conceitos:**
- ✅ Função com múltiplos parâmetros
- ✅ Chamadas de funções
- ✅ `print()` — saída para usuário
- ✅ Fluxo de programa

## 📊 Exemplo de Saída

### Entrada (arquivo FASTA):
```
>bacteria_DNA_sequence
ATCGATCGATCGATCG
ATCGATCGATCGATCG
```

### Processamento:
```
Carregando sequência...
Criando dicionário...
Dicionário inicial: {AA: 0, AT: 0, AC: 0, ...}

Contando dinucleotídeos...
Contagem final: {AA: 150, AT: 95, AC: 97, ...}

Gerando HTML...
```

### Saída (HTML visualizado no navegador):
```
Blocos coloridos azuis em gradiente:
- Dinucleotídeos muito frequentes: 🟦 Azul escuro
- Dinucleotídeos pouco frequentes: 🟦 Azul claro
```

## 📚 Comandos Python Principais

| Comando | O que faz | Exemplo |
|---------|-----------|---------|
| `open()` | Abre arquivo | `open("arquivo.txt")` |
| `.readlines()` | Lê linhas | `arquivo.readlines()` |
| `.strip()` | Remove espaços | `"  texto  ".strip()` |
| `.replace()` | Substitui texto | `"ola".replace("a", "e")` |
| `.join()` | Junta strings | `",".join(["a","b"])` |
| `.startswith()` | Verifica início | `"abc".startswith("a")` |
| `range()` | Cria sequência | `range(10)` |
| `len()` | Comprimento | `len("texto")` |
| `dict` | Dicionário | `{"chave": "valor"}` |
| `.items()` | Chave-valor | `dict.items()` |
| `for` | Loop | `for x in lista:` |
| `if/else` | Condicional | `if x > 0: ... else: ...` |
| `f-string` | Formatação | `f"valor: {x}"` |
| `+=` | Incremento | `x += 1` |

## 🔍 O que você aprende ao estudar este código

### Nível Iniciante ✅
- Como ler e processar arquivos
- Estruturas de dados (listas, dicionários)
- Loops e condicionais
- Funções básicas

### Nível Intermediário 🟡
- Gerenciamento de contexto (`with`)
- List comprehensions
- Manipulação de strings avançada
- Lógica de negócio (processamento de dados)

### Nível Avançado 🟣
- Conceitos bioinformáticos
- Análise e visualização de dados
- Design de funções reutilizáveis
- Tratamento de erros

## 📝 Formato do Arquivo FASTA

```
>ID_da_sequencia | descrição
ATCGATCGATCGATCGATCG
ATCGATCGATCGATCGATCG
>Outra_sequencia
GCTAGCTAGCTAGCTAGCTA
```

**Características:**
- Linhas com `>` são cabeçalhos
- Linhas seguintes contêm a sequência
- Múltiplas sequências em um arquivo

## 🧪 Exercícios Práticos

### 1. Modificar o código
```python
# Tente contar trinucleotídeos (3 bases) em vez de dinucleotídeos
# Dica: troque `range(len(sequencia) - 1)` por `range(len(sequencia) - 2)`
# E `sequencia[k] + sequencia[k + 1]` por `sequencia[k:k+3]`
```

### 2. Adicionar novos organismos
```python
# Crie seu próprio arquivo FASTA
# Coloque em `dados/meu_organismo.fasta`
# Execute: analisar_rna("../dados/meu_organismo.fasta", "resultado.html")
```

### 3. Comparar resultados
```python
# Execute para bactéria e humano
# Compare os gráficos gerados (bacteria.html vs human.html)
# Qual tem mais AA? Qual tem mais GC?
```

## 🔗 Comparação com Outras Linguagens

Mesmo projeto implementado em **3 linguagens diferentes**:

| Linguagem | Arquivo | Tamanho | Complexidade |
|-----------|---------|---------|-------------|
| **Python** | `funcao-compara-rna.py` | ~65 linhas | ✅ Simples |
| **Java** | `FuncaoComparaRna.java` | ~95 linhas | ❌ Complexa |
| **Groovy** | `ComparandoRna.groovy` | ~75 linhas | 🟡 Média |

**Conclusão:** Python é mais conciso e legível para este tipo de análise!

## 📚 Tópicos Python Abordados

- [x] Variáveis e tipos
- [x] Strings
- [x] Listas
- [x] Dicionários
- [x] Loops
- [x] Condicionais
- [x] Funções
- [x] Manipulação de arquivos
- [x] List comprehensions
- [x] F-strings
- [x] Operadores
- [x] Lógica de programa

## ⚙️ Requisitos

- **Python 3.8+**
- Nenhuma biblioteca externa necessária (só Python puro!)

## 🚀 Próximos Passos

1. ✅ Execute o projeto atual
2. ✅ Estude o código linha por linha
3. ✅ Modifique o código (exercícios acima)
4. ✅ Crie suas próprias funções
5. ✅ Estude as versões em Java e Groovy
6. ✅ Volte ao curso para aprender tópicos avançados

## 📞 Recursos Úteis

- [Curso: Visualização de Dados com Python](https://www.udemy.com/course/visualizacao-de-dados-com-python/)
- [Python Documentação Oficial](https://docs.python.org/3/)
- [Bioinformática Básica](https://en.wikipedia.org/wiki/Bioinformatics)
- [Formato FASTA](https://en.wikipedia.org/wiki/FASTA_format)

---

## 👨‍🏫 Autor do Curso

**Diego Mariano, Ph.D.**

- Especialista em Visualização de Dados
- Instrutor no Udemy
- Autor do curso: [Visualização de Dados com Python](https://www.udemy.com/course/visualizacao-de-dados-com-python/)

---

**Projeto:** Python Básico - Análise de Dados  
**Curso:** Visualização de Dados com Python  
**Tópico:** Sequências Genéticas (DNA/RNA)  
**Nível:** Iniciante/Intermediário  
**Data:** Novembro 2025  
**Status:** ✅ Funcionando  
**Linguagens:** Python, Java, Groovy