/**
 * Classe Produto - SysControl v2.0
 * Representa um produto do sistema, com atributos privados,
 * validações de negócio e métodos de comportamento.
 */
public class Produto {

    // ===================== ATRIBUTOS PRIVADOS =====================
    private String nome;
    private String codigo;
    private double preco;
    private int quantidadeEstoque;

    // ===================== CONSTRUTOR COMPLETO =====================
    public Produto(String nome, String codigo, double preco, int quantidadeEstoque) {
        // Aplica as mesmas validações usadas nos setters,
        // para garantir que nenhum objeto nasça em estado inválido.
        if (!validarNome(nome)) {
            throw new IllegalArgumentException("Nome do produto não pode ser vazio.");
        }
        if (!validarCodigo(codigo)) {
            throw new IllegalArgumentException("Código do produto não pode ser vazio.");
        }
        if (!validarPreco(preco)) {
            throw new IllegalArgumentException("Preço não pode ser negativo.");
        }
        if (!validarQuantidade(quantidadeEstoque)) {
            throw new IllegalArgumentException("Quantidade em estoque não pode ser negativa.");
        }

        this.nome = nome;
        this.codigo = codigo;
        this.preco = preco;
        this.quantidadeEstoque = quantidadeEstoque;
    }

    // ============ CONSTRUTOR ALTERNATIVO (desafio complementar) ============
    // Cria um produto novo com estoque zerado, exigindo apenas nome, código e preço.
    public Produto(String nome, String codigo, double preco) {
        this(nome, codigo, preco, 0);
    }

    // ===================== VALIDAÇÕES (mínimo 3) =====================
    private boolean validarNome(String nome) {
        return nome != null && !nome.trim().isEmpty();
    }

    private boolean validarCodigo(String codigo) {
        return codigo != null && !codigo.trim().isEmpty();
    }

    private boolean validarPreco(double preco) {
        return preco >= 0;
    }

    private boolean validarQuantidade(int quantidade) {
        return quantidade >= 0;
    }

    // ===================== GETTERS =====================
    // Apenas para dados que realmente precisam ser consultados de fora.
    public String getNome() {
        return nome;
    }

    public String getCodigo() {
        return codigo;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuantidadeEstoque() {
        return quantidadeEstoque;
    }

    // ===================== SETTERS =====================
    // Só existem onde alteração direta faz sentido (nome e código, por exemplo,
    // não têm setter pois representam identidade do produto e não devem mudar livremente).

    /**
     * Altera o preço do produto, validando que não seja negativo.
     * @return true se a alteração foi aplicada, false se foi recusada.
     */
    public boolean setPreco(double novoPreco) {
        if (!validarPreco(novoPreco)) {
            return false;
        }
        this.preco = novoPreco;
        return true;
    }

    /**
     * Altera a quantidade em estoque diretamente, validando que não seja negativa.
     * @return true se a alteração foi aplicada, false se foi recusada.
     */
    public boolean setQuantidadeEstoque(int novaQuantidade) {
        if (!validarQuantidade(novaQuantidade)) {
            return false;
        }
        this.quantidadeEstoque = novaQuantidade;
        return true;
    }

    // ===================== MÉTODOS DE COMPORTAMENTO (mínimo 2) =====================

    /**
     * Vende uma quantidade de unidades do produto, reduzindo o estoque.
     * Operação impossível se não houver estoque suficiente.
     * @return true se a venda foi realizada, false se foi recusada (estoque insuficiente).
     */
    public boolean venderUnidades(int quantidade) {
        if (quantidade <= 0) {
            return false; // não faz sentido vender quantidade zero ou negativa
        }
        if (quantidade > this.quantidadeEstoque) {
            return false; // estoque insuficiente: operação impossível
        }
        this.quantidadeEstoque -= quantidade;
        return true;
    }

    /**
     * Aplica um desconto percentual ao preço do produto.
     * @param percentual valor entre 0 e 100.
     * @return true se o desconto foi aplicado, false se o percentual for inválido.
     */
    public boolean aplicarDesconto(double percentual) {
        if (percentual < 0 || percentual > 100) {
            return false;
        }
        this.preco = this.preco - (this.preco * (percentual / 100));
        return true;
    }

    // ===================== DESAFIOS COMPLEMENTARES =====================

    // Desafio 1: método que retorna um resumo textual do objeto.
    public String resumo() {
        return String.format(
            "Produto[codigo=%s, nome=%s, preco=R$ %.2f, estoque=%d un.]",
            codigo, nome, preco, quantidadeEstoque
        );
    }

    // Desafio 2: método que compara dois produtos da mesma classe pelo preço.
    // Retorna negativo se este produto é mais barato, positivo se mais caro, 0 se igual.
    public int compararPorPreco(Produto outro) {
        return Double.compare(this.preco, outro.preco);
    }
}