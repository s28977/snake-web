import pytest
from packages.logic import Snake, Direction


# Test for checking correct size of the board
def test_correct_grid_size():
    grid_size = 10
    game = Snake(grid_size)
    assert len(game.board) == grid_size
    assert len(game.board[0]) == grid_size


# Test for checking incorrect size of the board
def test_incorrect_grid_size():
    grid_size = 3
    with pytest.raises(ValueError):
        Snake(grid_size)


# Test for checking initial snake position
def test_initial_snake_position():
    grid_size = 10
    game = Snake(grid_size)
    assert game.board[grid_size // 2][grid_size // 2 - 2] == game.snake_symbol
    assert game.board[grid_size // 2][grid_size // 2 - 1] == game.snake_symbol
    assert game.board[grid_size // 2][grid_size // 2] == game.snake_symbol


# Test for checking head and tail position after move
def test_snake_position_after_move():
    grid_size = 10
    game = Snake(grid_size)
    game.make_move(Direction.UP)
    assert game.board[grid_size // 2][grid_size // 2 - 1] == game.snake_symbol
    assert game.board[grid_size // 2][grid_size // 2] == game.snake_symbol
    assert game.board[grid_size // 2 - 1][grid_size // 2] == game.snake_symbol


# Test for checking detection of wall collision when it should happen
def test_wall_collision():
    grid_size = 5
    game = Snake(grid_size)
    game.make_move(Direction.RIGHT)
    game.make_move(Direction.RIGHT)
    assert game.check_wall_collision(Direction.RIGHT) is True


# Test for checking detection of wall collision when it shouldn't happen
def test_no_wall_collision():
    grid_size = 5
    game = Snake(grid_size)
    assert game.check_wall_collision(Direction.RIGHT) is False


# Test for checking if food gets generated

def test_food_exists_after_generate_random_food():
    grid_size = 10
    game = Snake(grid_size)
    is_food = 0
    for row in game.board:
        for el in row:
            if el == game.food_symbol:
                is_food += 1
    assert is_food == 1


# Test for checking if correct direction after move
def test_direction_switch_after_move():
    grid_size = 10
    game = Snake(grid_size)
    game.make_move(Direction.UP)
    assert game.direction == Direction.UP


def test_snake_len_after_eating():
    grid_size = 10
    game = Snake(grid_size)
    game.set_food(grid_size // 2, grid_size // 2 + 1)
    game.set_food(grid_size // 2 - 1, grid_size // 2 + 1)
    game.make_move(Direction.RIGHT)
    game.make_move(Direction.UP)
    snake_len = 0
    for row in game.board:
        for el in row:
            if el == game.snake_symbol:
                snake_len += 1
    assert snake_len == 5


def test_self_collision():
    grid_size = 10
    game = Snake(grid_size)
    game.set_food(grid_size // 2, grid_size // 2 + 1)
    game.set_food(grid_size // 2, grid_size // + 2)
    game.make_move(Direction.RIGHT)
    game.make_move(Direction.RIGHT)
    game.make_move(Direction.UP)
    game.make_move(Direction.LEFT)
    assert game.check_self_collision(Direction.DOWN) is True


def test_no_self_collision():
    grid_size = 10
    game = Snake(grid_size)
    assert game.check_self_collision(Direction.RIGHT) is False


# Test for checking if snake has len=4 and spins in circle, collision won't be detected because
def test_no_circular_self_collision():
    grid_size = 10
    game = Snake(grid_size)
    game.set_food(grid_size // 2, grid_size // 2 + 1)
    game.make_move(Direction.RIGHT)
    game.make_move(Direction.UP)
    game.make_move(Direction.LEFT)
    assert game.make_move(Direction.DOWN) == 'success'
