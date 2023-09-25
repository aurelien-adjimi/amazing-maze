import random
import time

# Class representing a cell. The class has 2 attributes: 
# 'visited' which is a boolean indicating if the cell have been visited. By default to False
# 'wall' which is also a boolean indicating if the cell has a wall. By default all cells have walls
class Cell:
    def __init__(self):
        self.visited = False
        self.wall = True

# Class representing the labytinth.
# __init__ is the constructor it takes 2 parameters: 'self' is the current instance of the class and size define the size of the maze
# 'self.size' assing size value to size attribute
# 'self.maze' create a two-dimensional matrix representing the labyrinth size
class Labyrinthe:
    def __init__(self, size):
        self.size = size
        self.maze = [['#' for _ in range(2 * size + 1)] for _ in range(2 * size + 1)]

# Method verifying if a peer of coordonate is in the limit of the maze
    def is_valid(self, x, y):
        return 0 <= x < 2 * self.size + 1 and 0 <= y < 2 * self.size + 1

# Method taking the coordinates x & y of a cell, mixing randomly the directions where the neighbors will be visited
# and generate the coordinates of the possible neighbors and return a list with the coordinates of the valid neighbors
    def get_neighbors(self, x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)] # Create the list with 4 tuples
        random.shuffle(directions)
        neighbors = [(x + dx, y + dy) for dx, dy in directions] # Create a list with neighbors coordinates
        return [(nx, ny) for nx, ny in neighbors if self.is_valid(nx, ny)] # Return a list of possible neighbors using 'is_valid' method

# initializes the maze generation process by setting the stack with the start cell (0, 0)
    def generate(self):
        stack = [(0, 0)]
        self.maze[0][0] = '.'

        while stack: # Loop that continues until the stack is empty.This stack is used to track the cells visited during maze generation.
            x, y = stack[-1] # Extracts the coordinates of the cell at the top of the stack. stack[-1] returns the last item in the stack, which represents the cell currently being explored.
            neighbors = self.get_neighbors(x, y) # Calls 'get_neighbors' method to get the valid neighbors of the current cell
            unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if self.is_valid(nx, ny) and self.maze[nx][ny] == '#'] # Create a unvisited neighbors list

            if unvisited_neighbors: # Checks if there are unvisited neighbors. If so, that means there are unexplored paths from the current cell.
                nx, ny = random.choice(unvisited_neighbors) # Chooses randomly one of the unvisited neighbors to explore. Ensures that the maze is randomly generated.
                wall_x = (x + nx) // 2 # Calculate the coordinates of the wall to remove between the current and the next cells. 
                wall_y = (y + ny) // 2
                self.maze[wall_x][wall_y] = '.' # Define the wall between current and next cells as a path.
                self.maze[nx][ny] = '.' # Define the next cell as visited 
                stack.append((nx, ny)) # Add the next cell on the stack because it will be the new cell for the next iteration
            else:
                stack.pop() # If none of the neighbors is unvisited, it unstack the stack by removing the current cell, go back and explore another possible path

# Check the last iteration
            if len(stack) == 1:
                last_x, last_y = stack[0]
                exit_candidates = []
            
            # Add the neighbors cells of the last cell
                if last_x > 0:
                    exit_candidates.append((last_x - 1, last_y))
                if last_x < 2 * self.size:
                    exit_candidates.append((last_x + 1, last_y))
                if last_y > 0:
                    exit_candidates.append((last_x, last_y - 1))
                if last_y < 2 * self.size:
                    exit_candidates.append((last_x, last_y + 1))

# Write the maze and read the grid, convert each string and write the lines
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.maze: # Runs the grid. Each lines is a string
                row_str = ''.join(row) # Convert the strings and concatenate every strings in one
                f.write(row_str + '\n')

def main():
# Inputs to interact with the user
    n = int(input("Entrez la taille du labyrinthe (un nombre entier naturel) : "))
    filename = input("Entrez le nom du fichier de sortie (avec l'extension .txt) : ")

    if n % 2 == 0:
        n += 1
    start = time.time()
    labyrinthe = Labyrinthe(n) # Create an instance of the class with n specified
    labyrinthe.generate() # Calls 'generate' method
    labyrinthe.save_to_file(filename) # Save the maze in the file
    end = time.time()
    elapsed = end - start
    print(f"Le labyrinthe a été généré et enregistré dans le fichier {filename} en {elapsed} secondes") 


    with open('log.txt', 'a') as log_file:
        log_file.write(f"The generation of the maze size {n}*{n} took {elapsed} seconds with Recursive Backtacking\n")

if __name__ == "__main__":
    main()
