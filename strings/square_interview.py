# You're going to build a game named Zendo.

# The game is played over a series of rounds. In each round, you will be given one or more game pieces and a rule.

# Your task will be to determine if the game pieces follow the rule.

# Each game piece will have a color and a size. The possible colors and sizes are
# colors: red, blue, green
# sizes: small, medium, large

# You can represent the game pieces and rules using any data structures you’d like.

# Round: 1
# pieces: one large red piece and one small blue piece
# rule: exactly one large red piece
# result: pass

# Round: 2
# pieces: two large red pieces
# rule: exactly one large red piece
# result: fail

# Round: 3
# pieces: two small blue pieces and one small red piece
# rule: less than three small blue pieces
# result: pass

# Round: 4
# pieces: one medium green, one medium red, one small blue
# rule: greater than one medium piece of any color
# result: pass

# Round: 5
# pieces: one large blue, one medium green, one small green
# rule: exactly two non-red pieces
# result: fail




# import requests
# import mysql.connector
# import pandas as pd


class GamePiece:

    def __init__(self, size, color):
        self.size = size
        self.color = color

def isGood(game_pieces, comp, num, size, color, color_valid=True):
    
    counter = 0
    for piece in game_pieces:
        if (color == "any" or piece.color == color)== color_valid and piece.size == size:
            counter += 1
    # eval(1==1)
    return eval(f"{counter}{comp}{num}")
    
if __name__ == "__main__":
    # pieces: one large red piece and one small blue piece
    # rule: exactly one large red piece 
    # result: pass
    game_pieces = [GamePiece("large", "red"), GamePiece("small", "blue")]
    print(isGood(game_pieces, "==", 1, "large", "red"))
    
    # pieces: two large red pieces
    # rule: exactly one large red piece
    # result: fail
    game_pieces = [GamePiece("large", "red"), GamePiece("large", "red")]
    print(isGood(game_pieces, "==", 1, "large", "red"))

    # pieces: two small blue pieces and one small red piece
    # rule: less than three small blue pieces
    # result: pass
    game_pieces = [GamePiece("small", "red"), GamePiece("small", "blue"), GamePiece("small", "blue")]
    print(isGood(game_pieces, "<", 3, "small", "blue"))
    
    # pieces: one medium green, one medium red, one small blue
    # rule: greater than one medium piece of any color
    # result: pass
    game_pieces = [GamePiece("medium", "green"), GamePiece("medium", "red"), GamePiece("small", "blue")]
    print(isGood(game_pieces, ">", 1, "medium", "any"))
    
    # pieces: one large blue, one medium green, one small green
    # rule: exactly two non-red pieces
    # result: fail
    game_pieces = [GamePiece("large", "blue"), GamePiece("medium", "green"), GamePiece("small", "green")]
    print(isGood(game_pieces, "==", 2, "medium", "red", False))