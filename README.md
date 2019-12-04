# Minesweeper 2.0
A modern interpretation on the classic Minesweeper game in `Python` using `PyGame`.
## Index
1. [How To Install Minesweeper 2.0](#installing-minesweeper-20)
2. [How To Play Minesweeper 2.0](#playing-minesweeper-20)
3. [Extending Minesweeper 2.0](#extending-minesweeper-20)
4. [Documentation](#documentation)
5. [Authors and Contributions](#authors-and-contributions)
6. [License](#license)

## Installing Minesweeper 2.0
###### For Both Mac and Windows
1. Download [Pygame](https://www.pygame.org/download.shtml) 
2. Click > Clone or Download
3. Click > Download ZIP
4. Unzip the file and run the python file named MinesweeperGUI.py using any IDE
5. Enjoy!

![To Download](assets/zip.png)

## Playing Minesweeper 2.0
To Play Minesweeper 2.0 the rules of the original minesweeper still apply. We have a table of tiles that can be pressed with your mouse. Some tiles contain bombs underneath, and your goal is to flag them using the right click on your mouse. The game is won when all the bombs have been flagged. If you happen to left click on a tile with a bomb underneath, the game is lost. The number on a tile represents how many bombs are surround it.

![To Download](assets/screenshot_1.PNG)
![To Download](assets/screenshot_2.PNG)

## Extending Minesweeper 2.0

## Documentation
  The Github Directory is structured such that all Python files and the assets folder are located in the root folder of the directory. This directory only contains one folder, which contains the visual PNG assets required for the game as well as the images included in this ReadMe. 
  The class responsible for controlling the logical model of Minesweeper is the Board class, located in Board.py. This class can be used to generate boards for the Minesweeper game, as the name of the class suggests. All computations on the state of the board occur in the Board class, which utilizes Tile child class objects and Sampler (a class located in Board.py) objects. A Board object contains methods to alter its state as well as the states of the Tiles it contains. The Sampler object is used to randomly distribute Tiles in the create_board() method. Running the Board class allows the user to play a text version of the game, where the player can type in the console to play the game.
  The Tile class, which is utilized heavily in the Board class and located in Tile.py, represents the state of a single tile on a Minesweeper board. This class defines the behaviour of a tile when it is revealed, clicked, or flagged. This class also has methods for returning its position, type, and string representation. The behaviour of a Tile when clicked is implemented in the child classes: BombTile, NumberTile, and EmptyTile.
  The Python classes TileView and MinesweeperGUI are responsible for running a visual version of the Minesweeper game, as shown in the screenshots. These classes utilize PyGame. The player uses the GUI to play the game.

## Authors and Contributions
#### Kavin Adithiya
> Insert Contribution
#### Sohrab Amin
> Insert Contribution
#### Aishah Kabir
> Insert Contribution
#### Emily Wu
> Emily Wu implemented the completed versions of Board, Sampler, Tile, NumberTile, BombTile, and Empty Tile classes and wrote the documentation of those classes. These classes represent the logical model of the game, which controls the underlying mechanics of the gameplay. She contributed to the ReadMe file by describing the code she implemented under Documentation.
#### Nan Xu
> Insert Contribution
## License
See the [LICENSE](LICENSE.txt) file for license rights and limitations (MIT).
