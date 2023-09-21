import random 
import time

# Class representing cells
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = None
        self.walls = {"top": True, "left": True, "bottom": True, "right": True}
        self.visited = False

# Find and collect references to neighboring cells of the current cell
    def get_neighbors(self, grid):
        x, y = self.x, self.y
        neighbors = []

        if x > 0:
            neighbors.append(grid[x - 1][y])
        if y > 0:
            neighbors.append(grid[x][y - 1])
        if x < len(grid) - 1:
            neighbors.append(grid[x + 1][y])
        if y < len(grid[0]) -1:
            neighbors.append(grid[x][y + 1])

        return neighbors
 
    def set_visited(self):
        self.visited = True

# Mark a cell as visited      
    def is_visited(self):
        return self.visited
# Define IDs of cells
    def find_id(self):
        return self.id
    
    def get_walls(self):
        return self.walls
    
class Maze:
    def __init__(self, size):
        self.width = size
        self.height = size
        self.grid = [[Cell(x, y) for x in range(size)] for y in range(size)]
        self.counter = 0

    def get_cell(self, x, y):
        return self.grid[y][x]
    
    def assign_id(self, cell):
        if cell.id is None:
            cell.id = self.counter
            self.counter += 1

    def link_id(self, cell1, cell2):
        id1 = cell1.find_id()
        id2 = cell2.find_id()

        if id1 != id2:
            for x in self.grid: 
                for cell in x:
                    if cell.id == id1:
                        cell.id = id2

    def kruskal_generate(self):
        walls = []

        for row in self.grid:
            for cell in row:
                self.assign_id(cell)
                neighbors = cell.get_neighbors(self.grid)
                random.shuffle(neighbors)

            for neighbor in neighbors:
                walls.append((cell, neighbor))

        random.shuffle(walls)

        for wall in walls:
            cell1, cell2 = wall

            if cell1.find_id() != cell2.find_id():
                row1, col1 = cell1.x, cell1.y
                row2, col2 = cell2.x, cell2.y
                if row1 == row2:
                    if col1 < col2:
                        cell1.walls["right"] = False
                        cell2.walls["left"] = False
                    else:
                        cell1.walls["left"] = False
                        cell2.walls['right'] = False

                else: 
                    if row1 < row2:
                        cell1.walls["bottom"] = False
                        cell2.walls["top"] = False
                    else:
                        cell1.walls["top"] = False
                        cell2.walls["bottom"] = False

                self.link_id(cell1, cell2)

    def depth_first_search(self, start_x, start_y):
        stack = [(start_x, start_y)]
        while stack:
            x, y = stack.pop()
            cell = self.get_cell(x, y)
            cell.set_visited()
            neighbors = [n for n in cell.get_neighbors(self.grid) if not n.is_visited()]
            if neighbors:
                stack.append((x, y))
                next_x, next_y = neighbors[random.randint(0, len(neighbors) - 1)].x, neighbors[random.randint(0, len(neighbors) - 1)].y
                cell2 = self.get_cell(next_x, next_y)
                cell2.set_visited()
                if x == next_x:
                    if y < next_y:
                        cell.walls["right"] = False
                        cell2.walls["left"] = False
                    else:
                        cell.walls["left"] = False
                        cell2.walls["right"] = False
                else:
                    if x < next_x:
                        cell.walls["bottom"] = False
                        cell2.walls["top"] = False
                    else:
                        cell.walls["top"] = False
                        cell2.walls["bottom"] = False
                stack.append((next_x, next_y))

    def print_maze(self):
        n = self.width
        size = 2 * n + 1
        maze = [['#' for _ in range(size)] for _ in range(size)]

        for row in range(size):
            for col in range(size):
                if (not (row == 0 or row == size - 1)) or (not (col == 0 or col == size - 1)):
                    
                    if row % 2 != 0 and col % 2 != 0:
                        maze[row][col] = "."

                        n_row, n_col = int((row - 1) / 2), int((col - 1) / 2)

                        if self.get_cell(n_col, n_row).get_walls()["right"] == False:
                            maze[row][col + 1] = "."
                        if self.get_cell(n_col, n_row).get_walls()["left"] == False:
                            maze[row][col - 1] = "."
                        if self.get_cell(n_col, n_row).get_walls()["top"] == False:
                            maze[row  - 1][col] = "."
                        if self.get_cell(n_col, n_row).get_walls()["bottom"] == False:
                            maze[row  + 1][col] = "."

                        
        maze[1][0] = "."
        maze[2 * n - 1][2 * n] = "."

        return maze

def main_script2():
    n = int(input("Entrez la taille du labyrinthe (un nombre entier naturel) : "))
    filename = input("Entrez le nom du fichier de sortie (avec l'extension .txt) : ")

    if n % 2 == 0:
        n += 1
    start = time.time()
    maze = Maze(n)
    maze.kruskal_generate()
    maze.depth_first_search(0, 0) 
    end = time.time()
    elapsed = end - start
    labyrinthe = maze.print_maze()
    with open(filename, 'w') as f:
        for row in labyrinthe:
            f.write("".join(row) + '\n')

    print(f"Le labyrinthe a été généré et enregistré dans le fichier {filename} en {elapsed} secondes")

    with open('log.txt', 'a') as log_file:
        log_file.write(f"The generation of the maze size {n}*{n} took {elapsed} seconds with Kruskal's algorithm\n")

if __name__ == "__main__":
    main_script2()
