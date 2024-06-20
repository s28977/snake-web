from flask import Flask, render_template

from packages.game import Snake

app = Flask(__name__)

game = Snake(10)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('game.html', grid_size=10)


if __name__ == '__main__':
    app.run()
