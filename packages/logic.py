import random
from collections import deque
from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def get_opposite(self):
        if self == Direction.UP:
            return Direction.DOWN
        if self == Direction.RIGHT:
            return Direction.LEFT
        if self == Direction.DOWN:
            return Direction.UP
        if self == Direction.LEFT:
            return Direction.RIGHT


class Snake:
    symbols = {'food': 'f', 'body': 'b', 'head': 'h'}

    def __init__(self, grid_size, generate_random_food=True, borderless=False):
        if grid_size < 5:
            raise ValueError("Grid size must be at least 5.")
        if grid_size > 25:
            raise ValueError("Grid size cannot exceed 25.")
        self.grid_size = grid_size
        self.board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        self.score = 0
        self.direction = Direction.RIGHT
        self.snake_deque = deque()
        self.snake_deque.append((grid_size // 2, grid_size // 2 - 2))
        self.snake_deque.append((grid_size // 2, grid_size // 2 - 1))
        self.snake_deque.append((grid_size // 2, grid_size // 2))
        for cell in self.snake_deque:
            self.board[cell[0]][cell[1]] = Snake.symbols['body']
        self.board[self.snake_deque[-1][0]][self.snake_deque[-1][1]] = Snake.symbols['head']
        if generate_random_food:
            self.generate_random_food()
        self.borderless = borderless

    def set_food(self, i, j):
        self.board[i][j] = Snake.symbols['food']

    def generate_random_food(self):
        num_free_cells = self.grid_size ** 2 - len(self.snake_deque)
        rand = random.randint(0, num_free_cells - 1)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.board[i][j] == '':
                    if rand == 0:
                        self.board[i][j] = Snake.symbols['food']
                        return True
                    rand -= 1
        return False

    def make_move(self, direction, generate_random_food=True):
        if not self.borderless:
            if self.check_wall_collision(direction):
                return 'wall_collision'
        if self.check_self_collision(direction):
            return 'self_collision'
        self.board[self.snake_deque[0][0]][self.snake_deque[0][1]] = ''
        previous_tail_pos = self.snake_deque.popleft()
        self.board[self.snake_deque[-1][0]][self.snake_deque[-1][1]] = Snake.symbols['body']
        if not self.borderless:
            previous_symbol = self.board[self.snake_deque[-1][0] + direction.value[0]][
                self.snake_deque[-1][1] + direction.value[1]]
            self.snake_deque.append(
                (self.snake_deque[-1][0] + direction.value[0], self.snake_deque[-1][1] + direction.value[1]))
        else:
            previous_symbol = self.board[(self.snake_deque[-1][0] + direction.value[0]) % self.grid_size][
                (self.snake_deque[-1][1] + direction.value[1]) % self.grid_size]
            self.snake_deque.append(
                ((self.snake_deque[-1][0] + direction.value[0]) % self.grid_size,
                 (self.snake_deque[-1][1] + direction.value[1]) % self.grid_size))
        self.board[self.snake_deque[-1][0]][self.snake_deque[-1][1]] = Snake.symbols['head']
        if previous_symbol == Snake.symbols['food']:
            self.snake_deque.appendleft(previous_tail_pos)
            self.board[self.snake_deque[0][0]][self.snake_deque[0][1]] = Snake.symbols['body']
            if generate_random_food:
                self.generate_random_food()
            self.score += 1
        self.direction = direction
        return 'success'

    def check_wall_collision(self, direction):
        return (self.snake_deque[-1][0] + direction.value[0] >= self.grid_size
                or self.snake_deque[-1][1] + direction.value[1] >= self.grid_size
                or self.snake_deque[-1][0] + direction.value[0] < 0
                or self.snake_deque[-1][1] + direction.value[1] < 0)

    def check_self_collision(self, direction):
        if not self.borderless:
            return (self.board[self.snake_deque[-1][0] + direction.value[0]][
                        self.snake_deque[-1][1] + direction.value[1]] == Snake.symbols['body']
                    and
                    (self.snake_deque[-1][0] + direction.value[0], self.snake_deque[-1][1] + direction.value[1]) !=
                    self.snake_deque[0])
        else:
            return (self.board[(self.snake_deque[-1][0] + direction.value[0]) % self.grid_size][
                (self.snake_deque[-1][1] + direction.value[1]) % self.grid_size] == Snake.symbols['body']
                and
                ((self.snake_deque[-1][0] + direction.value[0]) % self.grid_size,
                 (self.snake_deque[-1][1] + direction.value[1]) % self.grid_size)
                != self.snake_deque[0])
