# -*- coding: utf-8 -*-
import sys

# --- Bloco 1: Estrutura da Árvore e Funções de Impressão ---

class Node:
    """Classe para representar um nó da árvore."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construir_arvore(raiz, keys, i, j):
    """Constrói a árvore recursivamente a partir da tabela de raízes."""
    if i > j:
        return None
    
    indice_raiz = raiz[i][j]
    # O índice do array original de chaves é `indice_raiz - 1`
    no = Node(keys[indice_raiz - 1])
    
    no.left = construir_arvore(raiz, keys, i, indice_raiz - 1)
    no.right = construir_arvore(raiz, keys, indice_raiz + 1, j)
    
    return no

def imprimir_arvore(no, nivel=0, prefixo="Raiz:"):
    """Imprime a estrutura da árvore de forma visual."""
    if no is not None:
        print(" " * (nivel * 4) + prefixo, no.key)
        if no.left is not None or no.right is not None:
            imprimir_arvore(no.left, nivel + 1, "E:---")
            imprimir_arvore(no.right, nivel + 1, "D:---")

# --- Bloco 2: O Algoritmo da OBST ---

def optimal_bst(keys, p, q):
    """
    Calcula o custo da Árvore de Busca Binária Ótima usando programação dinâmica.
    """
    n = len(keys)
    
    # Adicionando elementos "dummy" para facilitar a indexação (de 1 a n)
    _keys = [None] + keys 
    _p = [None] + p
    _q = q
    
    custo = [[0.0] * (n + 2) for _ in range(n + 2)]
    raiz = [[0] * (n + 1) for _ in range(n + 1)]
    w = [[0.0] * (n + 2) for _ in range(n + 2)]
    
    # Casos Base e Preenchimento da tabela W
    for i in range(1, n + 2):
        custo[i][i-1] = _q[i-1]
        w[i][i-1] = _q[i-1]
        
    # Lógica da Programação Dinâmica
    for L in range(1, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            w[i][j] = w[i][j-1] + _p[j] + _q[j]
            custo[i][j] = sys.float_info.max 
            
            for r in range(i, j + 1):
                custo_atual = custo[i][r-1] + custo[r+1][j] + w[i][j]
                if custo_atual < custo[i][j]:
                    custo[i][j] = custo_atual
                    raiz[i][j] = r
                    
    return custo, raiz

# --- Bloco 3: Carregamento de Dados e Execução Principal ---

def carregar_dados_de_arquivo(nome_arquivo):
    """Lê as chaves e probabilidades de um arquivo de texto."""
    try:
        with open(nome_arquivo, 'r') as f:
            linhas = [linha for linha in f if not linha.startswith('#') and linha.strip()]

        if len(linhas) < 3:
            raise ValueError("O arquivo de dados deve conter 3 linhas ativas (chaves, p, q).")

        chaves = [int(k) for k in linhas[0].split()]
        p = [float(prob) for prob in linhas[1].split()]
        q = [float(prob) for prob in linhas[2].split()]
        
        # Validações básicas
        if len(chaves) != len(p):
            raise ValueError("O número de chaves deve ser igual ao número de probabilidades 'p'.")
        if len(q) != len(chaves) + 1:
             raise ValueError("O número de probabilidades 'q' deve ser igual ao número de chaves + 1.")
        
        return chaves, p, q
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None, None, None
    except (ValueError, IndexError) as e:
        print(f"Erro ao processar o arquivo de dados: {e}")
        return None, None, None


if __name__ == "__main__":
    nome_do_arquivo = "exemplo_dados.txt"
    chaves, p, q = carregar_dados_de_arquivo(nome_do_arquivo)
    
    if chaves:
        print(f"Dados carregados de '{nome_do_arquivo}':")
        print("Chaves:", chaves)
        print("Probabilidades p (sucesso):", p)
        print("Probabilidades q (falha):", q)
        print("-" * 30)

        # Executa o algoritmo
        tabela_custo, tabela_raiz = optimal_bst(chaves, p, q)
        
        custo_minimo = tabela_custo[1][len(chaves)]
        
        print(f"O custo mínimo da Árvore de Busca Binária Ótima é: {custo_minimo:.2f}")
        print("-" * 30)
        
        # Constrói e imprime a árvore resultante
        n = len(chaves)
        raiz_arvore = construir_arvore(tabela_raiz, chaves, 1, n)
        
        print("Estrutura da Árvore Ótima:")
        imprimir_arvore(raiz_arvore)