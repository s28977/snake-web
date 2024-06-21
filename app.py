from flask import Flask, render_template, request, jsonify, redirect, url_for

from packages.key_mapping import map_to_direction
from packages.logic import Snake

app = Flask(__name__)

game = None
name = None


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/game', methods=['POST'])
def start_game():
    global game, name
    data = request.form
    name = data['name']
    size = int(data['size'])
    game = Snake(size)
    return render_template('game.html', grid_size=size, board=game.board)


@app.route('/game', methods=['GET'])
def restart_game():
    global game, name
    if game is None or name is None:
        print('here')
        return redirect(url_for(""))
    else:
        game = Snake(game.grid_size)
        return render_template('game.html', grid_size=game.grid_size, board=game.board)


@app.route('/make_move', methods=['POST'])
def make_move():
    global game, name
    data = request.json
    key = data['key']
    previous_direction = game.direction
    new_direction = map_to_direction(key)
    if new_direction is None or new_direction == previous_direction.get_opposite():
        new_direction = previous_direction
    status = game.make_move(new_direction)
    return jsonify({'status': status, 'board': game.board, 'score': game.score})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

