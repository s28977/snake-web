from packages.logic import Direction


def map_to_direction(key):
    match key:
        case "ArrowDown" | "s" | "S":
            direction = Direction.DOWN
        case "ArrowUp" | "w" | "W":
            direction = Direction.UP
        case "ArrowRight" | "d" | "D":
            direction = Direction.RIGHT
        case "ArrowLeft" | "a" | "A":
            direction = Direction.LEFT
        case _:
            direction = None
    return direction
