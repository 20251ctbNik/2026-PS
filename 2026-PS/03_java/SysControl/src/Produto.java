/**
 * Classe Produto - SysControl v2.0
 * Representa um produto do sistema, com atributos privados,
 * validações de negócio e métodos de comportamento.
 */
public class Produto {

    // ===================== ATRIBUTOS PRIVADOS =====================
    // Tudo privado porque ninguém de fora deveria poder mudar esses valores
    // sem passar pelas regras de validação. É basicamente o coração do encapsulamento aqui.
    private String nome;
    private String codigo;
    private double preco;
    private int quantidadeEstoque;

    // ===================== CONSTRUTOR COMPLETO =====================
    public Produto(String nome, String codigo, double preco, int quantidadeEstoque) {
        // Reaproveito as mesmas validações dos setters aqui no construtor,
        // porque não faz sentido um objeto "nascer" já em estado inválido.
        // Se algo estiver errado, prefiro estourar exceção logo de cara
        // (diferente dos setters, que só devolvem false — aqui na criação
        // não tem como "recusar silenciosamente", o objeto não pode nem existir).
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
    // Ideia: às vezes eu só quero cadastrar um produto novo que ainda nem
    // chegou no estoque. Em vez de obrigar a informar quantidade toda vez,
    // esse construtor assume estoque 0 e delega pro construtor completo
    // (assim as validações continuam valendo do mesmo jeito).
    public Produto(String nome, String codigo, double preco) {
        this(nome, codigo, preco, 0);
    }

    // ===================== VALIDAÇÕES (mínimo 3) =====================
    // São private porque são detalhe interno de implementação — quem usa
    // a classe não precisa (nem deveria) chamar isso diretamente.

    private boolean validarNome(String nome) {
        // Nome não pode ser nulo nem só espaços em branco disfarçados de texto
        return nome != null && !nome.trim().isEmpty();
    }

    private boolean validarCodigo(String codigo) {
        // Mesma lógica do nome: código é a "identidade" do produto, não pode vir vazio
        return codigo != null && !codigo.trim().isEmpty();
    }

    private boolean validarPreco(double preco) {
        // Preço negativo não existe no mundo real, então bloqueio aqui
        return preco >= 0;
    }

    private boolean validarQuantidade(int quantidade) {
        // Estoque negativo também não faz sentido nenhum
        return quantidade >= 0;
    }

    // ===================== GETTERS =====================
    // Só criei getter pros campos que realmente precisam ser consultados
    // de fora da classe (pra imprimir, comparar, etc).
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
    // Só tem setter pra preço e estoque, porque esses dois realmente mudam
    // com o tempo (promoção, entrada/saída de mercadoria). Nome e código eu
    // decidi não deixar mudar depois de criado — se mudar, na prática vira
    // outro produto, não faz sentido "editar" a identidade dele.

    /**
     * Altera o preço do produto, validando que não seja negativo.
     * @return true se a alteração foi aplicada, false se foi recusada.
     */
    public boolean setPreco(double novoPreco) {
        if (!validarPreco(novoPreco)) {
            return false; // recusa educadamente em vez de quebrar o programa
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
            return false; // vender 0 ou quantidade negativa não faz sentido nenhum
        }
        if (quantidade > this.quantidadeEstoque) {
            return false; // não posso vender mais do que eu tenho, óbvio
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
            return false; // desconto negativo ou acima de 100% não existe
        }
        this.preco = this.preco - (this.preco * (percentual / 100));
        return true;
    }

    // ===================== DESAFIOS COMPLEMENTARES =====================

    // Desafio 1: um jeito rápido de mostrar o estado do objeto inteiro
    // sem precisar ficar chamando getter por getter toda vez que eu quiser imprimir.
    public String resumo() {
        return String.format(
            "Produto[codigo=%s, nome=%s, preco=R$ %.2f, estoque=%d un.]",
            codigo, nome, preco, quantidadeEstoque
        );
    }

    // Desafio 2: comparo dois produtos pelo preço, pra poder responder
    // "qual é mais barato" sem precisar acessar o atributo preco direto de fora.
    // Retorna negativo se este produto é mais barato, positivo se mais caro, 0 se igual.
    public int compararPorPreco(Produto outro) {
        return Double.compare(this.preco, outro.preco);
    }
}