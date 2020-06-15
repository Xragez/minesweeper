# Projekt nr 13: Saper

[*Link do opisu*](http://elf2.pk.edu.pl/pluginfile.php/88409/mod_resource/content/15/Projekty_JS_2020_wytyczne.pdf)
##### List comprehensions:
* [tutaj](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/game_screen.py#L25)

##### Klasy:
* [Block](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/block.py#L5)
* [GameScreen](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/game_screen.py#L7)
* [InfoScreen](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/info_screen.py#L14)
* [MenuScreen](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/info_screen.py#L142)
* [TextArea](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/info_screen.py#L242)
* [Text](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/info_screen.py#L319)
* [Game](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/run.py#L17)

##### Wyjątki:
* [WrongSettingsException, ValueError](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/info_screen.py#L217)
* [FileLoadErrorException](https://github.com/Xragez/minesweeper/blob/8d6aebae3b09ba6f76f9a80dccc0db20e46a240e/run.py#L127)

##### Projekt minimalnie różni się od opisu zadania, ale zawarte są w nim wszystkie wymienione tam funkcjonalności razem z kodem xyzzy na zaznaczanie bomb.

* Okno jest podzielone na planszę do gry oraz boczny ekran z informacjami (timer, ilość bomb, przyciski do:  restartu, menu ustawień i wyjścia).

* Ustawienia wielkości planszy i ilości bomb są wczytywane z pliku settings.csv (jeśli program nie może znaleźć pliku z ustawieniami to wczytuje domyślne podane w pliku default.py).

* Po kliknięciu przycisku Apply ustawienia zapisują się do pliku settings.csv, a gra restartuje się z nowymi ustawieniami.

* W menu nie da się wpisać liczb ujemnych, a po wpisaniu liczb wychodzących poza zakres lub przy zostawieniu pustego pola wyświetlą się odpowiednie komunikaty i zapis będzie niemożliwy.

* Licznik bomb wyświetla ile bomb zostało do zaznaczenia.

* Po przegranej lub wygranej partii pod przyciskiem Restart pojawi się odpowiedni komunikat (You Win lub Game Over), a plansza i timer zostaną zamrożone.
