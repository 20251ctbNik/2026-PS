public class TesteLivroDAO {

    public static void main(String[] args) {
        LivroDAO dao = new LivroDAO();

        System.out.println("=== ETAPA 3: Atualização ===");
        boolean atualizou = dao.atualizarLivro(
            2, 
            "O Hobbit - Edição Ilustrada", 
            "J.R.R. Tolkien", 
            1937
        );
        System.out.println("Livro 2 atualizado: " + atualizou);

        System.out.println("\n=== ETAPA 4: Exclusão ===");
        boolean excluiu = dao.excluirLivro(3);
        System.out.println("Livro 3 excluído: " + excluiu);

        System.out.println("\n=== TESTE ADICIONAL: Registro Inexistente ===");
        boolean atualizouInexistente = dao.atualizarLivro(
            999999,
            "Livro Inexistente",
            "Autor Desconhecido",
            2026
        );
        boolean excluiuInexistente = dao.excluirLivro(999999);

        System.out.println("Atualização inexistente: " + atualizouInexistente);
        System.out.println("Exclusão inexistente: " + excluiuInexistente);
    }
}