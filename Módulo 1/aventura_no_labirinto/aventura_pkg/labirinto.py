"""
Módulo para criar e imprimir o labirinto.
"""

from rich.console import Console
import random

console = Console()

def criar_labirinto(dificuldade=1):
    """
    Cria uma matriz (lista de listas) representando o labirinto.
    Usa a dificuldade para mudar o tamanho ou complexidade.
    """
    tamanho = {1: 5, 2: 7, 3: 10}.get(dificuldade, 5)
    lab = []

    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            # 0 = espaço livre, 1 = parede, 2 = item
            valor = random.choices([0, 1, 2], weights=[0.7, 0.2, 0.1])[0]
            linha.append(valor)
        lab.append(linha)

    # Garantir entrada e saída livre
    lab[0][0] = 0
    lab[tamanho - 1][tamanho - 1] = 0

    return lab

def imprimir_labirinto(labirinto, pos_jogador):
    """
    Imprime o labirinto na tela, mostrando o jogador, as paredes e os itens.
    """
    console.clear()
    for i in range(len(labirinto)):
        linha_str = ""
        for j in range(len(labirinto[i])):
            if (i, j) == pos_jogador:
                linha_str += "[bold green]@[/bold green]"  # jogador
            elif labirinto[i][j] == 1:
                linha_str += "█"  # parede
            elif labirinto[i][j] == 2:
                linha_str += "[yellow]*[/yellow]"  # item
            else:
                linha_str += " "  # caminho livre
        console.print(linha_str)