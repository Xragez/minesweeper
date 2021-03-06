# Saper

- Okno jest podzielone na planszę do gry oraz boczny ekran z informacjami (timer, ilośc bomb, przyciski do:  restartu, menu ustawień i wyjścia).

- Ustawienia wielkości planszy i ilości bomb są wczytywane z pliku settings.csv (jeśli program nie może znaleźć pliku z ustawieniami to wczytuje domyślne podane w pliku default.py).

- Po kliknięciu przycisku Apply ustawienia zapisują się do pliku settings.csv, a gra restartuje się z nowymi ustawieniami.

- W menu nie da się wpisać liczb ujemnych, a po wpisaniu liczb wychodzących poza zakres lub przy zostawieniu pustego pola wyświetlą się odpowiednie komunikaty i zapis będzie niemożliwy.

- Licznik bomb wyświetla ile bomb zostało do zaznaczenia.

- Po przegranej lub wygranej partii pod przyciskiem Restart pojawi się odpowiedni komunikat (You Win lub Game Over), a plansza i timer zostaną zamrożone.

- Główne okno jest podzielone na planszę do gry oraz boczny ekran z informacjami (timer, ilośc bomb, przyciski do:  restartu, menu ustawień i wyjścia).

- Menu ustawień zawiera trzy pola tekstowe: 
	- pole do wprowadzenia szerokości planszy
	- pole do wprowadzenia wysokości planszy
	- pole do wprowadzenia ilości bomb

- Wprowadzenie mniejszego rozmiaru planszy niż 2x2 lub większego niż 15x15, liczby
bomb mniejszej niż 0 lub większej niż m*n powoduje wyświetlenie komunikatu o
błędzie. Nie można rozpocząć gry dopóki te parametry nie są poprawne.

- Na początku gry na losowych polach umieszczane jest tyle min ile wskazano w polu
	tekstowym (każde możliwe rozłożenie min jest równie prawdopodobne).
 - Po kliknięciu lewym przyciskiem na pole:
	- Jeśli jest tam mina, wyświetlana jest wiadomość o przegranej i gra się
kończy,
	- Jeśli w sąsiedztwie pola są miny, na przycisku wyświetlana jest ich liczba a
pole dezaktywuje się,
- W przeciwnym razie sąsiednie pola są sprawdzane tak jakby zostały kliknięte
a pole dezaktywuje się.
- Po kliknięciu prawym przyciskiem pole może zostać oznaczone “tu jest mina”, po
ponownym kliknięciu oznaczenie zmienia się na “tu może być mina”, a po kolejnym
kliknięciu oznaczenie znika.
- Gra kończy się po kliknięciu wszystkich pól bez min, lub oznaczeniu “tu jest mina”
wszystkich pól z minami (i żadnych innych).
- Po naciśnięciu kolejno klawiszy x, y, z, z, y, pola pod którymi są miny stają się
ciemniejsze (

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
