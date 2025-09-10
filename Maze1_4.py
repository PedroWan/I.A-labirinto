import random
import math
import matplotlib.pyplot as plt

# -------- Classe Cell --------
class Cell:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.energy = 50  # energia inicial padrão

    def __eq__(self, other):
        return self.position == other.position

# -------- Geração do Labirinto --------
def generate_maze(size, min_walls=15, max_walls=35, start=(0, 0), end=(9, 9)):
    maze = [[1 for _ in range(size)] for _ in range(size)]  # inicializa tudo como caminho livre
    maze[start[0]][start[1]] = 1
    maze[end[0]][end[1]] = 1

    # Gerar paredes aleatórias
    num_walls = random.randint(min_walls, max_walls)
    walls = 0
    while walls < num_walls:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if (x, y) != start and (x, y) != end and maze[x][y] != 0:
            maze[x][y] = 0
            walls += 1

    return maze

# -------- Função A* --------
def a_star(maze, start, end):
    open_list = []
    closed_list = []
    start_node = Cell(position=start)
    end_node = Cell(position=end)
    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Se o caminho chegou ao fim, reconstruir o caminho
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            path.reverse()  # O caminho está invertido, então invertemos
            return path

        # Gerar os vizinhos
        neighbors = [
            (current_node.position[0] - 1, current_node.position[1]),  # cima
            (current_node.position[0] + 1, current_node.position[1]),  # baixo
            (current_node.position[0], current_node.position[1] - 1),  # esquerda
            (current_node.position[0], current_node.position[1] + 1)   # direita
        ]

        for neighbor_pos in neighbors:
            # Verificar se a posição está dentro dos limites
            if 0 <= neighbor_pos[0] < len(maze) and 0 <= neighbor_pos[1] < len(maze[0]) and maze[neighbor_pos[0]][neighbor_pos[1]] != 0:
                neighbor = Cell(position=neighbor_pos, parent=current_node)
                
                if neighbor not in closed_list:
                    # Calcular o custo g, h, f para este vizinho
                    neighbor.g = current_node.g + 1
                    neighbor.h = abs(neighbor.position[0] - end_node.position[0]) + abs(neighbor.position[1] - end_node.position[1])
                    neighbor.f = neighbor.g + neighbor.h
                    
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return []  # Se não encontrar o caminho

# -------- Função de Visualização --------
def desenhar_labirinto(labirinto, path=None):
    # Definindo as cores para os diferentes valores no labirinto
    cores = {
        0: 'black',       # Obstáculo
        1: 'yellowgreen', # Caminho livre
        4: 'blue',        # Início ou fim
    }
    
    fig, ax = plt.subplots()

    tamanho = len(labirinto)
    for i in range(tamanho):
        for j in range(tamanho):
            valor = labirinto[i][j]
            cor = cores.get(valor, 'gray')  # Se não encontrado, usar cinza

            rect = plt.Rectangle([j, tamanho - 1 - i], 1, 1, facecolor=cor, edgecolor='black')
            ax.add_patch(rect)

    # Destacando o caminho percorrido (caso haja um)
    if path:
        for (i, j) in path:
            # Garantir que a célula esteja dentro do labirinto (verificação de limites)
            if 0 <= i < tamanho and 0 <= j < tamanho:  # Não desenha se for fora do labirinto
                if labirinto[i][j] != 0:  # Não desenha se for obstáculo
                    rect = plt.Rectangle([j, tamanho - 1 - i], 1, 1, facecolor='blue', edgecolor='black')
                    ax.add_patch(rect)

    # Ajusta os limites 
    ax.set_xlim(0, tamanho)
    ax.set_ylim(0, tamanho)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    plt.gca().invert_yaxis()
    plt.show()

# Gerar labirinto com tamanho 10x10, 15 a 35 paredes
maze = generate_maze(10, 15, 35)

# Encontrar o caminho do robô
path = a_star(maze, start=(0, 0), end=(9, 9))

# Desenhar o labirinto gerado e o caminho percorrido
desenhar_labirinto(maze, path)


