"""
Módulo para controlar o jogador e sua pontuação.
"""

import time
from rich import print

class Jogador:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.pos = (0, 0)  # começa no topo-esquerdo
        self.pontuacao = 0

    def mover(self, comando):
        """
        Move o jogador conforme o comando (w,a,s,d).
        Comando é case-insensitive (maiúsculas ou minúsculas).
        Retorna True se o movimento foi válido, False se inválido.
        """
        comando = comando.lower()
        i, j = self.pos

        if comando == 'w':
            i -= 1
        elif comando == 's':
            i += 1
        elif comando == 'a':
            j -= 1
        elif comando == 'd':
            j += 1
        else:
            return False  # comando inválido

        # Verifica limites do labirinto
        if i < 0 or j < 0 or i >= len(self.labirinto) or j >= len(self.labirinto[0]):
            return False

        # Verifica se não é parede
        if self.labirinto[i][j] == 1:
            return False

        # Movimento válido, atualiza a posição
        self.pos = (i, j)
        return True

    def pontuar(self):
        """
        Se o jogador estiver numa célula com item (2),
        aumenta a pontuação e remove o item do labirinto.
        """
        i, j = self.pos
        if self.labirinto[i][j] == 2:
            self.pontuacao += 10
            self.labirinto[i][j] = 0


def resolver_labirinto_recursivo(labirinto, x, y, caminho, visitados):
    """
    Função recursiva para encontrar o caminho até a saída.
    """
    linhas, colunas = len(labirinto), len(labirinto[0])

    # Fora dos limites ou já visitado ou parede
    if (x < 0 or x >= linhas or y < 0 or y >= colunas or
        labirinto[x][y] == 1 or (x, y) in visitados):
        return False

    caminho.append((x, y))
    visitados.add((x, y))

    # Verifica se chegou na saída
    if (x, y) == (linhas - 1, colunas - 1):
        return True

    # Tenta se mover: baixo, direita, cima, esquerda
    if (resolver_labirinto_recursivo(labirinto, x+1, y, caminho, visitados) or
        resolver_labirinto_recursivo(labirinto, x, y+1, caminho, visitados) or
        resolver_labirinto_recursivo(labirinto, x-1, y, caminho, visitados) or
        resolver_labirinto_recursivo(labirinto, x, y-1, caminho, visitados)):
        return True

    # Se nenhum caminho deu certo, remove e volta
    caminho.pop()
    return False


def animar_solucao(labirinto, caminho):
    """
    Mostra passo a passo o caminho encontrado.
    """
    from aventura_pkg.labirinto import imprimir_labirinto
    for pos in caminho:
        time.sleep(0.3)
        imprimir_labirinto(labirinto, pos)
        print()