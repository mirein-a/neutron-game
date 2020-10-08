

class Game:
    """
    Class Game. Contains an attribute:

    :param display:
    Stores the starting default display of the pieces on the board.
    :type display: list
    """
    def __init__(self, display=[]):
        """Constructor method"""
        display = [
            ["B", "B", "B", "B", "B"],
            [" ", " ", " ", " ", " "],
            [" ", " ", "N", " ", " "],
            [" ", " ", " ", " ", " "],
            ["W", "W", "W", "W", "W"]
        ]
        self.display = display

    def the_display(self):
        """Prints out what the board currently looks like"""
        return f"""
        {self.display[0]}\n
        {self.display[1]}\n
        {self.display[2]}\n
        {self.display[3]}\n
        {self.display[4]}\n
        """

    def move_horizontally(self, p_place, direction, color):
        """the rules for moving the pieces horizontally"""
        r, c = p_place[0], p_place[1]
        self.display[r][c] = " "
        if direction == "right":
            while c <= 4 and self.display[r][c] == " ":
                c += 1
            if c > 4 or self.display[r][c] != " ":
                c -= 1
        elif direction == "left":
            while c >= 0 and self.display[r][c] == " ":
                c -= 1
            if c < 0 or self.display[r][c] != " ":
                c += 1
        self.display[r][c] = color
        print(self.the_display())
        return r, c

    def move_vertically(self, p_place, direction, color):
        """the rules for moving the pieces vertically"""
        r, c = p_place[0], p_place[1]
        self.display[r][c] = " "
        if direction == "down":
            while r <= 4 and self.display[r][c] == " ":
                r += 1
            if r > 4 or self.display[r][c] != " ":
                r -= 1
        elif direction == "up":
            while r >= 0 and self.display[r][c] == " ":
                r -= 1
            if r < 0 or self.display[r][c] != " ":
                r += 1
        self.display[r][c] = color
        print(self.the_display())
        return r, c

    def move_diagonally(self, p_place, direction, color):
        """the rules for moving the pieces diagonally"""
        r, c = p_place[0], p_place[1]
        self.display[r][c] = " "
        if direction == "diagonal down right":
            while c <= 4 and r <= 4 and self.display[r][c] == " ":
                c += 1
                r += 1
            if c > 4 or r > 4 or self.display[r][c] != " ":
                c -= 1
                r -= 1
        elif direction == "diagonal down left":
            while c >= 0 and r <= 4 and self.display[r][c] == " ":
                c -= 1
                r += 1
            if c < 0 or r > 4 or self.display[r][c] != " ":
                c += 1
                r -= 1
        elif direction == "diagonal up right":
            while c <= 4 and r >= 0 and self.display[r][c] == " ":
                c += 1
                r -= 1
            if c > 4 or r < 1 or self.display[r][c] != " ":
                c -= 1
                r += 1
        elif direction == "diagonal up left":
            while c >= 0 and r >= 0 and self.display[r][c] == " ":
                c -= 1
                r -= 1
            if c < 0 or r < 1 or self.display[r][c] != " ":
                c += 1
                r += 1
        self.display[r][c] = color
        print(self.the_display())
        return r, c

    def move_the_pieces(self, p_place, direction, color):
        """
        All possible directions in one method.
        This method calls other methods for the rules of moving the pieces
        """
        if direction == "down":
            return self.move_vertically(p_place, "down", color)
        elif direction == "up":
            return self.move_vertically(p_place, "up", color)
        elif direction == "right":
            return self.move_horizontally(p_place, "right", color)
        elif direction == "left":
            return self.move_horizontally(p_place, "left", color)
        elif direction == "diagonal down right":
            return self.move_diagonally(p_place, "diagonal down right", color)
        elif direction == "diagonal down left":
            return self.move_diagonally(p_place, "diagonal down left", color)
        elif direction == "diagonal up right":
            return self.move_diagonally(p_place, "diagonal up right", color)
        else:
            return self.move_diagonally(p_place, "diagonal up left", color)
