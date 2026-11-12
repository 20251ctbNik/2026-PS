import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class LivroDAO {

    // Sobrecarga mantida para compatibilidade com chamadas antigas (sem capa)
    public boolean adicionarLivro(String titulo, String autor, int ano) {
        return adicionarLivro(titulo, autor, ano, null);
    }

    // Novo método com suporte à capa
    public boolean adicionarLivro(String titulo, String autor, int ano, String capa) {
        String sql = "INSERT INTO livros (titulo, autor, ano, capa) VALUES (?, ?, ?, ?)";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, titulo);
            comando.setString(2, autor);
            comando.setInt(3, ano);
            comando.setString(4, capa);

            int linhas = comando.executeUpdate();
            return linhas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao adicionar livro: " + e.getMessage());
            return false;
        }
    }

    // Sobrecarga mantida para compatibilidade com chamadas antigas (sem capa)
    public boolean atualizarLivro(int id, String titulo, String autor, int ano) {
        return atualizarLivro(id, titulo, autor, ano, null);
    }

    // Novo método com suporte à capa
    public boolean atualizarLivro(int id, String titulo, String autor, int ano, String capa) {
        String sql = "UPDATE livros SET titulo = ?, autor = ?, ano = ?, capa = ? WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setString(1, titulo);
            comando.setString(2, autor);
            comando.setInt(3, ano);
            comando.setString(4, capa);
            comando.setInt(5, id);

            int linhas = comando.executeUpdate();
            return linhas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao atualizar livro: " + e.getMessage());
            return false;
        }
    }

    public boolean excluirLivro(int id) {
        String sql = "DELETE FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);
            int linhas = comando.executeUpdate();
            return linhas > 0;

        } catch (SQLException e) {
            System.out.println("Erro ao excluir livro: " + e.getMessage());
            return false;
        }
    }

    public List<Livro> listarLivros() {
        List<Livro> livros = new ArrayList<>();
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros ORDER BY titulo";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql);
             ResultSet resultado = comando.executeQuery()) {

            while (resultado.next()) {
                int id = resultado.getInt("id");
                String titulo = resultado.getString("titulo");
                String autor = resultado.getString("autor");
                int ano = resultado.getInt("ano");
                String capa = resultado.getString("capa");

                livros.add(new Livro(id, titulo, autor, ano, capa));
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar livros: " + e.getMessage());
        }

        return livros;
    }

    public Livro buscarLivroPorId(int id) {
        String sql = "SELECT id, titulo, autor, ano, capa FROM livros WHERE id = ?";

        try (Connection conexao = Conexao.conectar();
             PreparedStatement comando = conexao.prepareStatement(sql)) {

            comando.setInt(1, id);

            try (ResultSet resultado = comando.executeQuery()) {
                if (resultado.next()) {
                    String titulo = resultado.getString("titulo");
                    String autor = resultado.getString("autor");
                    int ano = resultado.getInt("ano");
                    String capa = resultado.getString("capa");

                    return new Livro(id, titulo, autor, ano, capa);
                }
            }

        } catch (SQLException e) {
            System.out.println("Erro ao buscar livro por ID: " + e.getMessage());
        }

        return null;
    }
}