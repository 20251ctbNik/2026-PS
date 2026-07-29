# SysControl v2.0 — Variante: Produto

Atividade de classes, objetos, encapsulamento e validação. A entidade escolhida foi **Produto**, representando um item de estoque com nome, código, preço e quantidade disponível.

## Estrutura da classe

```
Produto
├── nome              (String,  private)
├── codigo            (String,  private)
├── preco             (double,  private)
└── quantidadeEstoque (int,     private)
```

Todos os atributos são `private`. O acesso de fora da classe acontece só por getters (consulta) e, quando faz sentido, por setters que retornam `boolean` indicando se a alteração foi aceita ou recusada.

## Decisões de encapsulamento

- **`nome` e `codigo` não têm setter.** Eles representam a identidade do produto — mudar isso depois de criado, na prática, seria criar outro produto. Se precisar corrigir, a validação já acontece no construtor.
- **`preco` e `quantidadeEstoque` têm setter**, porque esses valores mudam naturalmente com o tempo (reajuste de preço, entrada/saída de mercadoria).
- Setters e métodos de comportamento nunca lançam exceção: eles retornam `false` quando a operação não pode ser feita, preservando o estado do objeto. O construtor é o único ponto que lança `IllegalArgumentException`, porque um objeto não pode nascer em estado inválido.

## Validações implementadas (mínimo 3 exigido)

1. `validarNome` — nome não pode ser nulo nem vazio/só espaços.
2. `validarCodigo` — código não pode ser nulo nem vazio/só espaços.
3. `validarPreco` — preço não pode ser negativo.
4. `validarQuantidade` — quantidade em estoque não pode ser negativa.

## Métodos de comportamento (mínimo 2 exigido)

- `venderUnidades(int quantidade)` — reduz o estoque; recusa se a quantidade for inválida ou maior que o estoque disponível.
- `aplicarDesconto(double percentual)` — reduz o preço em um percentual (0–100); recusa percentuais fora dessa faixa.

## Personalização exigida pelo enunciado

- Dia de nascimento do estudante (**11**) usado na quantidade em estoque do produto `p3`.
- Duas primeiras letras do primeiro nome (**"Ni"**) usadas no código do produto `p3` (`NI003`).

## Desafios complementares escolhidos

1. **Método de resumo textual** — `resumo()` retorna uma `String` formatada com todos os dados do produto, usada para exibir o estado sem acessar atributos diretamente.
2. **Método de comparação entre objetos** — `compararPorPreco(Produto outro)` compara dois produtos pelo preço, retornando negativo, positivo ou zero.

## Casos de teste

| # | Ação | Resultado esperado | Onde está no `Main` |
|---|------|---------------------|----------------------|
| 1 | Criar objeto com dados válidos | Objeto criado e exibido | Criação de `p1`, `p2`, `p3` |
| 2 | Atribuir texto vazio a campo obrigatório | Alteração recusada | Tentativa de criar produto com nome `""` |
| 3 | Atribuir número negativo a campo restrito | Alteração recusada | `p1.setPreco(-50.0)` |
| 4 | Executar comportamento permitido | Estado alterado corretamente | `p2.venderUnidades(10)` |
| 5 | Executar comportamento impossível | Estado preservado, retorno indicando falha | `p3.venderUnidades(500)` |

## Exemplo de execução

```
===== TESTE 1: Criar objetos com dados válidos =====
Produto[codigo=COD001, nome=Teclado Mecânico, preco=R$ 250,00, estoque=15 un.]
Produto[codigo=COD002, nome=Mouse Gamer, preco=R$ 120,50, estoque=30 un.]
Produto[codigo=NI003, nome=Monitor 24 polegadas, preco=R$ 899,90, estoque=11 un.]

===== TESTE 2: Atribuir texto vazio a campo obrigatório =====
Alteração recusada como esperado. Motivo: Nome do produto não pode ser vazio.

===== TESTE 3: Atribuir número negativo a campo numérico restrito =====
Tentativa de preço negativo aceita? false
Estado preservado -> Produto[codigo=COD001, nome=Teclado Mecânico, preco=R$ 250,00, estoque=15 un.]

===== TESTE 4: Executar comportamento permitido =====
Venda de 10 unidades realizada? true
Estado atualizado -> Produto[codigo=COD002, nome=Mouse Gamer, preco=R$ 120,50, estoque=20 un.]

===== TESTE 5: Executar comportamento impossível =====
Venda de 500 unidades realizada? false
Estado preservado -> Produto[codigo=NI003, nome=Monitor 24 polegadas, preco=R$ 899,90, estoque=11 un.]
```

*(Substitua pela captura de tela real da sua execução antes da entrega.)*

## Como executar

```bash
javac Produto.java Main.java
java Main
```