from flask import Flask, render_template, request, jsonify, redirect, url_for

from packages.key_mapping import map_to_direction
from packages.logic import Snake
from packages.mongodb import initialize_database, store_game_result, dump_data_to_file

app = Flask(__name__)

game = None
name = None


@app.route('/')
def menu():
    initialize_database()
    return render_template('menu.html')


@app.route('/game', methods=['POST'])
def start_game():
    global game, name
    data = request.form
    name = data['name']
    grid_size = int(data['grid_size'])
    game = Snake(grid_size)
    return render_template('game.html', grid_size=grid_size, board=game.board)


@app.route('/game', methods=['GET'])
def restart_game():
    global game, name
    if game is None or name is None:
        return redirect(url_for("menu"))
    else:
        game = Snake(game.grid_size)
        return render_template('game.html', grid_size=game.grid_size, board=game.board)


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
    return jsonify({'status': status, 'board': game.board, 'score': game.score})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
