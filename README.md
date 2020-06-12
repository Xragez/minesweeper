# Projekt nr 13: Saper

[*Link do opisu*](http://elf2.pk.edu.pl/pluginfile.php/88409/mod_resource/content/15/Projekty_JS_2020_wytyczne.pdf)

##### Projekt minimalnie różni się od opisu zadania, ale zawarte są w nim wszystkie wymienione tam funkcjonalności razem z kodem xyzzy na zaznaczanie bomb.

* Okno jest podzielone na planszę do gry oraz boczny ekran z informacjami (timer, ilośc bomb, przyciski do:  restartu, menu ustawień i wyjścia).

* Ustawienia wielkości planszy i ilości bomb są wczytywane z pliku settings.csv (jeśli program nie może znaleźć pliku z ustawieniami to wczytuje domyślne podane w pliku default.py).

* Po kliknięciu przycisku Apply ustawienia zapisują się do pliku settings.csv, a gra restartuje się z nowymi ustawieniami.

* W menu nie da się wpisać liczb ujemnych, a po wpisaniu liczb wychodzących poza zakres lub przy zostawieniu pustego pola wyświetlą się odpowiednie komunikaty i zapis będzie niemożliwy.

* Licznik bomb wyświetla ile bomb zostało do zaznaczenia.

* Po przegranej lub wygranej partii pod przyciskiem Restart pojawi się odpowiedni komunikat (You Win lub Game Over), a plansza i timer zostaną zamrożone.