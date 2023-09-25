import random 
import os
import time

class Solving:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.open = (1, 0)
        self.entrance = (1, 1)
        self.exit = (self.n - 2, self.n - 2)
        self.path = []
        self.visited = []
        self.visited.append((1, 0))
        self.neighbors = {"Left": None, "Top": None, "Right": None, "Bottom": None}

    def print_maze(self):
        for row in self.maze:
            for cell in row:
                print(cell, end='')
            print()
        print()

# Take for parameter a cell represented by a tuple and return None
    def check_neighbors(self, cell:tuple) -> None:
        # Extract the coordinates of a cell by the tuple
        x = cell[0]
        y = cell[1]

        # Check if a cell has a neighbor in every directions
        if x > 0:
            self.neighbors["Top"] = (x - 1, y)
        else:
            self.neighbors["Top"] = None
        if y > 0:
            self.neighbors["Left"] = (x, y - 1)
        else:
            self.neighbors["Left"] = None
        if x < self.n - 1:
            self.neighbors["Bottom"] = (x + 1, y)
        else:
            self.neighbors["Bottom"] = None
        if y < self.n - 1:
            self.neighbors["Right"] = (x, y + 1)
        else:
            self.neighbors["Right"] = None

    def backtrack_solver(self, position) -> None:
        # Initialize a cell with the position and call check_neighbors to determine its neighbors
        # An empty list is initialize too to store the possible directions for the solver
        cell = position
        self.check_neighbors(cell)
        directions = []

        # Check if the current cell is the exit, if it's the case, print a message.
        if cell == self.exit:
            print("")
            print("Exit founded !")
        # Runs every cells in self.path and mark those which are not in self.visited as "wrong way" and replace them with "*"
        # Then, mark the cells in self.path as explored cells and replace them with "o" and return the updated maze
            for cell in self.path:
                for visited in self.visited:
                    if visited not in self.path:
                        self.maze[visited[0]][visited[1]] = "*"
                self.maze[cell[0]][cell[1]] = "o"
            return self.maze
        
        # If the current cell is not cisited (not in self.visited) it's added to self.visited and self.path to follow the current path
        if cell not in self.visited:
            self.visited.append(cell)
            self.path.append(cell)

        # Runs the possible directions in fonction of the neighbors cells.
        # For each direction, it checks if the neighbor cell is not a wall and not visited
        # If it's not, the direction is added to 'directions' list to indicate that is possible to move in this direction
        for direction in self.neighbors:
            if self.maze[self.neighbors[direction][0]][self.neighbors[direction][1]] != "#":
                if self.neighbors[direction] not in self.visited:
                    directions.append(direction)
        
        # If the possible directions were founded in the precedent step, one is chosen randomly 
        # The cell corresponding to this direction is updated as the new current cell
        # If this cell is not visited, it's added to self.visited and self.path 
        # If no direction is found, the last cell is removed of self.path
        if len(directions) > 0:
            direction = random.choice(directions)
            cell = self.neighbors[direction]
            
            if cell not in self.visited:
                self.visited.append(cell)
                self.path.append(cell)
        else:
            self.path.pop()
            cell = self.path[-1]

        # The backtrack_solver function is recursively called with the current new cell. 
        # This allows the solver to continue exploring the maze in different directions until the exit is found or all possibilities have been explored.
        self.backtrack_solver(cell)
        self.print_maze()

    def astar(self) -> None:
        begin = self.entrance
        end = self.exit
        begin_list = [] # Contain the cells to explore
        close_list = [] # Contain the cells already explored
        h = self.heuristic(begin, end) # Heuristic estimation of the remaining cost from begin to end.
        g = {begin: 0} # Dictionary containing the actual costs of moving from begin to each explored cell
        f = {begin: h + g[begin]} # Dictionary containing the sum of the real costs and the heuristic estimate for each cell
        parent = {begin: None} # Dictionary that maintains the relationship between each cell and its parent cell in the path found so far
        actual_cell = begin

        # Initialize a list with the start cell 
        begin_list.append(begin)

        # Start a loop while the list is not empty, in each iteration the cell with the smallest cost is extract and become the actual cell
        while len(begin_list) > 0:
            begin_list.sort(key = lambda x: f[x])
            actual_cell = begin_list.pop(0)

        # If actual_cell is the exit, a message is show and and generate the path founded using make_path
            if actual_cell == end:
                print("Exit founded !")
                for cell in self.make_path(parent, actual_cell):
                    for visited in close_list:
                        if visited not in self.make_path(parent, actual_cell):
                            self.maze[visited[0]][visited[1]] = "*"
                    self.maze[cell[0]][cell[1]] = "o"
                return
            else:
                close_list.append(actual_cell)

            # Check the neighbors of a cell with check_neighbors fonction and determine which direction is valid
            self.check_neighbors(actual_cell)
            directions = []
            for direction in self.neighbors:
                if self.neighbors[direction] is not None:
                    if self.maze[self.neighbors[direction][0]][self.neighbors[direction][1]] != "#":
                        if self.neighbors[direction] != self.open:
                            if self.neighbors[direction] not in close_list:
                                directions.append(direction)

            # For each valid way, the algorithm calculate the cost (g_temp) of the actual path + the cost to get to the neighbor
            # Also calculate heuristic estimation (h_temp) of the neighbor in fonction of the exit and calculate the total cost (f_temp)
            # Check if the neighbor is in the begin_list or close_list 
            # If begin_list and new cost >= actual cost, go to next neighbor
            for direction in directions:
                g_temp = g[actual_cell] + 1
                h_temp = self.heuristic(self.neighbors[direction], end)
                f_temp = g_temp + h_temp

                if self.neighbors[direction] in begin_list:
                    if f_temp >= f[self.neighbors[direction]]:
                        continue
                if self.neighbors[direction] in close_list:
                    if f_temp >= f[self.neighbors[direction]]:
                        continue
                parent[self.neighbors[direction]] = actual_cell
                g[self.neighbors[direction]] = g_temp
                f[self.neighbors[direction]] = f_temp

                if self.neighbors[direction] in begin_list:
                    begin_list.remove(self.neighbors[direction])
                if self.neighbors[direction] in close_list:
                    close_list.remove(self.neighbors[direction])

                begin_list.append(self.neighbors[direction])
                self.print_maze()

    # Fonction to calculate the heuristic estimation 
    def heuristic(self, cell:tuple, end:tuple) -> int:
        heuris = abs(cell[0] - end[0]) + abs(cell[1] - end[1])
        return heuris
    
    def make_path(self, parent:dict, actual_cell:tuple) -> list:
        path = []

        while actual_cell in parent:
            path.append(actual_cell)
            actual_cell = parent[actual_cell]
        
        return path[::- 1]
    
def solve_maze(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    path = "mazes"
    full_path = os.path.join(script_dir, path, filename)
    print(full_path)

    if not os.path.exists(full_path):
        print(f"Le fichier {filename} n'existe pas.")
        return
    
    with open(full_path, 'r') as f:
        maze_data = [line.strip() for line in f.readlines()]

    maze_size = len(maze_data)
    maze = [[maze_data[row][col] for col in range(maze_size)] for row in range(maze_size)]

    solver = Solving(maze)

    start_time = time.time()
    # solver.backtrack_solver(solver.entrance)
    solver.astar()
    end_time = time.time()

    print(f"Résolution avec A* terminée en {end_time - start_time} secondes !")
    print(f"Résolution avec Backtracking terminée en {end_time - start_time} secondes !")

if __name__ == "__main__":
    filename = input("Entrez le nom du fichier du labyrinthe à résoudre (avec l'extension .txt) : ")
    solve_maze(filename)

