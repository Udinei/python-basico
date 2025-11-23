// Comparando RNAs Humano e Bactéria 

class ComparandoRnaAnalyzer {
    static nucleotideos = ['A', 'T', 'C', 'G']

/**
 * Carrega sequência do arquivo FASTA, removendo cabeçalho e quebras de linha
 */
 def carregarSequencia(String caminhoFasta) {
    File arquivo = new File(caminhoFasta)
    String sequencia = arquivo.readLines()
        .findAll { !it.startsWith(">") }
        .join("")
    return sequencia.toUpperCase()
}

/**
 * Cria dicionário com todos os dinucleotídeos possíveis inicializados com 0
 */
 def criarDicionarioDinucleotideos() {
    Map<String, Integer> cont = [:]
    nucleotideos.each { i ->
        nucleotideos.each { j ->
            cont[i + j] = 0
        }
    }
    return cont
}

/**
 * Conta a frequência de dinucleotídeos na sequência
 */

 def contarDinucleotideos(String sequencia, Map<String, Integer> dicionario) {
    // Normaliza sequência: remove espaços, converte para maiúsculas, troca U por T e remove caracteres não ATCG
    if (sequencia == null) {
        println "Sequência é nula"
        return dicionario
    }
    sequencia = sequencia.trim().toUpperCase().replaceAll("U", "T").replaceAll("[^ATCG]", "")

    println "Analisando sequência: comprimento=${sequencia.length()} prefixo=${sequencia.length() > 50 ? sequencia.substring(0,50) : sequencia}"

    if (sequencia.length() < 2) {
        println "Sequência muito curta para contar dinucleotídeos."
        return dicionario
    }

    for (int k = 0; k < sequencia.length() - 1; k++) {
        String par = sequencia.substring(k, k + 2)
        if (dicionario.containsKey(par)) {
            dicionario[par] = dicionario[par] + 1
        }
    }

    println "Contagem parcial: ${dicionario}\n"
    return dicionario
}


/**
 * Gera arquivo HTML com gráfico visual dos dinucleotídeos
 */
def gerarHtml(Map<String, Integer> contagem, String arquivoSaida = "bacteria.html") {
    File saida = new File(arquivoSaida)
    int maxValor = contagem.values().max() ?: 1
    
    saida.withWriter { writer ->
        writer.writeLine "<html><body>"
        
        int i = 1
        contagem.each { dinucleotideo, valor ->
             double transparencia = (maxValor > 0) ? (valor / maxValor as double) : 0.0
             String alpha = String.format(Locale.US, "%.6f", transparencia);

            writer.writeLine(
                "<div style='width:100px; border:1px solid #111; height:100px; float:left; " +
                "background-color:rgba(0, 0, 255, ${alpha})'>" +
                "${dinucleotideo}</div>"
            )
            
            // A cada 4 divs, cria uma nova linha
            if (i % 4 == 0) {
                writer.writeLine "<div style='clear:both'></div>"
            }
            i++
        }
        
        writer.writeLine "</body></html>"
    }
}

/**
 * Função principal que orquestra toda a análise de RNA
 */
def analisarRna(String caminhoFasta, String arquivoSaida = "bacteria.html") {
    println "Carregando sequência de ${caminhoFasta}..."
    String sequencia = carregarSequencia(caminhoFasta)
    
    println "Criando dicionário de dinucleotídeos..."
    Map<String, Integer> cont = criarDicionarioDinucleotideos()
    println "Dicionário inicial: ${cont}\n"
    
    println "Contando dinucleotídeos..."
    cont = contarDinucleotideos(sequencia, cont)
    println "Contagem final: ${cont}\n"
    
    println "Gerando arquivo HTML: ${arquivoSaida}..."
    gerarHtml(cont, arquivoSaida)
    println "✅ Análise concluída com sucesso!"
}

}

// Execução principal
if (args.size() >= 2) {
    ComparandoRnaAnalyzer.analisarRna(args[0], args[1])
} else {
    ComparandoRnaAnalyzer.analisarRna("../dados/bacteria.fasta", "bacteria.html")
    ComparandoRnaAnalyzer.analisarRna("../dados/human.fasta", "human.html")
}