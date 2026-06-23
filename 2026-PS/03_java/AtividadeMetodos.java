import java.util.Scanner;

public class AtividadeMetodos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n--- 🛠️ MENU DE TESTES INTERATIVOS ---");
            System.out.println("1 - Problema 1: Calculadora de Desconto");
            System.out.println("2 - Problema 2: Verificador de Maior Valor");
            System.out.println("3 - Problema 3: Sistema de Frete");
            System.out.println("4 - Problema 4: Sobrecarga de Soma");
            System.out.println("5 - Problema 5: Sistema de Cardápio");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o valor do produto: ");
                    double valor = scanner.nextDouble();
                    System.out.print("Digite o percentual de desconto (ex: 10): ");
                    double desc = scanner.nextDouble();
                    System.out.println("-> Valor Final: " + calcularDesconto(valor, desc));
                    break;

                case 2:
                    System.out.print("Digite o primeiro número inteiro: ");
                    int n1 = scanner.nextInt();
                    System.out.print("Digite o segundo número inteiro: ");
                    int n2 = scanner.nextInt();
                    System.out.println("-> Maior número: " + maiorNumero(n1, n2));
                    break;

                case 3:
                    System.out.print("Digite o peso da carga (em kg): ");
                    double peso = scanner.nextDouble();
                    System.out.println("-> Valor do Frete: R$ " + calcularFrete(peso));
                    break;

                case 4:
                    System.out.println("Escolha o tipo de soma:");
                    System.out.println("1 - Números Inteiros (int)");
                    System.out.println("2 - Números Decimais (double)");
                    int tipoSoma = scanner.nextInt();
                    if (tipoSoma == 1) {
                        System.out.print("Digite o primeiro inteiro: ");
                        int a = scanner.nextInt();
                        System.out.print("Digite o segundo inteiro: ");
                        int b = scanner.nextInt();
                        System.out.println("-> Resultado (int): " + somar(a, b));
                    } else {
                        System.out.print("Digite o primeiro decimal: ");
                        double a = scanner.nextDouble();
                        System.out.print("Digite o segundo decimal: ");
                        double b = scanner.nextDouble();
                        System.out.println("-> Resultado (double): " + somar(a, b));
                    }
                    break;

                case 5:
                    System.out.println("Escolha como exibir o produto:");
                    System.out.println("1 - Apenas Nome");
                    System.out.println("2 - Nome e Preço");
                    int tipoCardapio = scanner.nextInt();
                    scanner.nextLine(); // Limpa o buffer do teclado

                    System.out.print("Digite o nome do produto: ");
                    String nome = scanner.nextLine();

                    if (tipoCardapio == 1) {
                        exibirProduto(nome);
                    } else {
                        System.out.print("Digite o preço do produto: ");
                        double preco = scanner.nextDouble();
                        exibirProduto(nome, preco);
                    }
                    break;

                case 0:
                    System.out.println("Saindo do programa... Até logo!");
                    break;

                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        } while (opcao != 0);

        scanner.close();
    }

    // --- MÉTODOS ESTÁTICOS SOLICITADOS (Mantêm a mesma estrutura) ---

    // 🧩 Problema 1
    public static double calcularDesconto(double valor, double percentual) {
        return valor - (valor * (percentual / 100));
    }

    // 🧩 Problema 2
    public static int maiorNumero(int a, int b) {
        return (a >= b) ? a : b;
    }

    // 🧩 Problema 3
    public static double calcularFrete(double peso) {
        if (peso <= 1) return 10.0;
        if (peso <= 5) return 20.0;
        return 35.0;
    }

    // 🧩 Problema 4 (Sobrecarga)
    public static int somar(int a, int b) {
        return a + b;
    }

    public static double somar(double a, double b) {
        return a + b;
    }

    // 🧩 Problema 5 (Sobrecarga)
    public static void exibirProduto(String nome) {
        System.out.println("Produto: " + nome);
    }

    public static void exibirProduto(String nome, double preco) {
        System.out.println("Produto: " + nome + "\nPreço: R$ " + preco);
    }
}