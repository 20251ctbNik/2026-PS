import java.util.ArrayList;

public class AtividadeIntegradora {

    public static void main(String[] args) {
        // Teste dos Exercícios 1, 2, 5 e Desafio
        double[] notasTurma = {7.0, 5.0, 9.0, 6.0};
        System.out.println("--- 📊 BOLETIM DA TURMA ---");
        exibirBoletim(notasTurma);
        
        System.out.println("\n--- 🧩 TESTE DO EXERCÍCIO 4 (SOBRECARGA) ---");
        System.out.println("Maior entre 12 e 7: " + maiorValor(12, 7));
        System.out.println("Maior no array {3, 9, 5}: " + maiorValor(new int[]{3, 9, 5}));

        System.out.println("\n--- 🛒 TESTE DO EXERCÍCIO 3 (ARRAYLIST) ---");
        ArrayList<String> catalogo = new ArrayList<>();
        adicionarProduto(catalogo, "Pizza");
        adicionarProduto(catalogo, "Suco");
        listarProdutos(catalogo);
    }

    // 🧩 Exercício 1 — Média da Turma
    static double calcularMedia(double[] notas) {
        double soma = 0.0;
        for (double nota : notas) {
            soma += nota;
        }
        return soma / notas.length;
    }

    // 🧩 Exercício 2 — Contador de Aprovados
    static int contarAprovados(double[] notas) {
        int aprovados = 0;
        for (double nota : notas) {
            if (nota >= 6.0) {
                aprovados++;
            }
        }
        return aprovados;
    }

    // 🧩 Exercício 3 — Catálogo de Produtos (Adicionar)
    static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    // 🧩 Exercício 3 — Catálogo de Produtos (Listar)
    static void listarProdutos(ArrayList<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println((i + 1) + " - " + lista.get(i));
        }
    }

    // 🧩 Exercício 4 — Maior Valor (Dois números)
    static int maiorValor(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }

    // 🧩 Exercício 4 — Maior Valor (Array)
    static int maiorValor(int[] valores) {
        int maior = valores[0]; 
        for (int valor : valores) {
            if (valor > maior) {
                maior = valor;
            }
        }
        return maior;
    }

    // ⭐ Desafio Nível A — Contador Acima da Média
    static int contarAcimaDaMedia(double[] notas) {
        double media = calcularMedia(notas); // Reaproveita o Ex 1
        int acima = 0;
        for (double nota : notas) {
            if (nota > media) {
                acima++;
            }
        }
        return acima;
    }

    // 🧩 Exercício 5 — Boletim Integrador
    static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);     // Reaproveita o Ex 1
        int aprovados = contarAprovados(notas); // Reaproveita o Ex 2
        int acimaDaMedia = contarAcimaDaMedia(notas); // Reaproveita o Desafio

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);
        System.out.println("Acima da Média: " + acimaDaMedia);
        
        if (media >= 6.0) {
            System.out.println("Situação: APROVADA");
        } else {
            System.out.println("Situação: EM RECUPERAÇÃO");
        }
    }
}