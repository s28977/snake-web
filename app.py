from flask import Flask, render_template, request, jsonify

from packages.key_mapping import map_to_direction
from packages.logic import Snake

app = Flask(__name__)

game = Snake(10)


@app.route('/')
def start_game():  # put application's code here
    global game
    return render_template('game.html', grid_size=10, board=game.board)


@app.route('/make_move', methods=['POST'])
def make_move():
    global game
    data = request.json
    key = data['key']
    previous_direction = game.direction
    new_direction = map_to_direction(key)
    if new_direction is None or new_direction == previous_direction.get_opposite():
        new_direction = previous_direction
    status = game.make_move(new_direction)
    return jsonify({'status': status, 'board': game.board, 'score': game.score})


if __name__ == '__main__':
    app.run()
