def linha_separadora (char="=", largura = 40):
    """retorna uma linha separadora"""
    return char * largura

def formatar_resultado(origem, valor_original, unidade_origem, valorconvertido, unidade_destino):
    """Formata a exibição de um resultado de conversão"""
    return f"   {origem}: {valor_original:.2f} {unidade_origem} {valorconvertido} {unidade_destino}"

def cabecalho_secao(titulo):
    """Retorna um cabeçalho de seção formatada"""
    sep = linha_separadora("-", len(titulo)  + 4)
    return f"\n{sep}\n {titulo}\n{sep}"