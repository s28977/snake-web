import msvcrt
import sys
import time
from game import Snake, Direction


def get_direction(char):
    if char == 'w':
        return Direction.UP
    if char == 's':
        return Direction.DOWN
    if char == 'd':
        return Direction.RIGHT
    if char == 'a':
        return Direction.LEFT


def is_correct_key(char):
    return char == 'w' or char == 's' or char == 'd' or char == 'a'


def print_game(game):
    print(f'Score: {game.score}')
    print('|', end='')
    print(2 * len(game.board) * '-', end='')
    print('|')
    for row in game.board:
        print('|', end='')
        for cell in row:
            if cell == '':
                print(' ', end=' ')
            if cell == game.snake_symbol:
                print(game.snake_symbol, end=' ')
            if cell == game.food_symbol:
                print(game.food_symbol, end=' ')
        print('|')
    print('|', end='')
    print(2 * len(game.board) * '-', end='')
    print('|')

while True:
    print('Use wsad to move')
    time.sleep(2)
    game = Snake(10)
    print_game(game)
    while True:
        time.sleep(1)
        direction = game.direction
        if msvcrt.kbhit():
            while msvcrt.kbhit():
                char = msvcrt.getch()
            if char.islower():
                char = char.decode()
            if char == 'q':
                sys.exit(0)
            if is_correct_key(char):
                if get_direction(char) != direction.get_opposite():
                    direction = get_direction(char)
        status = game.make_move(direction)
        if status == 'wall_collision' or status == 'self_collision':
            print(f'You lost! Score: {game.score}')
            break
        print_game(game)
    char = input('Play again? [y/n]\n')
    while char != 'y' and char != 'n':
        char = input('Play again? [y/n]\n')
    if char == 'n':
        break
