/**
 * Classe Main - SysControl v2.0
 * Instancia objetos Produto e executa os 5 casos de teste exigidos.
 *
 * Personalização exigida pelo enunciado:
 * - Dia de nascimento do estudante (11) usado como quantidade em estoque de p3.
 * - Duas primeiras letras do primeiro nome ("Ni") usadas no código de p3.
 */
public class Main {

    public static void main(String[] args) {

        System.out.println("===== TESTE 1: Criar objetos com dados válidos =====");
        Produto p1 = new Produto("Teclado Mecânico", "COD001", 250.00, 15);
        Produto p2 = new Produto("Mouse Gamer", "COD002", 120.50, 30);
        // Personalização: código usa as iniciais "Ni" e a quantidade usa o dia 11.
        Produto p3 = new Produto("Monitor 24 polegadas", "NI003", 899.90, 11);

        System.out.println(p1.resumo());
        System.out.println(p2.resumo());
        System.out.println(p3.resumo());

        System.out.println("\n===== TESTE 2: Atribuir texto vazio a campo obrigatório =====");
        try {
            Produto invalido = new Produto("", "COD004", 50.0, 5);
            System.out.println("Objeto criado indevidamente: " + invalido.resumo());
        } catch (IllegalArgumentException e) {
            System.out.println("Alteração recusada como esperado. Motivo: " + e.getMessage());
        }

        System.out.println("\n===== TESTE 3: Atribuir número negativo a campo numérico restrito =====");
        boolean resultadoPrecoInvalido = p1.setPreco(-50.0);
        System.out.println("Tentativa de preço negativo aceita? " + resultadoPrecoInvalido);
        System.out.println("Estado preservado -> " + p1.resumo());

        System.out.println("\n===== TESTE 4: Executar comportamento permitido =====");
        boolean vendaOk = p2.venderUnidades(10);
        System.out.println("Venda de 10 unidades realizada? " + vendaOk);
        System.out.println("Estado atualizado -> " + p2.resumo());

        System.out.println("\n===== TESTE 5: Executar comportamento impossível =====");
        boolean vendaImpossivel = p3.venderUnidades(500); // maior que o estoque (11)
        System.out.println("Venda de 500 unidades realizada? " + vendaImpossivel);
        System.out.println("Estado preservado -> " + p3.resumo());

        System.out.println("\n===== DEMONSTRAÇÃO EXTRA: alteração válida com desconto =====");
        boolean descontoOk = p1.aplicarDesconto(10); // 10% de desconto, válido
        System.out.println("Desconto de 10% aplicado? " + descontoOk);
        System.out.println("Estado atualizado -> " + p1.resumo());

        System.out.println("\n===== DESAFIO: comparação entre dois objetos =====");
        int comparacao = p1.compararPorPreco(p3);
        if (comparacao < 0) {
            System.out.println(p1.getNome() + " é mais barato que " + p3.getNome());
        } else if (comparacao > 0) {
            System.out.println(p1.getNome() + " é mais caro que " + p3.getNome());
        } else {
            System.out.println(p1.getNome() + " e " + p3.getNome() + " têm o mesmo preço");
        }

        System.out.println("\n===== ESTADO FINAL DE TODOS OS OBJETOS =====");
        System.out.println(p1.resumo());
        System.out.println(p2.resumo());
        System.out.println(p3.resumo());
    }
}