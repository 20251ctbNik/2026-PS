/**
 * Disciplina: 2026-PS
 * Estudante : Nickolas Kinceski Martins
 * Data      : 2026.08.20
 * Projeto   : aula32-projeto-secretaria
 * Arquivo   : Main.java
 */

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while (true) {

            System.out.println();
            System.out.println("==============================================");
            System.out.println("       SECRETARIA DO NICKOLAS");
            System.out.println("==============================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar aluno por matricula");
            System.out.println("[4] Atualizar aluno");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");

            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {

                System.out.println("Secretaria fechada. Ate a proxima!");
                break;

            } else if (opcao.equals("1")) {

                cadastrar(lista, teclado);

            } else if (opcao.equals("2")) {

                listar(lista);

            } else if (opcao.equals("3")) {

                buscar(lista, teclado);

            } else if (opcao.equals("4")) {

                atualizar(lista, teclado);

            } else if (opcao.equals("5")) {

                remover(lista, teclado);

            } else if (opcao.equals("6")) {

                relatorio(lista);

            } else {

                System.out.println("Opcao invalida!");

            }
        }

        teclado.close();
    }


    // ============================================================
    // CADASTRAR
    // ============================================================

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {

        System.out.println();
        System.out.println("--- CADASTRO DE ALUNO ---");

        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        if (nome.isEmpty()) {
            System.out.println("Erro: o nome nao pode ficar vazio.");
            return;
        }

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        if (matricula.isEmpty()) {
            System.out.println("Erro: a matricula nao pode ficar vazia.");
            return;
        }

        // Verifica se a matricula ja existe
        if (buscarPorMatricula(lista, matricula) != null) {
            System.out.println("Erro: essa matricula ja esta cadastrada.");
            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        if (curso.isEmpty()) {
            System.out.println("Erro: o curso nao pode ficar vazio.");
            return;
        }

        System.out.print("Email: ");
        String email = teclado.nextLine().trim();

        if (email.isEmpty()) {
            System.out.println("Erro: o email nao pode ficar vazio.");
            return;
        }

        Aluno novo = new Aluno(nome, matricula, curso, email);

        lista.add(novo);

        System.out.println("Ficha de " + nome + " guardada!");
    }


    // ============================================================
    // LISTAR
    // ============================================================

    static void listar(ArrayList<Aluno> lista) {

        System.out.println();

        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha cadastrada.");
            return;
        }

        System.out.println("--- FICHAS NO GAVETEIRO: " + lista.size() + " ---");

        for (Aluno aluno : lista) {
            System.out.println(aluno);
        }
    }


    // ============================================================
    // BUSCAR POR MATRICULA
    // ============================================================

    static Aluno buscarPorMatricula(
            ArrayList<Aluno> lista,
            String matricula) {

        for (Aluno aluno : lista) {

            if (aluno.getMatricula().equals(matricula)) {
                return aluno;
            }
        }

        return null;
    }


    // ============================================================
    // MENU DE BUSCA
    // ============================================================

    static void buscar(
            ArrayList<Aluno> lista,
            Scanner teclado) {

        System.out.println();
        System.out.println("--- BUSCAR ALUNO ---");

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        Aluno aluno = buscarPorMatricula(lista, matricula);

        if (aluno == null) {
            System.out.println("Aluno nao encontrado.");
            return;
        }

        System.out.println("Aluno encontrado:");
        System.out.println(aluno);
    }


    // ============================================================
    // ATUALIZAR
    // ============================================================

    static void atualizar(
            ArrayList<Aluno> lista,
            Scanner teclado) {

        System.out.println();
        System.out.println("--- ATUALIZAR ALUNO ---");

        System.out.print("Matricula do aluno: ");
        String matricula = teclado.nextLine().trim();

        Aluno aluno = buscarPorMatricula(lista, matricula);

        if (aluno == null) {
            System.out.println("Aluno nao encontrado.");
            return;
        }

        System.out.println();
        System.out.println("Aluno atual:");
        System.out.println(aluno);

        System.out.println();
        System.out.print("Novo nome: ");
        String novoNome = teclado.nextLine().trim();

        if (novoNome.isEmpty()) {
            System.out.println("Erro: o nome nao pode ficar vazio.");
            return;
        }

        System.out.print("Novo curso: ");
        String novoCurso = teclado.nextLine().trim();

        if (novoCurso.isEmpty()) {
            System.out.println("Erro: o curso nao pode ficar vazio.");
            return;
        }

        System.out.print("Novo email: ");
        String novoEmail = teclado.nextLine().trim();

        if (novoEmail.isEmpty()) {
            System.out.println("Erro: o email nao pode ficar vazio.");
            return;
        }

        aluno.setNome(novoNome);
        aluno.setCurso(novoCurso);
        aluno.setEmail(novoEmail);

        System.out.println("Aluno atualizado com sucesso!");
    }


    // ============================================================
    // REMOVER
    // ============================================================

    static void remover(
            ArrayList<Aluno> lista,
            Scanner teclado) {

        System.out.println();
        System.out.println("--- REMOVER ALUNO ---");

        System.out.print("Matricula do aluno: ");
        String matricula = teclado.nextLine().trim();

        Aluno aluno = buscarPorMatricula(lista, matricula);

        if (aluno == null) {
            System.out.println("Aluno nao encontrado.");
            return;
        }

        System.out.println();
        System.out.println("Aluno encontrado:");
        System.out.println(aluno);

        System.out.print("Tem certeza que deseja remover? (s/n): ");
        String confirmacao = teclado.nextLine().trim();

        if (confirmacao.equalsIgnoreCase("s")) {

            lista.remove(aluno);

            System.out.println("Aluno removido com sucesso!");

        } else {

            System.out.println("Remocao cancelada.");
        }
    }


    // ============================================================
    // RELATORIO
    // ============================================================

    static void relatorio(ArrayList<Aluno> lista) {

        System.out.println();
        System.out.println("--- RELATORIO DA SECRETARIA ---");

        System.out.println("Total de alunos: " + lista.size());

        if (lista.size() == 0) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }

        ArrayList<String> cursos = new ArrayList<String>();
        ArrayList<Integer> quantidades = new ArrayList<Integer>();

        for (Aluno aluno : lista) {

            String curso = aluno.getCurso();

            int posicao = cursos.indexOf(curso);

            if (posicao == -1) {

                cursos.add(curso);
                quantidades.add(1);

            } else {

                int quantidadeAtual = quantidades.get(posicao);
                quantidades.set(posicao, quantidadeAtual + 1);
            }
        }

        System.out.println();
        System.out.println("Alunos por curso:");

        for (int i = 0; i < cursos.size(); i++) {

            System.out.println(
                cursos.get(i) + ": " + quantidades.get(i)
            );
        }
    }
}