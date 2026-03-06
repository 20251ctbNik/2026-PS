# Arquivo: 01b-debug.py
# ATENÇÃO: 4 erros propositeis. Encontre e corrija todos!

catalogo = [
    {"titulo": "Código Limpo",      "autor": "Robert C. Martin", "disponivel":
     True},
    {"titulo": "Entendnedo Algoritmos", "autor": "Aditya Bhargava", "disponivel":
     False},
    {"titulo": "Python Fluente",        "autor": "Luciano Ramalho",
    "disponivel": True}
]

print("primeiro livro:", catalogo[0]["titulo"])         # Erro 1: O catalogo tem 3 elesmentos (então os índices são 0, 1 e 2), o índice 3 não existe.

print("\nLivros disponiveis:")
for livro in catalogo:
    if livro["disponivel"] == True:                     # Erro 2: O programa diz sobre os titulos disponíveis, mas o programa imprimia os livros indisponíveis. Isso aconteceu porque no lugar do "True" estavba o "False".
        print(f' {livro["titulo"]}')
    
total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items():                  # Erro 3: O erro acontece porque iterar diretamente não funciona porque o "for chave, valor in catalogo[0]" retorna apenas as as chaves. Parra funcionar corretamente é necessário adicionar um ".items()" ao final.
    print(f"    {chave}: {valor}")

primeiro_autor = catalogo[0]["autor"]                   # Erro 4: O código guarda o dicionário inteiro em "primeiro_autor", mas na verdade deveria guardar só valor da chave "autor". Então para corrigir o correto é usar um '["autor"]' ao final.
print("\nAutor do primeiro livro:", primeiro_autor)