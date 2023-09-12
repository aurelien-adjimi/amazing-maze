import random
import time

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.wall = True
        self.set_id = x * self.size + y

class Maze:
    def __init__(self, size):
        self.size = size
        self.cells = [[Cell(x, y) for x in range(size)] for y in range(size)]
        self.maze = [['#' for _ in range(2 * size + 1)] for _ in range(2 * size + 1)]

    def is_valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def get_neighbors(self, x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        neighbors = [(x + dx, y + dy) for dx, dy in directions]
        return [(nx, ny) for nx, ny in neighbors if self.is_valid(nx, ny)]

    def kruskal_algorithm(self):
        edges = []

        for x in range(self.size):
            for y in range(self.size):
                edges.append((x, y))