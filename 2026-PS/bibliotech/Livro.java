/*
 * Disciplina : 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Livro.java
 * Autor     : Nickolas Kinceski Martins
 */
public class Livro {

    private int id;
    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;

    // Construtor com ID (para buscas e listagens do banco)
    public Livro(int id, String titulo, String autor, int ano) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
    }

    // Construtor sem ID (para novos cadastros)
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
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