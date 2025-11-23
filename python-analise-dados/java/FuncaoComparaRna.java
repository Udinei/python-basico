import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class FuncaoComparaRna {

    private static final char[] NUCLEOTIDE = {'A','T','C','G'};

    // Carrega sequência do FASTA removendo cabeçalho e quebras de linha
    public static String carregarSequencia(String caminhoFasta) throws IOException {
        Path p = Paths.get(caminhoFasta);
        List<String> linhas = Files.readAllLines(p);
        StringBuilder sb = new StringBuilder();
        for (String linha : linhas) {
            if (!linha.startsWith(">")) {
                sb.append(linha.trim());
            }
        }
        return sb.toString().toUpperCase();
    }

    // Cria dicionário (Map) com todos os dinucleotídeos possíveis inicializados em 0
    public static Map<String,Integer> criarDicionarioDinucleotideos() {
        Map<String,Integer> cont = new LinkedHashMap<>();
        for (char a : NUCLEOTIDE) {
            for (char b : NUCLEOTIDE) {
                cont.put("" + a + b, 0);
            }
        }
        return cont;
    }

    // Conta dinucleotídeos na sequência (ignora pares não presentes no dicionário)
    public static void contarDinucleotideos(String sequencia, Map<String,Integer> cont) {
        int len = sequencia.length();
        for (int i = 0; i < len - 1; i++) {
            String par = sequencia.substring(i, i + 2);
            if (cont.containsKey(par)) {
                cont.put(par, cont.get(par) + 1);
            }
        }
    }

    
    // Gera arquivo HTML simples com blocos coloridos representando as contagens
    public static void gerarHtml(Map<String,Integer> contagem, String arquivoSaida) throws IOException {
        int maxVal = contagem.values().stream().mapToInt(Integer::intValue).max().orElse(1);
        Path out = Paths.get(arquivoSaida);
        try (PrintWriter pw = new PrintWriter(Files.newBufferedWriter(out))) {
            pw.println("<html><body>");
            int i = 1;
            for (Map.Entry<String,Integer> e : contagem.entrySet()) {
                double transparencia = (maxVal > 0) ? ((double) e.getValue() / maxVal) : 0.0;
                // Força ponto decimal usando Locale.US
                String alpha = String.format(Locale.US, "%.6f", transparencia);
                

                pw.println("<div style='width:100px; border:1px solid #111; height:100px; float:left; "
                        + "background-color:rgba(0, 0, 255, " + alpha + ")'>"
                        + e.getKey() + "-" + e.getValue() + "</div>");
                
                if (i % 4 == 0) {
                    pw.println("<div style='clear:both'></div>");
                }
                i++;
            }
            pw.println("</body></html>");
        }
    }


    // Função principal que orquestra a análise
    public static void analisarRna(String caminhoFasta, String arquivoSaida) {
        try {
            System.out.println("Carregando sequência de " + caminhoFasta + "...");
            String seq = carregarSequencia(caminhoFasta);

            System.out.println("Criando dicionário de dinucleotídeos...");
            Map<String,Integer> cont = criarDicionarioDinucleotideos();
            System.out.println("Dicionário inicial: " + cont);

            System.out.println("Contando dinucleotídeos...");
            contarDinucleotideos(seq, cont);
            System.out.println("Contagem final: " + cont);

            System.out.println("Gerando arquivo HTML: " + arquivoSaida + "...");
            gerarHtml(cont, arquivoSaida);
            System.out.println("✅ Análise concluída com sucesso!");
        } catch (IOException ex) {
            System.err.println("Erro: " + ex.getMessage());
        }
    }


    public static void main(String[] args) {
        // Exemplo de uso: se passar argumentos, usa-os; senão usa caminhos padrão
        if (args.length >= 2) {
            analisarRna(args[0], args[1]);
        } else {
            analisarRna("python-analise-dados/dados/bacteria.fasta", "bacteria.html");
            analisarRna("python-analise-dados/dados/human.fasta", "human.html");
        }
    }
}