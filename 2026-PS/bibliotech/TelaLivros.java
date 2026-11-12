import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.border.TitledBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import java.awt.*;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    // Paleta de cores e fontes personalizadas
    private static final Color COR_PRIMARIA = new Color(30, 58, 95);     // Azul-marinho
    private static final Color COR_SECUNDARIA = new Color(52, 110, 168); // Azul destaque
    private static final Color COR_FUNDO = new Color(244, 246, 249);     // Cinza muito claro
    private static final Color COR_LINHA_ALT = new Color(235, 241, 248); // Zebra da tabela
    private static final Font FONTE_TITULO = new Font("Segoe UI", Font.BOLD, 15);
    private static final Font FONTE_PADRAO = new Font("Segoe UI", Font.PLAIN, 13);
    private static final Font FONTE_NEGRITO = new Font("Segoe UI", Font.BOLD, 13);

    private final DefaultTableModel modelo;
    private final JTable tabela;

    // Controles de busca
    private final JTextField campoId = new JTextField(6);
    private final JLabel status = new JLabel("Pronto.");

    // Controles de cadastro / seleção de capa
    private final JTextField campoTitulo = new JTextField(16);
    private final JTextField campoAutor = new JTextField(14);
    private final JTextField campoAno = new JTextField(5);
    private final JLabel lblPreviewCapa = new JLabel("Sem capa", SwingConstants.CENTER);
    private String caminhoCapaSelecionada = null;

    public TelaLivros() {
        setTitle("BiblioTech — Gestão e Consulta de Livros");
        setSize(980, 600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        JPanel painelPrincipal = new JPanel(new BorderLayout(12, 12));
        painelPrincipal.setBackground(COR_FUNDO);
        painelPrincipal.setBorder(new EmptyBorder(12, 14, 12, 14));
        setContentPane(painelPrincipal);

        // --- TOPO: Busca e Cadastro ---
        JPanel painelTopo = new JPanel(new BorderLayout(8, 8));
        painelTopo.setOpaque(false);

        // Barra de busca
        JPanel barraBusca = new JPanel(new FlowLayout(FlowLayout.LEFT, 8, 6));
        barraBusca.setBackground(Color.WHITE);
        barraBusca.setBorder(BorderFactory.createLineBorder(new Color(215, 222, 230)));

        JLabel lblBusca = new JLabel("ID do livro:");
        lblBusca.setFont(FONTE_NEGRITO);
        campoId.setFont(FONTE_PADRAO);

        JButton buscar = criarBotao("Buscar por ID", COR_SECUNDARIA);
        JButton limpar = criarBotao("Limpar", new Color(110, 120, 130));
        JButton atualizar = criarBotao("Atualizar listagem", COR_PRIMARIA);

        barraBusca.add(lblBusca);
        barraBusca.add(campoId);
        barraBusca.add(buscar);
        barraBusca.add(limpar);
        barraBusca.add(atualizar);

        // Painel de cadastro rápido com JFileChooser
        JPanel painelCadastro = new JPanel(new BorderLayout(10, 5));
        painelCadastro.setBackground(Color.WHITE);
        painelCadastro.setBorder(BorderFactory.createTitledBorder(
            BorderFactory.createLineBorder(new Color(200, 210, 222)),
            "Cadastrar Novo Livro / Associar Capa",
            TitledBorder.LEFT,
            TitledBorder.TOP,
            FONTE_TITULO,
            COR_PRIMARIA
        ));

        JPanel camposForm = new JPanel(new FlowLayout(FlowLayout.LEFT, 8, 10));
        camposForm.setOpaque(false);

        campoTitulo.setFont(FONTE_PADRAO);
        campoAutor.setFont(FONTE_PADRAO);
        campoAno.setFont(FONTE_PADRAO);

        JButton btnEscolherCapa = criarBotao("Selecionar Capa...", COR_SECUNDARIA);
        JButton btnSalvarLivro = criarBotao("Salvar Livro", new Color(39, 135, 84));
        JButton btnVincularCapa = criarBotao("Vincular Capa ao Selecionado", new Color(180, 110, 30));

        camposForm.add(criarLabel("Título:"));
        camposForm.add(campoTitulo);
        camposForm.add(criarLabel("Autor:"));
        camposForm.add(campoAutor);
        camposForm.add(criarLabel("Ano:"));
        camposForm.add(campoAno);
        camposForm.add(btnEscolherCapa);
        camposForm.add(btnSalvarLivro);
        camposForm.add(btnVincularCapa);

        // Miniatura de pré-visualização da capa
        lblPreviewCapa.setPreferredSize(new Dimension(65, 85));
        lblPreviewCapa.setFont(new Font("Segoe UI", Font.ITALIC, 11));
        lblPreviewCapa.setForeground(Color.GRAY);
        lblPreviewCapa.setBorder(BorderFactory.createLineBorder(new Color(190, 200, 210)));
        lblPreviewCapa.setOpaque(true);
        lblPreviewCapa.setBackground(COR_FUNDO);

        painelCadastro.add(camposForm, BorderLayout.CENTER);
        painelCadastro.add(lblPreviewCapa, BorderLayout.EAST);

        painelTopo.add(barraBusca, BorderLayout.NORTH);
        painelTopo.add(painelCadastro, BorderLayout.CENTER);
        painelPrincipal.add(painelTopo, BorderLayout.NORTH);

        // --- CENTRO: Modelo de Tabela Personalizado com Miniaturas ---
        modelo = new DefaultTableModel(
            new Object[]{"ID", "Capa", "Título", "Autor", "Ano"}, 0
        ) {
            @Override
            public Class<?> getColumnClass(int coluna) {
                if (coluna == 1) return ImageIcon.class;
                return super.getColumnClass(coluna);
            }

            @Override
            public boolean isCellEditable(int linha, int coluna) {
                return false;
            }
        };

        tabela = new JTable(modelo);
        estilizarTabela();

        JScrollPane scroll = new JScrollPane(tabela);
        scroll.setBorder(BorderFactory.createLineBorder(new Color(205, 213, 222)));
        painelPrincipal.add(scroll, BorderLayout.CENTER);

        // --- RODAPÉ: Barra de Status ---
        status.setFont(FONTE_NEGRITO);
        status.setForeground(COR_PRIMARIA);
        painelPrincipal.add(status, BorderLayout.SOUTH);

        // --- EVENTOS ---
        atualizar.addActionListener(e -> carregarLivros());
        buscar.addActionListener(e -> buscarLivro());
        campoId.addActionListener(e -> buscarLivro());
        limpar.addActionListener(e -> {
            campoId.setText("");
            carregarLivros();
        });

        btnEscolherCapa.addActionListener(e -> selecionarImagemCapa());
        btnSalvarLivro.addActionListener(e -> salvarNovoLivro());
        btnVincularCapa.addActionListener(e -> atualizarCapaLivroSelecionado());

        carregarLivros();
    }

    private void estilizarTabela() {
        tabela.setFont(FONTE_PADRAO);
        tabela.setRowHeight(74);
        tabela.setShowVerticalLines(false);
        tabela.setGridColor(new Color(225, 230, 236));
        tabela.setSelectionBackground(new Color(204, 224, 245));
        tabela.setSelectionForeground(Color.BLACK);

        // Larguras das colunas
        tabela.getColumnModel().getColumn(0).setMaxWidth(60);
        tabela.getColumnModel().getColumn(1).setPreferredWidth(80);
        tabela.getColumnModel().getColumn(1).setMaxWidth(90);
        tabela.getColumnModel().getColumn(4).setMaxWidth(80);

        // Cabeçalho estilizado
        JTableHeader cabecalho = tabela.getTableHeader();
        cabecalho.setBackground(COR_PRIMARIA);
        cabecalho.setForeground(Color.WHITE);
        cabecalho.setFont(FONTE_NEGRITO);
        cabecalho.setPreferredSize(new Dimension(cabecalho.getWidth(), 34));

        // Centralização e linhas zebradas para colunas de texto
        DefaultTableCellRenderer renderTexto = new DefaultTableCellRenderer() {
            @Override
            public Component getTableCellRendererComponent(JTable table, Object value,
                    boolean isSelected, boolean hasFocus, int row, int column) {
                Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                if (!isSelected) {
                    c.setBackground(row % 2 == 0 ? Color.WHITE : COR_LINHA_ALT);
                }
                setHorizontalAlignment(column == 0 || column == 4 ? SwingConstants.CENTER : SwingConstants.LEFT);
                setBorder(new EmptyBorder(0, 8, 0, 8));
                return c;
            }
        };

        tabela.getColumnModel().getColumn(0).setCellRenderer(renderTexto);
        tabela.getColumnModel().getColumn(2).setCellRenderer(renderTexto);
        tabela.getColumnModel().getColumn(3).setCellRenderer(renderTexto);
        tabela.getColumnModel().getColumn(4).setCellRenderer(renderTexto);
    }

    private void selecionarImagemCapa() {
        JFileChooser chooser = new JFileChooser(new File("imagens"));
        chooser.setDialogTitle("Selecionar capa do livro");
        chooser.setFileFilter(new FileNameExtensionFilter("Imagens (JPG, JPEG, PNG)", "jpg", "jpeg", "png"));

        int opcao = chooser.showOpenDialog(this);
        if (opcao == JFileChooser.APPROVE_OPTION) {
            File arquivoOrigem = chooser.getSelectedFile();
            try {
                File pastaDestino = new File("imagens/livros");
                if (!pastaDestino.exists()) {
                    pastaDestino.mkdirs();
                }

                String nomeArquivo = System.currentTimeMillis() + "_" + arquivoOrigem.getName().replaceAll("\\s+", "_");
                Path destino = Paths.get("imagens/livros", nomeArquivo);
                Files.copy(arquivoOrigem.toPath(), destino, StandardCopyOption.REPLACE_EXISTING);

                caminhoCapaSelecionada = "imagens/livros/" + nomeArquivo;

                ImageIcon preview = redimensionarImagem(caminhoCapaSelecionada, 55, 78);
                lblPreviewCapa.setIcon(preview);
                lblPreviewCapa.setText("");
                status.setText("Capa selecionada: " + caminhoCapaSelecionada);

            } catch (Exception ex) {
                JOptionPane.showMessageDialog(this, "Erro ao copiar imagem: " + ex.getMessage(),
                        "Erro", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    private void salvarNovoLivro() {
        String titulo = campoTitulo.getText().trim();
        String autor = campoAutor.getText().trim();
        String anoStr = campoAno.getText().trim();

        if (titulo.isEmpty() || autor.isEmpty() || anoStr.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Preencha título, autor e ano.");
            return;
        }

        int ano;
        try {
            ano = Integer.parseInt(anoStr);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Informe um ano válido.");
            return;
        }

        if (dao.adicionarLivro(titulo, autor, ano, caminhoCapaSelecionada)) {
            JOptionPane.showMessageDialog(this, "Livro cadastrado com sucesso!");
            limparFormularioCadastro();
            carregarLivros();
        } else {
            JOptionPane.showMessageDialog(this, "Erro ao salvar livro no banco.", "Erro", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void atualizarCapaLivroSelecionado() {
        int linha = tabela.getSelectedRow();
        if (linha == -1) {
            JOptionPane.showMessageDialog(this, "Selecione um livro na tabela primeiro.");
            return;
        }
        if (caminhoCapaSelecionada == null) {
            JOptionPane.showMessageDialog(this, "Clique em 'Selecionar Capa...' antes de vincular.");
            return;
        }

        int id = (int) modelo.getValueAt(linha, 0);
        String titulo = (String) modelo.getValueAt(linha, 2);
        String autor = (String) modelo.getValueAt(linha, 3);
        int ano = (int) modelo.getValueAt(linha, 4);

        if (dao.atualizarLivro(id, titulo, autor, ano, caminhoCapaSelecionada)) {
            JOptionPane.showMessageDialog(this, "Capa associada ao livro '" + titulo + "'!");
            limparFormularioCadastro();
            carregarLivros();
        }
    }

    private void limparFormularioCadastro() {
        campoTitulo.setText("");
        campoAutor.setText("");
        campoAno.setText("");
        caminhoCapaSelecionada = null;
        lblPreviewCapa.setIcon(null);
        lblPreviewCapa.setText("Sem capa");
    }

    private ImageIcon redimensionarImagem(String caminho, int largura, int altura) {
        if (caminho == null || caminho.isEmpty()) return null;
        File arquivo = new File(caminho);
        if (!arquivo.exists()) return null;

        ImageIcon original = new ImageIcon(caminho);
        Image redimensionada = original.getImage().getScaledInstance(largura, altura, Image.SCALE_SMOOTH);
        return new ImageIcon(redimensionada);
    }

    private void carregarLivros() {
        modelo.setRowCount(0);
        List<Livro> livros = dao.listarLivros();

        if (livros != null) {
            for (Livro livro : livros) {
                adicionarLinha(livro);
            }
            status.setText("Livros apresentados: " + livros.size());
        } else {
            status.setText("Erro ao carregar livros do banco.");
        }
    }

    private void adicionarLinha(Livro livro) {
        ImageIcon miniCapa = redimensionarImagem(livro.getCapa(), 45, 64);
        modelo.addRow(new Object[]{
            livro.getId(),
            miniCapa,
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        });
    }

    private void buscarLivro() {
        String texto = campoId.getText().trim();
        int id;

        try {
            id = Integer.parseInt(texto);
            if (id <= 0) throw new NumberFormatException();
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Informe um ID inteiro positivo.", "Entrada inválida", JOptionPane.WARNING_MESSAGE);
            return;
        }

        Livro livro = dao.buscarLivroPorId(id);
        modelo.setRowCount(0);

        if (livro == null) {
            status.setText("Nenhum livro encontrado para o ID " + id);
            JOptionPane.showMessageDialog(this, "Livro não encontrado.", "Aviso", JOptionPane.INFORMATION_MESSAGE);
        } else {
            adicionarLinha(livro);
            status.setText("Livro encontrado: " + livro.getTitulo() + " (Total: 1)");
        }
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

    private JLabel criarLabel(String texto) {
        JLabel lbl = new JLabel(texto);
        lbl.setFont(FONTE_NEGRITO);
        return lbl;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TelaLivros().setVisible(true));
    }
}