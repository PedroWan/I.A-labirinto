# Atualizando o código para simular visão local (o robô só enxerga as posições vizinhas)
import random
import math

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

# -------- Heurísticas --------
class Heuristics:
    def euclidean(self, current, end, parent):
        dx = current.position[0] - end.position[0]
        dy = current.position[1] - end.position[1]
        current.g = parent.g + 1
        current.h = math.sqrt(dx**2 + dy**2)
        current.f = current.g + current.h

# -------- Geração do Labirinto --------
def generate_maze(size, min_walls=15, max_walls=35, start=(0, 0), end=(9, 9)):
    maze = [[0 for _ in range(size)] for _ in range(size)]
    wall_count = random.randint(min_walls, max_walls)

    for _ in range(wall_count):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        while (i, j) == start or (i, j) == end or maze[i][j] == 1:
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
        maze[i][j] = 1

    return maze

# -------- Geração das Posições de Recarga --------
def generate_energy_positions(maze, start, end):
    size = len(maze)
    recharge_5 = set()
    recharge_10 = set()

    while len(recharge_5) < 5:
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        if maze[i][j] == 0 and (i, j) != start and (i, j) != end:
            recharge_5.add((i, j))

    while len(recharge_10) < 3:
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        if maze[i][j] == 0 and (i, j) != start and (i, j) != end and (i, j) not in recharge_5:
            recharge_10.add((i, j))

    return list(recharge_5), list(recharge_10)

# -------- Algoritmo com Visão Local --------
def local_astar(maze, start, end, recharge_5, recharge_10):
    current = Cell(None, start)
    current.energy = 50
    path = [start]
    visited = set()
    visited.add(start)

    while current.position != end:
        i, j = current.position
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        neighbors = []

        for move in moves:
            ni, nj = i + move[0], j + move[1]
            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
                if maze[ni][nj] == 0 and (ni, nj) not in visited:
                    neighbor = Cell(current, (ni, nj))
                    neighbor.energy = current.energy - 1
                    if (ni, nj) in recharge_5:
                        neighbor.energy += 5
                    elif (ni, nj) in recharge_10:
                        neighbor.energy += 10
                    if neighbor.energy > 0:
                        neighbors.append(neighbor)

        if not neighbors:
            return None  # Sem caminho

        heuristics = Heuristics()
        for n in neighbors:
            heuristics.euclidean(n, Cell(None, end), current)

        next_move = min(neighbors, key=lambda n: n.f)
        current = next_move
        path.append(current.position)
        visited.add(current.position)

    return path

# -------- Impressão do Labirinto --------
def print_maze(maze, path=[], recharge_5=[], recharge_10=[]):
    for i in range(len(maze)):
        row = ""
        for j in range(len(maze[i])):
            pos = (i, j)
            if pos in path:
                row += "* "
            elif pos in recharge_5:
                row += "+ "
            elif pos in recharge_10:
                row += "@ "
            elif maze[i][j] == 1:
                row += "# "
            else:
                row += ". "
        print(row)

# -------- Execução --------
def run_test(size=10):
    start, end = (0, 0), (size - 1, size - 1)
    maze = generate_maze(size, start=start, end=end)
    r5, r10 = generate_energy_positions(maze, start, end)
    path = local_astar(maze, start, end, r5, r10)

    print_maze(maze, path if path else [], r5, r10)
    print("\\nPath found:" if path else "\\nNo path found.")

if __name__ == "__main__":
    run_test()