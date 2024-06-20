from flask import Flask, render_template

from packages.game import Snake

app = Flask(__name__)

game = Snake(10)


@app.route('/')
def start_game():  # put application's code here
    global game
    return render_template('game.html', grid_size=10, board=game.board)

# @app.route('/make_move', methods=['POST'])
# def make_move():
#     global game
#     data = request.json
#     key = data['key']

if __name__ == '__main__':
    app.run()
