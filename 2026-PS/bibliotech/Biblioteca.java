import java.util.ArrayList;
import java.util.List;

public class Biblioteca {

    // O 0..* do diagrama: cada lista guarda muitas referencias.
    private List<Livro> livros;
    private List<Leitor> leitores;
    private List<Emprestimo> emprestimos;

    public Biblioteca() {
        this.livros = new ArrayList<>();
        this.leitores = new ArrayList<>();
        this.emprestimos = new ArrayList<>();
    }

    public void cadastrarLivro(Livro livro) {
        if (livro != null) {
            livros.add(livro);
        }
    }

    public void cadastrarLeitor(Leitor leitor) {
        if (leitor != null) {
            leitores.add(leitor);
        }
    }

    public void listarAcervo() {
        for (Livro livro : livros) {
            System.out.println(livro);
        }
    }

    // Devolve o livro achado, ou null se o titulo nao esta no acervo.
    public Livro buscarLivro(String titulo) {
        if (titulo == null) return null;

        for (Livro l : livros) {
            if (l.getTitulo() != null && l.getTitulo().equalsIgnoreCase(titulo)) {
                return l;
            }
        }
        return null;
    }

    // Devolve o leitor achado, ou null se a matricula nao esta cadastrada.
    public Leitor buscarLeitor(String matricula) {
        if (matricula == null) return null;

        for (Leitor l : leitores) {
            if (l.getMatricula() != null && l.getMatricula().equals(matricula)) {
                return l;
            }
        }
        return null;
    }

    // Acha os dois pelo texto, cria o registro e so arquiva se deu certo.
    public boolean emprestar(String titulo, String matricula) {
        Livro livro = buscarLivro(titulo);
        Leitor leitor = buscarLeitor(matricula);

        if (livro == null || leitor == null) {
            return false;
        }

        Emprestimo novo = new Emprestimo(livro, leitor);
        if (!novo.realizarEmprestimo()) {
            return false;
        }

        emprestimos.add(novo);
        return true;
    }

    // Procura o emprestimo ATIVO daquele titulo. O registro continua na lista
    public boolean devolver(String titulo) {
        if (titulo == null) return false;

        for (Emprestimo e : emprestimos) {
            if (e.estaAtivo() && e.getLivro() != null && e.getLivro().getTitulo() != null) {
                if (e.getLivro().getTitulo().equalsIgnoreCase(titulo)) {
                    return e.registrarDevolucao();
                }
            }
        }
        return false;
    }

    public void listarEmprestimos() {
        for (Emprestimo e : emprestimos) {
            System.out.println(e);
        }
    }

    // Fornece uma descricao do acervo para a interface.
    public String obterAcervoComoTexto() {
        if (livros.isEmpty()) {
            return "Nenhum livro cadastrado.";
        }

        StringBuilder sb = new StringBuilder();
        for (Livro l : livros) {
            sb.append(l).append("\n");
        }
        return sb.toString();
    }
}