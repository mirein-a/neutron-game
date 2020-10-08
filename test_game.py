from ThePlayer_projekt import HumanPlayer, RandomCompPlayer, OkComputer
from TheGame_projekt import Game
from Play_projekt import PlayGame
from ThePossibilities_projekt import PossibleMoves

pm = PossibleMoves()
g = Game()
hp = HumanPlayer()
randomc = RandomCompPlayer()
okc = OkComputer()
pg = PlayGame(randomc, okc)


def test_players():
    assert len(hp.p_places) == 5
    assert len(randomc.p_places) == 5
    assert len(okc.p_places) == 5
    assert type(randomc.move_reg(g.display)) == tuple, str
    assert type(okc.move_reg(g.display)) == tuple, str
    assert type(randomc.move_n((2, 2), g.display)) == str
    assert type(okc.move_n((2, 2), g.display)) == str


def test_possible_moves():
    assert pm.check_move('down', (1, 0), g.display) is True
    assert pm.check_move('up', (1, 0), g.display) is None
    assert pm.check_move('', (1, 0), g.display) is None
    assert pm.check_move('diagonal down right', (9, 2), g.display) is None
    assert type(pm.generate_possibilities((1, 0), g.display)) == list


def test_the_rules():
    assert type(g.the_display()) == str
    assert g.move_the_pieces((0, 0), 'down', 'B') == (3, 0)
    assert type(g.move_the_pieces((3, 0), 'down', 'B')) == tuple


def test_the_game():
    assert pg.check_winner(g.display) is False
    disp1 = [
            ["B", "B", "B", "B", "B"],
            [" ", " ", " ", " ", " "],
            [" ", " ", "W", " ", " "],
            [" ", " ", " ", " ", " "],
            ["W", "N", "W", "W", "W"]
        ]
    pg.neutron_position = (4, 1)
    assert pg.check_winner(disp1) is True
    disp2 = [
            [" ", "W", " ", " ", "W"],
            [" ", "W", " ", "W", " "],
            ["W", " ", "N", " ", " "],
            [" ", "W", " ", " ", " "],
            ["B", "B", "B", "B", "B"]
        ]
    pg.comp_player.p_places = [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    assert pg.check_winner(disp2) is True
    disp3 = [
            [" ", " ", " ", " ", "B"],
            [" ", "B", "B", "W", " "],
            [" ", "B", "N", "W", " "],
            [" ", "W", "W", "B", " "],
            [" ", "W", " ", " ", " "]
        ]
    pg.neutron_position = (2, 2)
    g.display = disp3
    assert pg.check_winner(disp3) is True
