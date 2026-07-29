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
        // Três produtos "normais", só pra ter um cenário com estoque de verdade
        Produto p1 = new Produto("Teclado Mecânico", "COD001", 250.00, 15);
        Produto p2 = new Produto("Mouse Gamer", "COD002", 120.50, 30);
        // Esse aqui é o produto "personalizado": código com minhas iniciais (Ni)
        // e estoque com o dia do meu nascimento (11), como pedido no enunciado
        Produto p3 = new Produto("Monitor 24 polegadas", "NI003", 899.90, 11);

        System.out.println(p1.resumo());
        System.out.println(p2.resumo());
        System.out.println(p3.resumo());

        System.out.println("\n===== TESTE 2: Atribuir texto vazio a campo obrigatório =====");
        // Nome não tem setter (é identidade do produto), então testo a validação
        // direto no construtor mesmo. Se passar string vazia, tem que estourar exceção.
        try {
            Produto invalido = new Produto("", "COD004", 50.0, 5);
            System.out.println("Objeto criado indevidamente: " + invalido.resumo());
        } catch (IllegalArgumentException e) {
            System.out.println("Alteração recusada como esperado. Motivo: " + e.getMessage());
        }

        System.out.println("\n===== TESTE 3: Atribuir número negativo a campo numérico restrito =====");
        // TENTATIVA INVÁLIDA: tento colocar o preço do teclado como -50.
        // O setter tem que barrar isso e devolver false, sem mudar o preço.
        boolean resultadoPrecoInvalido = p1.setPreco(-50.0);
        System.out.println("Tentativa de preço negativo aceita? " + resultadoPrecoInvalido);
        System.out.println("Estado preservado -> " + p1.resumo());

        System.out.println("\n===== TESTE 4: Executar comportamento permitido =====");
        // Aqui é uma operação que dá pra fazer numa boa: vender 10 mouses,
        // tem estoque de sobra (30), então o estoque deve cair pra 20.
        boolean vendaOk = p2.venderUnidades(10);
        System.out.println("Venda de 10 unidades realizada? " + vendaOk);
        System.out.println("Estado atualizado -> " + p2.resumo());

        System.out.println("\n===== TESTE 5: Executar comportamento impossível =====");
        // TENTATIVA IMPOSSÍVEL: o monitor só tem 11 no estoque, então tentar
        // vender 500 tem que ser recusado e o estoque não pode mudar.
        boolean vendaImpossivel = p3.venderUnidades(500); // maior que o estoque (11)
        System.out.println("Venda de 500 unidades realizada? " + vendaImpossivel);
        System.out.println("Estado preservado -> " + p3.resumo());

        System.out.println("\n===== DEMONSTRAÇÃO EXTRA: alteração válida com desconto =====");
        // TENTATIVA VÁLIDA extra: 10% de desconto é um percentual permitido (0-100),
        // então o preço do teclado deve diminuir de verdade.
        boolean descontoOk = p1.aplicarDesconto(10); // 10% de desconto, válido
        System.out.println("Desconto de 10% aplicado? " + descontoOk);
        System.out.println("Estado atualizado -> " + p1.resumo());

        System.out.println("\n===== DESAFIO: comparação entre dois objetos =====");
        // Comparo o teclado (já com desconto) com o monitor, só pra mostrar
        // o método de comparação por preço funcionando na prática.
        int comparacao = p1.compararPorPreco(p3);
        if (comparacao < 0) {
            System.out.println(p1.getNome() + " é mais barato que " + p3.getNome());
        } else if (comparacao > 0) {
            System.out.println(p1.getNome() + " é mais caro que " + p3.getNome());
        } else {
            System.out.println(p1.getNome() + " e " + p3.getNome() + " têm o mesmo preço");
        }

        System.out.println("\n===== ESTADO FINAL DE TODOS OS OBJETOS =====");
        // Estado final sempre exibido via resumo(), nunca acessando atributo direto
        System.out.println(p1.resumo());
        System.out.println(p2.resumo());
        System.out.println(p3.resumo());
    }
}