_Weronika Obcowska, PIPR Projekt, 2019Z_
# neutron-game


## The rules of the game
1. The board is 5x5. When starting the game, the bottom row contains “W” pieces (white), at the
top there are “B” ones (black). Black pieces are played by the computer player, white ones by
the user or the second computer player (in the simulation mode).
2. When starting the game, the special piece, Neutron, is in the middle of the board. It’s played
by both players.
3. The aim of the game is moving the Neutron to one’s base or taking the opponent’s base.
4. In case the Neutron gets blocked by the other pieces, both players win.
5. Pieces get to be moved in the following directions: up, down, left, right, diagonally up to the
right or to the left, diagonally down to the right or to the left.
6. One round equals moving one regular piece and the Neutron being moved by the opponent.

## Class Game
It is the class, which contains the initial display of the pieces on the board (`display` attribute)
and the information of how moving across the board takes place in certain directions. Methods
`move_horizontally`, `move_vertically` and `move_diagonally` specify the movement in the directions
designated to them by incrementing or decrementing the piece’s indices until further movement is not
valid (when the board ends or when the next place is taken by the opponent’s piece). Method
`move_the_pieces` calls the methods mentioned above. This class’ methods are not supposed to handle
exceptions – if the coefficients or the direction are not valid, the program will stop working (which by
default is not going to happen, because this class is not directly available to the user. Instead, other
classes’ methods use this one’s methods).

## Class PossibleMoves
  This class is used to generates lists of possible moves by the pieces across the board and
partially to handle exceptions. Method `check_move` takes the pieces’ coefficients and the direction as
arguments; then checks if the direction is in the dictionary of directions (attribute of the same name)
and if the piece can be moved in said direction. In case of the piece being “blocked” by other pieces or
indices exceeding the boards’ measurements, the method returns nothing, otherwise it returns True.
The method described above is called by the `generate_possibilities` method – for the specified
coefficients all of the valid directions are checked one by one. If the piece can be moved in a certain
direction, it is added to the list of the possible directions (possibilities attribute), which gets passed to
the players’ classes (when they choose how to move the piece).

## Classes HumanPlayer, RandomCompPlayer, OkComputer
  These classes serve the purpose of creating players’ objects. Class `HumanPlayer`’s methods
enable communication with the user during the game, class `RandomCompPlayer`’s and `OkComputer`’s
methods base the choices off of the previously specified criteria. When the object from one of those
classes is created, it gets its color (“W” or “B”, color attribute) and the list of coefficients taken by the
pieces on the board (`p_places` attribute) – those are the pieces which can be moved by the object’s
methods.
  Methods `move_reg` and `move_n` in class `HumanPlayer` interact with the user: what kind of
choice they are supposed to make and from which they can choose. The list of possible moves for a
certain piece is created when `generate_possibilities` (class `PossibleMoves`’ method) is called. In case
of choosing the piece that cannot be moved in any direction or picking the direction not included in
the possible directions list, methods `move_reg` and `move_n` ask the user to provide information once
again.
  Analogous methods in class `RandomCompPlayer` make random choices for the coefficients
(from the `p_places` attribute) and for the direction (from the list of possible directions). If the piece
cannot be moved in any direction, it is chosen again, until the length of the possible directions list
does not equal zero.
  Class `OkComputer` is a subclass of `RandomCompPlayer`. There are three attributes in class
`OkComputer`, which serve the purpose of choosing the coefficients and the directions. Those choices
are not random. When the regular piece is to be moved, `move_reg` method chooses the piece (from
`p_places` attribute) with the index stored as an attribute i, which gets incremented after making said
choice. If the move is not valid, the coefficients are chosen again, with the same instruction. Then the
direction is being chosen – it will always be the direction the last one from the first half. Index of this
direction is stored in the attribute j. The direction for the Neutron is chosen similarly, though the index
is stored in the attribute k. This way, the `OkComputer`’s object is biased towards choosing the same
direction over and over again, for the list of possible directions is always in the same order. This is
especially visible when the list is long, otherwise the method will settle for a different direction.

## Class PlayGame
  This class contains attributes directly allowing to play the game. Attributes `user_player` and
`comp_player` are for player’s avatars, attribute turn tells which player is supposed to make the move.
The Neutron is a special piece played by both players – because of that its coefficients are stored in
the separate attribute (`neutron_position`). Methods `check_winner` and `evaluate_results` verify if the
game should end, if so, who the winner is. When the game ends is verified based on:
  1. The Neutron coefficients (the game ends when the first coefficient equals 0 or 4, which means
  that the Neutron is in one of the players’ base).
  2. The coefficients of the pieces played by players (the game ends when the player whose base
  is in row 0 moves all of his pieces to row 4 and vice versa).
  3. The length of the list of possible moves for the Neutron (the game ends when the length is
  equal to zero – it means that the Neutron is “blocked” and cannot be moved).
  Method `play` brings together all of the classes listed above. The player’s objects are created (one
of them is the `HumanPlayer`’s object by default, the other is supposed to be given as an argument) and
the board along with the instructions on making moves (class `Game`’s objects). In every round the
winning requirements are verified (`check_winner` method), if they are met, the winner is announced.
  The process is organized in the following way: the user starts with moving the regular piece, the
computer player responds with moving the Neutron, in the second round the computer player moves
one of its regular pieces, the user responds with moving the Neutron. The pattern is repeated in every
round.
  It is possible to carry out a simulation (by method `simulation`) – the duel between two computer
players. This kind of duel can be done by two objects from the same class of players or by different
ones. The criteria of the end of the game are the same as for the duel between the computer player and
the user player.

## How to play
  In the MainMenu file there is a starting menu, which serves the purpose of the interactive user
manual. It tells how to choose the pieces and directions, as well as “what is happening at the
moment”, during the game.

## What has been achieved
  The program works as it is supposed to work. All kinds of situations resulting from human
mistakes during the game or from how the methods function together have been covered. Multiple
modes and options make the game interesting. The main problem while creating the program was to
work out how to move across the board, because it required analysing the goals from every
perspective: the right way to get the coefficients was needed, so they do not exceed the length of the
lists, the pieces do not override each other, pieces move in every round, without stagnation. Verifying
the validity of the moves, storing the current coefficients of the pieces and instructions on how to
make the move have been placed in different classes, so the elements listed above are independent
from each other.
  Last minute before finishing, I added another option: now two users can play together using
the board. The program communicates with each of them. The rules are the same as when the user is
playing with the computer player.


## What has not been achieved
  In my opinion the code could be shorter and optimalized in a better way; what the game looks
like could be more user-friendly. The implementation contains repetitions and lacks special graphic
design. Other than that, there could be more variety in options for computer players. When adding
more computer players or modes of the game, the starting menu should be modified. It was designed
for few combinations of how the game can be played, not sufficient to handle multiple options.
Otherwise, it would be work in a repetitive manner. This could be avoided by managing those options
in functions.

## Adding new options to the game
  New computer player’s class should inherit from class `RandomCompPlayer`. The constructor
method must contain the attributes `color` and `p_places`: the first one by default set as “B”, the second
one as a list of every coefficient from row 0. It may also contain additional attributes needed for
choosing the moves.
  There must be methods `move_reg` and `move_n`. The first one should take the display of the
pieces on the board as an argument (in this program the attribute `display`, from class `Game`’s object, is
given as said argument, for those methods are not used directly by the user). The second one takes the
Neutron’s position as an argument, as well as the `display` (both of these arguments are provided by
different classes’ methods when the program is running, not by the user). Method `move_reg` must
choose the coefficients from the `p_places` attribute, both of the methods listed above must call the
`generate_possibilities` method (`PossibleMoves` class), to ensure that the choices are valid. Method
`move_reg` must return the coeffiecients of the piece (a tuple) that is supposed to be moved and a
direction’s name (a string from the list of possible moves) of said movement, `move_n` must return the
direction (similarly to `move_reg`). The way in which the coefficients (`move_reg` only) and direction
(both `move_reg` and `move_n`) are chosen is optional.

## Tests
  In the test_game file, there are tests for some of the methods. Outputs (and their types) of the
complex methods are verified to make sure that the program handles all possible exceptions and that
the methods work as they are designed to.
