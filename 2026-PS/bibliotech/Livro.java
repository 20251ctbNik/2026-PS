/*
 * Disciplina : 2026-PS
 * Projeto    : bibliotech
 * Arquivo    : Livro.java
 * Autor      : Nickolas Kinceski Martins
 */
public class Livro {

    private int id;
    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;
    private String capa;

    // Construtor com ID (para buscas e listagens do banco) - mantido para compatibilidade
    public Livro(int id, String titulo, String autor, int ano) {
        this(id, titulo, autor, ano, null);
    }

    // Construtor com ID e capa (para buscas e listagens do banco)
    public Livro(int id, String titulo, String autor, int ano, String capa) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
        this.capa = capa;
    }

    // Construtor sem ID (para novos cadastros sem capa) - mantido para compatibilidade
    public Livro(String titulo, String autor, int ano) {
        this(titulo, autor, ano, null);
    }

    // Construtor sem ID e com capa (para novos cadastros)
    public Livro(String titulo, String autor, int ano, String capa) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
        this.capa = capa;
    }

    // GETTERS & SETTERS
    public int getId() {
        return id;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
    }

    public String getCapa() {
        return capa;
    }

    public void setCapa(String capa) {
        this.capa = capa;
    }

    public boolean estaDisponivel() {
        return disponivel;
    }

    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }

    public void emprestar() {
        this.disponivel = false;
    }

    public void devolver() {
        this.disponivel = true;
    }

    @Override
    public String toString() {
        String situacao = disponivel ? "disponivel" : "emprestado";
        return id + " - " + titulo + " (" + autor + ", " + ano + ") - " + situacao;
    }
}