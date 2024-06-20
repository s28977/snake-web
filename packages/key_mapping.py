from packages.logic import Direction


def map_to_direction(key):
    match key:
        case "ArrowDown" | "s":
            direction = Direction.DOWN
        case "ArrowUp" | "w":
            direction = Direction.UP
        case "ArrowRight" | "d":
            direction = Direction.RIGHT
        case "ArrowLeft" | "a":
            direction = Direction.LEFT
        case _:
            direction = None
    return direction
