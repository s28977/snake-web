import random
from enum import Enum
from collections import deque


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Snake:
    def __init__(self, grid_size):
        if grid_size < 5:
            raise ValueError("Grid size must be at least 5.")
        if grid_size > 25:
            raise ValueError("Grid size cannot exceed 25.")
        self.board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        self.food_symbol = 'f'
        self.snake_symbol = 's'
        self.score = 0
        self.direction = Direction.RIGHT
        self.snake_deque = deque()
        self.snake_deque.append((grid_size // 2 - 2, grid_size // 2))
        self.snake_deque.append((grid_size // 2 - 1, grid_size // 2))
        self.snake_deque.append((grid_size // 2, grid_size // 2))
        for cell in self.snake_deque:
            self.board[cell[0]][cell[1]] = self.snake_symbol
        self.generate_random_food()

    def generate_food(self, x, y):
        pass

    def generate_random_food(self):
        pass

    def make_move(self, direction):
        if self.check_wall_collision(direction) is True:
            return 'Wall collision', self.score
        if self.check_self_collision(direction) is True:
            return 'Self collision', self.score
        self.snake_deque.append((self.snake_deque[0][0] + direction[0], self.snake_deque[0][1] + direction[1]))
        if self.check_food() is True:
            self.score += 1
        else:
            self.board[self.snake_deque[0][0]][self.snake_deque[0][1]] = ''
            self.snake_deque.popleft()
        self.board[self.snake_deque[-1][0] + direction[0]][self.snake_deque[-1][1] + direction[1]] = self.snake_symbol
        return 'Success', self.score

    def check_wall_collision(self, direction):
        return (self.snake_deque[-1][0] + direction[0] >= len(self.board)
                or self.snake_deque[-1][1] + direction[1] >= len(self.board)
                or self.snake_deque[-1][0] + direction[0] < 0
                or self.snake_deque[-1][1] + direction[1] < 0)

    def check_self_collision(self, direction):
        return self.board[self.snake_deque[-1][0] + direction[0]][
            self.snake_deque[-1][1] + direction[1]] == self.snake_symbol

    def check_food(self):
        return self.board[self.snake_deque[-1][0]][self.snake_deque[-1][1]] == self.food_symbol
