import java.util.Random;
import java.util.Scanner;

public class Sanduruba {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random random = new Random();

        String[] nomes = {"X-Burguer", "Pizza", "Batata Frita", "Refrigerante", "Sorvete"};
        double[] precos = {18.0, 30.0, 10.0, 8.0, 12.0};
        int[] qtd = new int[5];

        boolean comprando = true;

        while (comprando) {

            System.out.println("\n====== SANDURUBA ======");
            for (int i = 0; i < nomes.length; i++) {
                System.out.printf("%d - %s\n", i + 1, nomes[i]);
            }
            System.out.println("6 - Finalizar Pedido");

            System.out.print("\nEscolha: ");
            int opcao = entrada.nextInt();

            if (opcao >= 1 && opcao <= 5) {

                int i = opcao - 1;

                System.out.print("Quantidade: ");
                int quantidade = entrada.nextInt();

                if (quantidade > 0) {
                    qtd[i] += quantidade;
                    System.out.println("Item adicionado!");
                }

                System.out.println("\n1 - Continuar  |  2 - Finalizar");
                if (entrada.nextInt() == 2) comprando = false;

            } else if (opcao == 6) {
                comprando = false;
            } else {
                System.out.println("Opção inválida.");
            }
        }

        double total = 0;

        System.out.println("\n===== RESUMO =====");

        for (int i = 0; i < nomes.length; i++) {
            if (qtd[i] > 0) {
                double subtotal = qtd[i] * precos[i];
                total += subtotal;
                System.out.printf("%dx %s = R$ %.2f\n", qtd[i], nomes[i], subtotal);
            }
        }

        System.out.printf("\nTOTAL: R$ %.2f\n", total);

        System.out.println("\nPagamento: 1-Dinheiro 2-Cartão 3-PIX");
        int pag = entrada.nextInt();

        switch (pag) {
            case 1 -> System.out.println("Pago em dinheiro!");
            case 2 -> System.out.println("Pago no cartão!");
            case 3 -> System.out.println("Pago via PIX!");
            default -> System.out.println("Pagamento inválido!");
        }

        int pedido = random.nextInt(900) + 100;

        System.out.println("\nPedido Nº " + pedido);
        System.out.println("Aguarde a chamada.");

        entrada.close();
    }
}