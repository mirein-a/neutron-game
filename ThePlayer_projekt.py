from ThePossibilities_projekt import PossibleMoves
from random import choice


class HumanPlayer:
    """
    Class HumanPlayer. Contains attributes:

    :param p_places: Stores the places of the pieces previous to the current move.
    :type p_places: list

    :param color: Stores the default set of the pieces played by the player.
    :type color: str
    """
    def __init__(self, p_places=[], color="W"):
        """Constructor method"""
        self.p_places = p_places
        self.color = color
        if p_places == []:
            self.p_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    def move_reg(self, display):
        """
        Interacts with the user
        in order to choose the move of the regular piece.
        Calls other methods to ensure that the move is valid.
        """
        for i in range(5):
            print(f"{i+1}. {self.p_places[i]}")
        x = 0
        y = 0
        while x not in range(1, 6):
            x = int(input("choose the piece you want to move, by number, from listed above: "))

        pos_dir = PossibleMoves().generate_possibilities(self.p_places[x-1], display)
        while len(pos_dir) == 0:
            for i in range(5):
                print(f"{i+1}. {self.p_places[i]}")
            x = int(input("this piece cannot be moved, choose a different one (1-5): "))
            pos_dir = PossibleMoves().generate_possibilities(self.p_places[x-1], display)
        for i in range(len(pos_dir)):
            print(f"{i+1}. {pos_dir[i]}")
        while y not in range(1, len(pos_dir)+1):
            y = int(input("choose the direction by number, from listed above: "))

        return self.p_places[x-1], pos_dir[y-1]
        # tuple and str -> p_place and direction

    def move_n(self, n_p, display):
        """
        Interacts with the user
        in order to choose the move of the Neutron.
        Calls other methods to ensure that the move is valid.
        """
        pos_dir = PossibleMoves().generate_possibilities(n_p, display)
        for i in range(len(pos_dir)):
            print(f"{i+1}. {pos_dir[i]}")
        n = 0
        while n not in range(1, len(pos_dir)+1):
            n = int(input("choose the direction for The Neutron, by number, from listed above: "))

        return pos_dir[n-1]


class RandomCompPlayer:
    """
    Class RandomCompPlayer. Contains attributes:

    :param p_places: Stores the places of the pieces previous to the current move.
    :type p_places: list

    :param color: Stores the default color played by the computer.
    :type color: str
    """
    def __init__(self, p_places=[], color="B"):
        """Constructor method"""
        self.p_places = p_places
        self.color = color
        if p_places == []:
            self.p_places = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]

    def move_reg(self, display):
        """
        Chooses the move randomly.
        Calls other methods to ensure the move is valid.
        """
        pos_dir = []

        while len(pos_dir) == 0:
            x = choice(self.p_places)
            pos_dir = PossibleMoves().generate_possibilities(x, display)

        y = choice(pos_dir)

        return x, y

    def move_n(self, n_p, display):
        """
        Chooses the move for the Neutron randomly.
        Calls other methods to ensure the move is valid.
        """
        return choice(PossibleMoves().generate_possibilities(n_p, display))


class OkComputer(RandomCompPlayer):
    """
    Class OkComputer, subclass of RandomCompPlayer.
    Contains attributes:

    :param color: Stores the default color played by the computer.
    :type color: str

    :param p_places: Stores the places of the pieces previous to the current move.
    :type p_places: list

    :param i: Stores a number used in making non-random choices.
    Ranges from 0 to 5
    :type i: int

    :param j: Stores a number used in making non-random choices.
    Is set after the length of the list of the possible moves of the regular piece is known
    :type j: int

    :param k: Stores a number used in making non-random choices.
    Is set after the length of the list of the possible moves of the Neutron is known
    :type k: int
    """

    def __init__(self, color="B", p_places=[], i=0, j=0, k=0):
        """Constructor method"""
        super().__init__(color="B", p_places=[])
        self.i = i
        self.j = j
        self.k = k

    def move_reg(self, display):
        """
        Depends on the attribute i when choosing the piece.
        The attribute i is incremented with every method call.
        Depends on the attribute j when choosing the direction of the move.
        The attribute j is the length of the possible-moves list divided by 2, with the remainder
        """
        pos_dir = []

        while len(pos_dir) == 0:
            x = self.p_places[self.i]
            pos_dir = PossibleMoves().generate_possibilities(x, display)
            if self.i < 4:
                self.i += 1
            else:
                self.i = 0

        self.j = len(pos_dir)//2
        y = pos_dir[self.j]

        return x, y

    def move_n(self, n_p, display):
        """
        Depends on the attribute k when choosing the direction of the move for the Neutron.
        The attribute k is the length of the possible-moves list divided by 2, with the remainder
        """
        pos = PossibleMoves().generate_possibilities(n_p, display)
        self.k = len(pos)//2
        return pos[self.k]
