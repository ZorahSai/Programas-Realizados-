def calcular_preco_venda(num_paginas, tipo_encadernacao, num_copias):
    custo_pagina = 0.03
    custo_fixo = 4397.00

    # Custos de encadernação
    if tipo_encadernacao == 'simples':
        custo_encadernacao = 4.30
    elif tipo_encadernacao == 'especial':
        custo_encadernacao = 7.80
    elif tipo_encadernacao == 'luxo':
        custo_encadernacao = 10.50
    else:
        raise ValueError("Tipo de encadernação inválido")

    # Cálculo do custo total
    custo_producao = (num_paginas * custo_pagina) + custo_encadernacao + custo_fixo
    custo_por_unidade = custo_producao / num_copias

    # Preço de venda com lucro de 20%
    preco_venda = custo_por_unidade * 1.20

    return preco_venda

def main():
    livros = []
    while True:
        try:
            num_paginas = int(input("Número de páginas (ou 0 para encerrar): "))
            if num_paginas == 0:
                break
            
            tipo_encadernacao = input("Tipo de encadernação (simples, especial, luxo): ").strip().lower()
            num_copias = int(input("Número de vendas previstas (cópias): "))

            preco_venda = calcular_preco_venda(num_paginas, tipo_encadernacao, num_copias)
            livros.append(preco_venda)
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
    
    if livros:
        total_livros = len(livros)
        preco_medio = sum(livros) / total_livros
        preco_minimo = min(livros)
        preco_maximo = max(livros)

        print(f"\nTotal de livros analisados: {total_livros}")
        print(f"Preço médio de venda dos livros: R${preco_medio:.2f}")
        print(f"Preço de venda do livro mais barato: R${preco_minimo:.2f}")
        print(f"Preço de venda do livro mais caro: R${preco_maximo:.2f}")
    else:
        print("Nenhum livro foi analisado.")

if __name__ == "__main__":
    main()
