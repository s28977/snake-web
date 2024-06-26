from flask import Flask, render_template, request, jsonify, redirect, url_for

from packages.direction_dto_mapping import map_to_direction
from packages.logic import Snake
from packages.mongodb import initialize_database, store_game_result, dump_data_to_file, get_leaderboard_list

app = Flask(__name__)

game = None
name = None


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/setup')
def game_setup():
    return render_template('setup.html')


@app.route('/game', methods=['POST'])
def start_game():
    global game, name
    data = request.form
    name = data['name']
    grid_size = int(data['grid_size'])
    game = Snake(grid_size)
    initial_timeout = int(1000 / game.initial_speed)  # timeout between moves in milliseconds
    return render_template('game.html', grid_size=grid_size, board=game.board, symbols=Snake.symbols,
                           initial_timeout=initial_timeout)


@app.route('/game', methods=['GET'])
def restart_game():
    global game, name
    if game is None or name is None:
        return redirect(url_for("menu"))
    else:
        game = Snake(game.grid_size)
        initial_timeout = int(1000 / game.initial_speed)  # timeout between moves in milliseconds
        return render_template('game.html', grid_size=game.grid_size, board=game.board, symbols=Snake.symbols,
                               initial_timeout=initial_timeout)


@app.route('/make_move', methods=['POST'])
def make_move():
    global game, name
    if not game:
        return jsonify({'error': 'Game has not been initialized.'}), 500
    data = request.json
    key = data['key']
    previous_direction = game.direction
    new_direction = map_to_direction(key)
    if new_direction is None or new_direction == previous_direction.get_opposite():
        new_direction = previous_direction
    status = game.make_move(new_direction)
    if status == "self_collision" or status == "wall_collision":
        store_game_result(name, game.grid_size, game.score)
        dump_data_to_file('db/data.json')
    timeout = int(1000 / game.speed)  # timeout between moves in milliseconds
    return jsonify({'status': status, 'board': game.board, 'score': game.score, 'timeout': timeout})


@app.route('/leaderboard')
def leaderboard():
    leaderboard_list = get_leaderboard_list()
    return render_template('leaderboard.html', leaderboard_list=leaderboard_list)


if __name__ == '__main__':
    initialize_database()  # Initialize the database if necessary
    app.run(debug=True, host='0.0.0.0')
