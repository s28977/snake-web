# Snake Game by Jan Musiał (s28977)

This is a simple browser-based Snake game implemented in Python using Flask and MongoDB.

## How to install and run

To install and run the game locally on your machine, you need to have Docker application installed and running locally on your machine.

1. Clone or download this repository to your local machine.

2. Navigate to the project directory.

3. Run this command in project directory:

```
docker compose up -d 
```

4. Open a web browser and navigate to http://localhost:5000 to play the game.

5. After closing the game, run this command in project directory to stop the game:

```
docker compose stop
```

6. If you want to play again you can run this command, and the game will launch way faster, because it is already installed:

```
docker compose start
```

7. If you want to delete the game run this command in project directory:

```
docker compose down --rmi all
```
