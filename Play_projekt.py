from TheGame_projekt import Game
from ThePlayer_projekt import HumanPlayer
from ThePossibilities_projekt import PossibleMoves


class PlayGame:
    """
    Class PlayGame. Contains attributes:

    :param user_player: Stores the first player's avatar.
    By name it is for the user, in the simulation mode it's used by the computer.
    :type user_player: boole

    :param comp_player: Stores the second player's avatar.
    By name it is for the computer, and it remains so in the simulation mode.
    :type player: boole

    :param turn: Stores the information of who moves the pieces in the current round.
    :type turn: int

    :param turn_count: Stores the number of the current round.
    Incremented with every round.
    :type turn_count: int

    :param neutron_position: Stores the cooefficients of the Neutron.
    :type neutron_position: tuple
    """

    def __init__(
            self, game=None,
            user_player=None, comp_player=None,
            turn=0, turn_count=1,
            neutron_position=(2, 2)
            ):
        """Constructor method"""
        self.game = game
        self.user_player = user_player
        self.comp_player = comp_player
        self.turn = turn
        self.turn_count = turn_count
        self.neutron_position = neutron_position

    def the_current_turn(self):
        """
        Sets the turn attribute depending on what the attribute was previously.
        """
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0
        return self.turn

    def play(self, cplayer):
        """
        The actual duel happens because of this method.
        The user's and computer's objects are created when the method is called.
        The computer player responds with a Neutron move to the regular move of the user player.
        The user player responds with a Neutron move to the regular move of the computer player.
        With each round the winning criteria are evaluated.
        The method evaluates final results when winning is detected, then stops.
        """
        self.user_player = HumanPlayer()
        self.comp_player = cplayer
        self.game = Game()
        print(self.game.the_display())
        while self.check_winner(self.game.display) is False:
            self.the_current_turn()
            if self.turn == 1:
                print(f"ROUND {self.turn_count}")
                print("THIS IS WHITE'S TURN")
                # the regular piece move of the user
                p_place, direction = self.user_player.move_reg(self.game.display)
                r, c = self.game.move_the_pieces(p_place, direction, self.user_player.color)
                for i in range(len(self.user_player.p_places)):
                    if self.user_player.p_places[i] == p_place:
                        self.user_player.p_places[i] = (r, c)
                print(f"{self.user_player.color} moved to row {r+1} column {c+1}")

                if self.check_winner(self.game.display) is False:
                    # the neutron move of the computer
                    print("BLACK SHALL MOVE THE NEUTRON")
                    p_place = self.neutron_position
                    direction = self.comp_player.move_n(self.neutron_position, self.game.display)
                    r, c = self.game.move_the_pieces(self.neutron_position, direction, "N")
                    self.neutron_position = (r, c)
                    print(f"The Neutron moved to row {r+1} column {c+1}")
                    self.turn_count += 1
                else:
                    pass

            elif self.turn == 0:
                print(f"ROUND {self.turn_count}")
                print("THIS IS BLACK'S TURN")
                # the regular piece move of the computer
                p_place, direction = self.comp_player.move_reg(self.game.display)
                r, c = self.game.move_the_pieces(p_place, direction, self.comp_player.color)
                for i in range(len(self.comp_player.p_places)):
                    if self.comp_player.p_places[i] == p_place:
                        self.comp_player.p_places[i] = (r, c)
                print(f"{self.comp_player.color} moved to column {r+1} row {c+1}")

                if self.check_winner(self.game.display) is False:
                    # the neutron move of the user
                    print("WHITE SHALL MOVE THE NEUTRON")
                    direction = self.user_player.move_n(self.neutron_position, self.game.display)
                    r, c = self.game.move_the_pieces(self.neutron_position, direction, "N")
                    self.neutron_position = (r, c)
                    print(f"The Neutron moved to row {r+1} column {c+1}")
                    self.turn_count += 1
                else:
                    pass

        self.evaluate_result(self.game.display)

    def simulation(self, cplayer1, cplayer2):
        """
        The simulation of the duel happens because of this method.
        The computer players' objects are created when the method is called.
        The second player responds with a Neutron move to the regular move of the first player.
        The first player responds with a Neutron move to the regular move of the second player.
        With each round the winning criteria are evaluated.
        The method evaluates final results when winning is detected, then stops.
        """
        self.user_player = cplayer1
        self.comp_player = cplayer2
        self.game = Game()
        print(self.game.the_display())
        while self.check_winner(self.game.display) is False:
            self.the_current_turn()
            if self.turn == 1:
                print(f"ROUND {self.turn_count}")
                print("THIS IS THE FIRST COMPUTER'S TURN")
                # the regular piece move of the COMP1
                p_place, direction = self.user_player.move_reg(self.game.display)
                r, c = self.game.move_the_pieces(p_place, direction, self.user_player.color)
                for i in range(len(self.user_player.p_places)):
                    if self.user_player.p_places[i] == p_place:
                        self.user_player.p_places[i] = (r, c)
                print(f"{self.user_player.color} moved to row {r+1} column {c+1}")

                if self.check_winner(self.game.display) is False:
                    # the neutron move of the COMP2
                    print("THE SECOND COMPUTER SHALL MOVE THE NEUTRON")
                    p_place = self.neutron_position
                    direction = self.comp_player.move_n(self.neutron_position, self.game.display)
                    r, c = self.game.move_the_pieces(self.neutron_position, direction, "N")
                    self.neutron_position = (r, c)
                    print(f"The Neutron moved to row {r+1} column {c+1}")
                    self.turn_count += 1
                else:
                    pass

            elif self.turn == 0:
                print(f"ROUND {self.turn_count}")
                print("THIS IS THE SECOND COMPUTER'S TURN")
                # the regular piece move of the COMP2
                p_place, direction = self.comp_player.move_reg(self.game.display)
                r, c = self.game.move_the_pieces(p_place, direction, self.comp_player.color)
                for i in range(len(self.comp_player.p_places)):
                    if self.comp_player.p_places[i] == p_place:
                        self.comp_player.p_places[i] = (r, c)
                print(f"{self.comp_player.color} moved to row {r+1} column {c+1}")

                if self.check_winner(self.game.display) is False:
                    # the neutron move of the COMP1
                    print("THE FIRST COMPUTER SHALL MOVE THE NEUTRON")
                    direction = self.user_player.move_n(self.neutron_position, self.game.display)
                    r, c = self.game.move_the_pieces(self.neutron_position, direction, "N")
                    self.neutron_position = (r, c)
                    print(f"The Neutron moved to row {r+1} column {c+1}")
                    self.turn_count += 1
                else:
                    pass

        self.evaluate_result_sim(self.game.display)

    def check_winner(self, display):
        """Detects winning."""
        n_pos = PossibleMoves().generate_possibilities(self.neutron_position, display)
        if (
            self.neutron_position[0] == 0
            or self.neutron_position[0] == 4
            or self.user_player.p_places == 0
            or self.comp_player.p_places == 4
            or len(n_pos) == 0
                ):
            return True
        else:
            return False

    def evaluate_result_sim(self, display):
        """
        Evaluates who the winner is in the simulation mode.
        In case of no option to move the Neutron, both computer players are winners.
        """
        user_base = [place[0] for place in self.user_player.p_places]
        comp_base = [place[0] for place in self.comp_player.p_places]
        n_pos = PossibleMoves().generate_possibilities(self.neutron_position, display)

        if (
            self.neutron_position[0] == 4
            or
            user_base == [0, 0, 0, 0, 0]
                ):
            print("THE FIRST COMPUTER HAS WON")
        elif (
            self.neutron_position[0] == 0
            or
            comp_base == [4, 4, 4, 4, 4]
                ):
            print("THE SECOND COMPUTER HAS WON")
        elif len(n_pos) == 0:
            print("BOTH COMPUTERS ARE WINNERS. THE NEUTRON HAS SURRENDERED")

    def evaluate_result(self, display):
        """
        Evaluates who the winner of the duel is.
        In case of no option to move the Neutron, both players are winners.
        """
        user_base = [place[0] for place in self.user_player.p_places]
        comp_base = [place[0] for place in self.comp_player.p_places]
        n_pos = PossibleMoves().generate_possibilities(self.neutron_position, display)

        if (
            self.neutron_position[0] == 4
            or
            user_base == [0, 0, 0, 0, 0]
                ):
            print("THE KING OF WHITE PIECES HAS WON")
        elif (
            self.neutron_position[0] == 0
            or
            comp_base == [4, 4, 4, 4, 4]
                ):
            print("THE KING OF BLACK PIECES HAS WON")
        elif len(n_pos) == 0:
            print("BOTH PLAYERS ARE WINNERS. THE NEUTRON HAS SURRENDERED")
