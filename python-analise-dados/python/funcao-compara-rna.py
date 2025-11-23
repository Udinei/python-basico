# Comparando RNAs Humano e Bactéria 
import os
# lista para armazenar as letras dos nucleotídeos
nucleotideos=['A', 'T', 'C', 'G']

def carregar_sequencia(caminho_fasta):
    """Carrega sequência do arquivo FASTA, removendo cabeçalho e quebras de linha."""
    with open(caminho_fasta) as arquivo:
        linhas = arquivo.readlines()
    
    # linha.strip() remove espaços em branco nas extremidades
    sequencia = "".join(linha.strip() 
                        
    # Remove cabeçalho (linhas que começam com '>') e junta o restante                    
    for linha in linhas
      if not linha.startswith(">"))
    
    return sequencia.upper()


def criar_dicionario_dinucleotideos():
    """Cria dicionário com todos os dinucleotídeos possíveis inicializados com 0."""
    dicDinucleotideos = {}
    for i in nucleotideos:
        for j in nucleotideos:
            dicDinucleotideos[i + j] = 0
    return dicDinucleotideos


def contar_dinucleotideos(sequencia, dicionario):
    """Conta a frequência de dinucleotídeos na sequência."""
    for k in range(len(sequencia) - 1):
        par = sequencia[k] + sequencia[k + 1]
        if par in dicionario:
            dicionario[par] += 1
    return dicionario




def gerar_html(contagem, arquivo_saida="bacteria.html"):
    """Gera arquivo HTML com gráfico visual dos dinucleotídeos."""
    # Obtém o diretório do script atual
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_html = os.path.join(diretorio_script, arquivo_saida)
    
    with open(caminho_html, "w") as saida:
        saida.write("<html><body>\n")
        i = 1
        max_valor = max(contagem.values())
        
        for dinucleotideo, valor in contagem.items():
            # se max_valor for maior que 0, calcula transparência proporcional
            # se max_valor nao for maior que 0, transparência é = 0
            transparencia = valor / max_valor if max_valor > 0 else 0
            
            # cria a div com a cor azul e transparência proporcional
            # essa div usa a transparencia no canal alpha do RGBA
            saida.write(
                f"<div style='width:100px; border:1px solid #111; height:100px; float:left;"
                f" background-color:rgba(0, 0, 255, {transparencia})'>"
                f"{dinucleotideo}-{valor} </div>\n"
            )
            
            # A cada 4 divs, cria uma nova linha
            # i = contador de divs
            if i % 4 == 0:
                saida.write("<div style='clear:both'></div>\n")
            # incrementa o contador
            i += 1
        
        saida.write("</body></html>")
    
    print(f"✅ HTML salvo em: {caminho_html}")


# Função principal que orquestra toda a análise de RNA.
def analisar_rna(caminho_fasta, arquivo_saida="bacteria.html"):
    """Função principal que orquestra toda a análise de RNA."""
    print(f"Carregando sequência de {caminho_fasta}...")
    sequencia = carregar_sequencia(caminho_fasta)
    
    print("Criando dicionário de dinucleotídeos...")
    dic = criar_dicionario_dinucleotideos()
    print(f"Dicionário inicial: {dic}\n")
    
    print("Contando dinucleotídeos...")
    dic = contar_dinucleotideos(sequencia, dic)
    print(f"Contagem final: {dic}\n")
    
    print(f"Gerando arquivo HTML: {arquivo_saida}...")
    gerar_html(dic, arquivo_saida)
    print("✅ Análise concluída com sucesso!")


# Execução principal
if __name__ == "__main__":
    # Use assim:
    analisar_rna("python-analise-dados/dados/bacteria.fasta", "bacteria.html")
    analisar_rna("python-analise-dados/dados/human.fasta", "human.html")
    # Ou com outro arquivo:
    # from funcao-compara-rna import analisar_rna
    #analisar_rna("dados/humano.fasta")  # Você chama manualmente
    