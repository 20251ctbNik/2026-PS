import java.time.Year;

public class ValidadorLivro {

    public static void validar(String titulo, String autor, int ano) throws LivroInvalidoException {
        if (titulo == null || titulo.isBlank()) {
            throw new LivroInvalidoException("O título é obrigatório.");
        }

        if (titulo.trim().length() < 3) {
            throw new LivroInvalidoException("O título deve ter pelo menos 3 caracteres.");
        }

        if (autor == null || autor.isBlank()) {
            throw new LivroInvalidoException("O autor é obrigatório.");
        }

        int anoAtual = Year.now().getValue();
        if (ano < 1450 || ano > anoAtual + 1) {
            throw new LivroInvalidoException("Informe um ano válido (entre 1450 e " + (anoAtual + 1) + ").");
        }
    }
}