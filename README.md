# Snake Web Game

This is a simple browser-based Snake game implemented in Python using Flask and MongoDB.

## How to install the game
 
To install and run the game locally on your machine, **you need to have Docker application** installed and running locally on your machine. **Thanks to the magic of Docker, you don't need to have installed anything else (e.g. Python) other then Docker and your favourite web browser**.

1. Clone or download this repository to your local machine.

2. Navigate to the project directory.

3. Run this command from project directory:

```
docker compose create --build 
```

## How to locally run the game in the web

1. Run this command from project directory:

```
docker compose start 
```

2. Open a web browser and navigate to http://localhost:5000 to play the game.

## How to shut down the game

Run this command from project directory:

```
docker compose stop
```

## How to delete the game

Run this command from project directory:

```
docker compose down --rmi all
```
