import java.awt.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class TelaBiblioteca extends JFrame {
    private Biblioteca biblioteca;
    private JTextField campoTitulo;
    private JTextField campoMatricula;
    private JTextArea areaAcervo;

    private static final Color COR_PRIMARIA = new Color(30, 58, 95);
    private static final Color COR_FUNDO = new Color(244, 246, 249);
    private static final Font FONTE_PADRAO = new Font("Segoe UI", Font.PLAIN, 13);
    private static final Font FONTE_NEGRITO = new Font("Segoe UI", Font.BOLD, 13);

    public TelaBiblioteca(Biblioteca biblioteca) {
        this.biblioteca = biblioteca;

        setTitle("BiblioTech — Controle de Empréstimos");
        setSize(780, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel painelRaiz = new JPanel(new BorderLayout(12, 12));
        painelRaiz.setBackground(COR_FUNDO);
        painelRaiz.setBorder(new EmptyBorder(12, 14, 12, 14));
        setContentPane(painelRaiz);

        // Cabeçalho visual
        JPanel topo = new JPanel(new BorderLayout(8, 8));
        topo.setOpaque(false);

        JLabel banner = new JLabel("  BiblioTech — Sistema de Biblioteca", SwingConstants.LEFT);
        banner.setOpaque(true);
        banner.setBackground(COR_PRIMARIA);
        banner.setForeground(Color.WHITE);
        banner.setFont(new Font("Segoe UI", Font.BOLD, 16));
        banner.setPreferredSize(new Dimension(0, 40));

        // Painel dos campos de entrada
        JPanel campos = new JPanel(new GridLayout(2, 2, 10, 10));
        campos.setBackground(Color.WHITE);
        campos.setBorder(BorderFactory.createCompoundBorder(
            BorderFactory.createLineBorder(new Color(210, 218, 226)),
            new EmptyBorder(12, 12, 12, 12)
        ));

        campoTitulo = new JTextField();
        campoTitulo.setFont(FONTE_PADRAO);
        campoMatricula = new JTextField();
        campoMatricula.setFont(FONTE_PADRAO);

        JLabel lblTitulo = new JLabel("Título do livro:");
        lblTitulo.setFont(FONTE_NEGRITO);
        JLabel lblMatricula = new JLabel("Matrícula do leitor:");
        lblMatricula.setFont(FONTE_NEGRITO);

        campos.add(lblTitulo);
        campos.add(campoTitulo);
        campos.add(lblMatricula);
        campos.add(campoMatricula);

        topo.add(banner, BorderLayout.NORTH);
        topo.add(campos, BorderLayout.CENTER);
        painelRaiz.add(topo, BorderLayout.NORTH);

        // Área central para visualização do acervo
        areaAcervo = new JTextArea();
        areaAcervo.setEditable(false);
        areaAcervo.setLineWrap(true);
        areaAcervo.setWrapStyleWord(true);
        areaAcervo.setFont(new Font("Consolas", Font.PLAIN, 13));
        areaAcervo.setBorder(new EmptyBorder(10, 10, 10, 10));

        JScrollPane scroll = new JScrollPane(areaAcervo);
        scroll.setBorder(BorderFactory.createLineBorder(new Color(205, 213, 222)));
        painelRaiz.add(scroll, BorderLayout.CENTER);

        // Painel inferior com os botões estilizados
        JPanel botoes = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 4));
        botoes.setOpaque(false);

        JButton botaoEmprestar = criarBotao("Emprestar", new Color(39, 135, 84));
        JButton botaoDevolver = criarBotao("Devolver", new Color(192, 86, 33));
        JButton botaoAtualizar = criarBotao("Atualizar acervo", new Color(52, 110, 168));
        JButton botaoAbrirLivros = criarBotao("Consulta e Capas (Banco)", COR_PRIMARIA);

        botaoEmprestar.addActionListener(e -> emprestar());
        botaoDevolver.addActionListener(e -> devolver());
        botaoAtualizar.addActionListener(e -> atualizarAcervo());
        botaoAbrirLivros.addActionListener(e -> new TelaLivros().setVisible(true));

        botoes.add(botaoEmprestar);
        botoes.add(botaoDevolver);
        botoes.add(botaoAtualizar);
        botoes.add(botaoAbrirLivros);
        painelRaiz.add(botoes, BorderLayout.SOUTH);

        atualizarAcervo();
    }

    private JButton criarBotao(String texto, Color corFundo) {
        JButton btn = new JButton(texto);
        btn.setFont(FONTE_NEGRITO);
        btn.setBackground(corFundo);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setCursor(new Cursor(Cursor.HAND_CURSOR));
        return btn;
    }

    private void atualizarAcervo() {
        areaAcervo.setText(biblioteca.obterAcervoComoTexto());
        areaAcervo.setCaretPosition(0);
    }

    private void emprestar() {
        String titulo = campoTitulo.getText().trim();
        String matricula = campoMatricula.getText().trim();

        if (titulo.isEmpty() || matricula.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Preencha o título e a matrícula.");
            return;
        }

        boolean resultado = biblioteca.emprestar(titulo, matricula);
        atualizarAcervo();

        if (resultado) {
            JOptionPane.showMessageDialog(this, "Empréstimo realizado.");
        } else {
            JOptionPane.showMessageDialog(
                this,
                "Empréstimo recusado. Confira o título, a matrícula, a disponibilidade e o limite do leitor."
            );
        }
    }

    private void devolver() {
        String titulo = campoTitulo.getText().trim();

        if (titulo.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Preencha o título do livro.");
            return;
        }

        boolean resultado = biblioteca.devolver(titulo);
        atualizarAcervo();

        if (resultado) {
            JOptionPane.showMessageDialog(this, "Devolução registrada.");
        } else {
            JOptionPane.showMessageDialog(this, "Nenhum empréstimo ativo encontrado para esse título.");
        }
    }

    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(new Livro("Dom Casmurro", "Machado de Assis", 1899));
        biblioteca.cadastrarLivro(new Livro("Capitães da Areia", "Jorge Amado", 1937));
        biblioteca.cadastrarLeitor(new Leitor("Pedro Alves", "2026010", 1));
        biblioteca.cadastrarLeitor(new Leitor("Ana Lima", "2026011", 2));

        SwingUtilities.invokeLater(() -> new TelaBiblioteca(biblioteca).setVisible(true));
    }
}