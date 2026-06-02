import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Bem-vindo ao Restaurante Essenza!");
        System.out.println("=====================================");
        System.out.println("        CARDÁPIO ELETRÔNICO");
        System.out.println("=====================================");
        System.out.println("1 - X-Burger ................ R$ 18,00");
        System.out.println("2 - Pizza ................... R$ 35,00");
        System.out.println("3 - Suco Natural ............ R$ 8,00");
        System.out.println("4 - Café .................... R$ 5,00");
        System.out.println("5 - Bolo de Chocolate ....... R$ 100,00");
        System.out.println("6 - Calcular o valor total do pedido");
        System.out.println("7 - Resumo do pedido");
        System.out.println("=====================================");

        int quantidadeX = 0;
        int quantidadePizza = 0;
        int quantidadeSuco = 0;
        int quantidadeCafe = 0;
        int quantidadeBolo = 0;

        double precoXBurger = 18.0;
        double precoPizza = 35.0;
        double precoSuco = 8.0;
        double precoCafe = 5.0;
        double precoBolo = 100.0;

        while (true) {
            System.out.println("=====================================");
            System.out.println("        CARDÁPIO ELETRÔNICO");
            System.out.println("=====================================");
            System.out.println("1 - X-Burger ................ R$ 18,00");
            System.out.println("2 - Pizza ................... R$ 35,00");
            System.out.println("3 - Suco Natural ............ R$ 8,00");
            System.out.println("4 - Café .................... R$ 5,00");
            System.out.println("5 - Bolo de Chocolate ....... R$ 100,00");
            System.out.println("6 - Calcular o valor total do pedido");
            System.out.println("7 - Resumo do pedido");
            System.out.println("=====================================");
            System.out.print("Escolha uma opção: ");
            int opcao = entrada.nextInt();

            if (opcao == 1) {
                System.out.print("Quantos X-Burgers você quer adicionar ao pedido? ");
                quantidadeX += entrada.nextInt();
                System.out.println("X-Burger adicionado ao pedido.");
            } else if (opcao == 2) {
                System.out.print("Quantas Pizzas você quer adicionar ao pedido? ");
                quantidadePizza += entrada.nextInt();
                System.out.println("Pizza adicionada ao pedido.");
            } else if (opcao == 3) {
                System.out.print("Quantos Sucos Naturais você quer adicionar ao pedido? ");
                quantidadeSuco += entrada.nextInt();
                System.out.println("Suco Natural adicionado ao pedido.");
            } else if (opcao == 4) {
                System.out.print("Quantos Cafés você quer adicionar ao pedido? ");
                quantidadeCafe += entrada.nextInt();
                System.out.println("Café adicionado ao pedido.");
            } else if (opcao == 5) {
                System.out.print("Quantos Bolos de Chocolate você quer adicionar ao pedido? ");
                quantidadeBolo += entrada.nextInt();
                System.out.println("Bolo de Chocolate adicionado ao pedido.");
            } else if (opcao == 6) {
                double total = quantidadeX * precoXBurger
                        + quantidadePizza * precoPizza
                        + quantidadeSuco * precoSuco
                        + quantidadeCafe * precoCafe
                        + quantidadeBolo * precoBolo;

                System.out.printf("Valor total do pedido: R$ %.2f\n", total);
                break;
            } else if (opcao == 7) {
                if (quantidadeX + quantidadePizza + quantidadeSuco + quantidadeCafe + quantidadeBolo == 0) {
                    System.out.println("Nenhum item foi adicionado ao pedido ainda.");
                } else {
                    System.out.println("Resumo do pedido:");
                    if (quantidadeX > 0) {
                        System.out.printf("- X-Burger: %d unidades (R$ %.2f)\n", quantidadeX, quantidadeX * precoXBurger);
                    }
                    if (quantidadePizza > 0) {
                        System.out.printf("- Pizza: %d unidades (R$ %.2f)\n", quantidadePizza, quantidadePizza * precoPizza);
                    }
                    if (quantidadeSuco > 0) {
                        System.out.printf("- Suco Natural: %d unidades (R$ %.2f)\n", quantidadeSuco, quantidadeSuco * precoSuco);
                    }
                    if (quantidadeCafe > 0) {
                        System.out.printf("- Café: %d unidades (R$ %.2f)\n", quantidadeCafe, quantidadeCafe * precoCafe);
                    }
                    if (quantidadeBolo > 0) {
                        System.out.printf("- Bolo de Chocolate: %d unidades (R$ %.2f)\n", quantidadeBolo, quantidadeBolo * precoBolo);
                    }
                    double total = quantidadeX * precoXBurger
                            + quantidadePizza * precoPizza
                            + quantidadeSuco * precoSuco
                            + quantidadeCafe * precoCafe
                            + quantidadeBolo * precoBolo;
                    System.out.printf("Valor total: R$ %.2f\n", total);
                }
                break;
            } else {
                System.out.println("Opção inválida. Tente novamente.");
            }
        }

        entrada.close();
    }
}