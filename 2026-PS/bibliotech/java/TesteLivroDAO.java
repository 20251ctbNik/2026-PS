public class TesteLivroDAO {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        boolean resultado = dao.atualizarLivro(
            1,
            "Dom Casmurro - Edição Especial",
            "Machado de Assis",
            1899
        );

        System.out.println(
            "Livro atualizado: " + resultado
        );
    }

    public boolean excluirLivro(int id) {

    String sql =
        "DELETE FROM livros WHERE id = ?";

    try (Connection conexao = Conexao.conectar();
         PreparedStatement comando =
             conexao.prepareStatement(sql)) {

        comando.setInt(1, id);

        int linhas = comando.executeUpdate();

        return linhas > 0;

    } catch (SQLException e) {

        System.out.println(
            "Erro ao excluir livro: " +
            e.getMessage()
        );

        return false;
    }
}
}
