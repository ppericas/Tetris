# names of different game pieces
tetrominos: list[str] = ['I', 'O', 'T', 'J', 'L', 'S', 'Z']

# shape layouts
I: list[list[list[int]]] = [
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0]],
    [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
]

O: list[list[list[int]]] = [
    [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]
]

T: list[list[list[int]]] = [
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[0, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]]
]

J: list[list[list[int]]] = [
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0]],
    [[1, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    [[0, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]]
]

L: list[list[list[int]]] = [
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]],
    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0]],
    [[1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
    [[0, 0, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
]

S: list[list[list[int]]] = [
    [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0]],
    [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]]
]

Z: list[list[list[int]]] = [
    [[0, 0, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0]]
]

shapes: dict[str, list[list[list[int]]]] = {
    'I': I,
    'O': O,
    'T': T,
    'J': J,
    'L': L,
    'S': S,
    'Z': Z
}


# rgb color values for the game pieces
red: tuple[int] = (255, 0, 0)
yellow: tuple[int] = (255, 255, 0)
purple: tuple[int] = (148, 0, 211)
green: tuple[int] = (0, 255, 0)
blue: tuple[int] = (0, 0, 255)
cyan: tuple[int] = (0, 255, 255)
orange: tuple[int] = (255, 165, 0)

colors: dict[str, tuple[int]] = {
    'I': cyan,
    'O': yellow,
    'T': purple,
    'J': blue,
    'L': orange,
    'S': green,
    'Z': red
}