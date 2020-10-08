

class PossibleMoves:
    """
    Class PossibleMoves. Contains an attribute:

    :param possibilities: Stores the possible moves of the chosen piece,
    in the chosen direction
    :type possibilities: list
    """
    directions = {
        1: "down",
        2: "up",
        3: "right",
        4: "left",
        5: "diagonal down right",
        6: "diagonal down left",
        7: "diagonal up right",
        8: "diagonal up left"
        }

    def __init__(self, possibilities=[]):
        """Constructor method"""
        self.possibilities = possibilities

    def check_move(self, direction, p_place, display):
        """
        Checks if the attribute directions contains the chosen direction,
        if the move of a certain piece in said direction is valid.
        Handles exceptions.
        """
        r, c = p_place[0], p_place[1]
        # DOWN
        try:
            if (
                direction == PossibleMoves.directions[1]
                and display[r+1][c] == " "
                and r+1 <= 4
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # UP
        try:
            if (
                direction == PossibleMoves.directions[2]
                and display[r-1][c] == " "
                and r-1 >= 0
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # RIGHT
        try:
            if (
                direction == PossibleMoves.directions[3]
                and display[r][c+1] == " "
                and c+1 <= 4
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # LEFT
        try:
            if (
                direction == PossibleMoves.directions[4]
                and display[r][c-1] == " "
                and c-1 >= 0
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # DIGONALLY DOWN RIGHT
        try:
            if (
                direction == PossibleMoves.directions[5]
                and display[r+1][c+1] == " "
                and r+1 <= 4
                and c+1 <= 4
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # DIAGONALLY DOWN LEFT
        try:
            if (
                direction == PossibleMoves.directions[6]
                and display[r+1][c-1] == " "
                and r+1 <= 4
                and c-1 >= 0
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # DIAGONALLY UP RIGHT
        try:
            if (
                direction == PossibleMoves.directions[7]
                and display[r-1][c+1] == " "
                and r-1 >= 0
                and c+1 <= 4
                    ):
                return True
            else:
                pass
        except IndexError:
            pass
        # DIAGONALLY UP LEFT
        try:
            if (
                direction == PossibleMoves.directions[8]
                and display[r-1][c-1] == " "
                and r-1 >= 0
                and c-1 >= 0
                    ):
                return True
            else:
                pass
        except IndexError:
            pass

    def generate_possibilities(self, p_place, display):
        """
        Calls the cheking method.
        Returns a list of valid moves for a certain piece
        """
        self.possibilities = []
        r, c = p_place[0], p_place[1]
        for val in PossibleMoves.directions.values():
            if self.check_move(val, (r, c), display) is True:
                self.possibilities.append(val)
        return self.possibilities
