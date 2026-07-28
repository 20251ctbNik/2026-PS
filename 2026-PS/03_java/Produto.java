public class Produto {

    private String nome;
    private String codigo;
    private double preco;
    private int quantidade;

    public Produto(String nome, String codigo, double preco, int quantidade) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("Nome não pode ser vazio");
        }
        if (codigo == null || codigo.trim().isEmpty()) {
            throw new IllegalArgumentException("Código não pode ser vazio");
        }
        if (preco < 0) {
            throw new IllegalArgumentException("Preço não pode ser negativo");
        }
        if (quantidade < 0) {
            throw new IllegalArgumentException("Quantidade não pode ser negativa");
        }

        this.nome = nome;
        this.codigo = codigo;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    public String getNome() {
        return nome;
    }

    public String getCodigo() {
        return codigo;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public boolean setPreco(double preco) {
        if (preco < 0) {
            return false;
        }
        this.preco = preco;
        return true;
    }

    public boolean venderUnidades(int unidades) {
        if (unidades <= 0 || unidades > quantidade) {
            return false;
        }
        quantidade -= unidades;
        return true;
    }

    public boolean aplicarDesconto(double percentual) {
        if (percentual < 0 || percentual > 100) {
            return false;
        }

        double novoPreco = this.preco * (1 - percentual / 100);
        if (novoPreco < 0) {
            return false;
        }

        this.preco = novoPreco;
        return true;
    }

    public int compararPorPreco(Produto outro) {
        return Double.compare(this.preco, outro.preco);
    }

    public String resumo() {
        return "Produto: " + nome
                + " | Código: " + codigo
                + " | Preço: R$ " + String.format("%.2f", preco)
                + " | Estoque: " + quantidade;
    }
}
