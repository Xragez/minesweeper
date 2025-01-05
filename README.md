# Minesweeper

- The window is divided into a game board and a side screen with information (timer, number of bombs, buttons for: restart, settings menu and exit).

- The settings for the game board size and the number of bombs are loaded from the settings.csv file (if the program can't find the file with the settings it loads the default ones given in the default.py file).

- When you click Apply, the settings are saved to the settings.csv file, and the game restarts with the new settings.

- Negative numbers cannot be entered in the settings, and if you enter numbers out of range or if you leave the field blank, appropriate messages will be displayed and saving will be impossible.

- The bomb counter displays how many bombs are left to mark.

- After losing or winning a game, an appropriate message (You Win or Game Over) will appear under the Restart button, and the board and timer will be frozen.

- The main window is divided into a game board and a side screen with information (timer, number of bombs, buttons for: restart, settings menu and exit).

- Entering a board size smaller than 2x2 or larger than 15x15, a number of bombs smaller than 0 or larger than m*n results in an error message. You cannot start the game until these parameters are correct.

- At the beginning of the game, as many mines are placed on random fields as indicated in the text box (any possible distribution of mines is equally likely).
- When the left button is clicked on a field:
	- If there is a mine there, a game over message is displayed and the game ends,
	- If there are mines adjacent to the field, the number of mines is displayed on the field and the field deactivates,
- Otherwise, adjacent fields are checked as if they were clicked and the field deactivates.
- When the right button is clicked, the field may be marked “there is a mine here,” when clicked again the marking changes to “there may be a mine here,” and when clicked again the marking disappears.
- The game ends when all fields without mines are clicked, or all fields with mines (and no others) are marked “here is a mine.”

### Cheatcodes:
- When you press the x, y, z, z, y keys in succession, the fields under which there are mines become darker
