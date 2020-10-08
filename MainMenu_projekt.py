from Play_projekt import PlayGame
from ThePlayer_projekt import RandomCompPlayer, OkComputer, HumanPlayer


if __name__ == "__main__":
    print(
        """
        MENU\n
        1. play
        2. watch a simulation
        3. quit
        """
    )
    chosen1 = int(input("option: "))

    while chosen1 == 1:
        print(
            """
            1. Random Computer Player
            2. Ok Computer Player
            3. a fight between two users
            """
        )
        chosen2 = int(input("choose your fighter: "))
        if chosen2 == 1:
            print("your color is White, Computer's is Black\ngood luck\n")
            new_game = PlayGame()
            c_player = RandomCompPlayer()
            new_game.play(c_player)
        elif chosen2 == 2:
            print("your color is White, Computer's is Black\ngood luck\n")
            new_game = PlayGame()
            c_player = OkComputer()
            new_game.play(c_player)
        elif chosen2 == 3:
            print("White color starts, Black follows")
            new_game = PlayGame()
            h_player = HumanPlayer()
            h_player.color = "B"
            h_player.p_places = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
            new_game.play(h_player)
            print("CONGRATULATIONS!")
        else:
            pass
        print(
            """
            1. continue playing
            2. quit
            """
        )
        chosen1 = int(input("option: "))
    while chosen1 == 2:
        print(
            """
            1. Random Computer vs Random Computer
            2. Random Computer vs Ok Computer (Random Computer makes the first move)
            3. Ok Computer vs Random Computer (Ok Computer makes the first move)
            4. Ok Computer vs OkComputer
            """
        )
        chosen2 = int(input("choose the fight you want to watch: "))
        if chosen2 == 1:
            new_game = PlayGame()
            cplayer1 = RandomCompPlayer()
            cplayer2 = RandomCompPlayer()
            cplayer2.color = "W"
            cplayer2.p_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
            new_game.simulation(cplayer1, cplayer2)

        elif chosen2 == 2:
            new_game = PlayGame()
            cplayer1 = RandomCompPlayer()
            cplayer2 = OkComputer()
            cplayer2.color = "W"
            cplayer2.p_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
            new_game.simulation(cplayer1, cplayer2)

        elif chosen2 == 3:
            new_game = PlayGame()
            cplayer2 = RandomCompPlayer()
            cplayer1 = OkComputer()
            cplayer2.color = "W"
            cplayer2.p_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
            new_game.simulation(cplayer1, cplayer2)

        elif chosen2 == 4:
            new_game = PlayGame()
            cplayer1 = OkComputer()
            cplayer2 = OkComputer()
            cplayer2.color = "W"
            cplayer2.p_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
            new_game.simulation(cplayer1, cplayer2)

        else:
            pass

        print(
            """
            1. continue watching simulations
            2. quit
            """
            )
        chosen1 = int(input("option: "))
        if chosen1 == 1:
            chosen1 = 2
        elif chosen1 == 2:
            chosen1 == 3
        else:
            pass

    if chosen1 == 3:
        print("")
