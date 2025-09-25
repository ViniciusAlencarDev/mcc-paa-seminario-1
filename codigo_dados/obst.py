# -*- coding: utf-8 -*-
import sys

# --- Bloco 1: Estrutura da Árvore e Funções de Impressão ---

class Node:
    """Classe para representar um nó da árvore."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def construir_arvore(raiz_tabela, keys, i, j):
    """Constrói a árvore recursivamente a partir da tabela de raízes."""
    if i > j:
        return None
    
    indice_raiz = raiz_tabela[i][j]
    no = Node(keys[indice_raiz])
    
    no.left = construir_arvore(raiz_tabela, keys, i, indice_raiz - 1)
    no.right = construir_arvore(raiz_tabela, keys, indice_raiz + 1, j)
    
    return no

def imprimir_arvore(no, nivel=0, prefixo="Raiz:"):
    """Imprime a estrutura da árvore de forma visual."""
    if no is not None:
        print(" " * (nivel * 4) + prefixo, no.key)
        if no.left is not None or no.right is not None:
            imprimir_arvore(no.left, nivel + 1, "E:---")
            imprimir_arvore(no.right, nivel + 1, "D:---")

# --- Bloco 2: O Algoritmo da OBST ---

def calcular_obst_simplificado(keys, freqs):
    """
    Calcula o custo da Árvore de Busca Binária Ótima usando a lógica simplificada.
    """
    n = len(keys)
    custo = [[0] * n for _ in range(n)]
    raiz = [[0] * n for _ in range(n)]

    # Casos Base: sub-árvores de tamanho 1
    for i in range(n):
        custo[i][i] = freqs[i]
        raiz[i][i] = i

    # Lógica da Programação Dinâmica (Bottom-Up)
    for tamanho in range(2, n + 1):
        for i in range(n - tamanho + 1):
            j = i + tamanho - 1
            custo[i][j] = sys.maxsize
            soma_freqs = sum(freqs[k] for k in range(i, j + 1))

            for r_idx in range(i, j + 1):
                c_esquerda = custo[i][r_idx - 1] if r_idx > i else 0
                c_direita = custo[r_idx + 1][j] if r_idx < j else 0
                
                custo_atual = c_esquerda + c_direita + soma_freqs
                
                if custo_atual < custo[i][j]:
                    custo[i][j] = custo_atual
                    raiz[i][j] = r_idx
                    
    return custo, raiz

# --- Bloco 3: Carregamento de Dados e Execução  ---

def carregar_dados_de_arquivo(nome_arquivo):
    """Lê as chaves e frequências de um arquivo de texto."""
    try:
        with open(nome_arquivo, 'r') as f:
            linhas = [linha for linha in f if not linha.startswith('#') and linha.strip()]

        if len(linhas) < 2:
            raise ValueError("O arquivo de dados deve conter 2 linhas ativas (chaves, freqs).")

        chaves = [int(k) for k in linhas[0].split()]

        freqs = [int(prob) for prob in linhas[1].split()]
        
        if len(chaves) != len(freqs):
            raise ValueError("O número de chaves deve ser igual ao número de frequências.")
        
        return chaves, freqs
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None, None
    except (ValueError, IndexError) as e:
        print(f"Erro ao processar o arquivo de dados: {e}")
        return None, None

if __name__ == "__main__":
    # Crie um arquivo com este nome e conteúdo para testar
    nome_do_arquivo = "exemplo_dados.txt"
    chaves, freqs = carregar_dados_de_arquivo(nome_do_arquivo)
    
    if chaves:
        print(f"Dados carregados de '{nome_do_arquivo}':")
        print("Chaves:", chaves)
        print("Frequências:", freqs)
        print("-" * 30)

        
        tabela_custo, tabela_raiz = calcular_obst_simplificado(chaves, freqs)
        
        # O custo mínimo está na posição [0][n-1] com base 0
        n = len(chaves)
        custo_minimo = tabela_custo[0][n-1]
        
        print(f"O custo mínimo (soma ponderada) da Árvore é: {custo_minimo}")
        print("-" * 30)
        
        # Constrói e imprime a árvore resultante
        # Usa os índices [0] e [n-1] para a construção inicial
        raiz_arvore = construir_arvore(tabela_raiz, chaves, 0, n - 1)
        
        print("Estrutura da Árvore Ótima:")
        imprimir_arvore(raiz_arvore)