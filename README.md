# Instrukcja procesu konfiguracji LEGO® Education SPIKE™ z VS Code 

Poniższe kroki procesu konfiguracji wykonane zostały na komputerze z zainstalowanym systemem operacyjnym Windows 10.

## Dostępne komendy 

* **Upload to SPIKE PRIME** - komenda opowiadająca za przesłanie programu do LEGO® Education SPIKE™ poprzez wprowadzenie identyfikatora gniazda, do którego mamy zamiar załadować przesyłany micropythonowy program. W trakcie przesyłania programu należy określić identyfikator gniazda wybrany z przedziału od 1 do 19 włącznie oraz numer portu połączenia LEGO® Education SPIKE™ z komputerem,
* **List SPIKE PRIME files** - komenda odpowiadająca za wyświetlenie listy zarezerwowanych identyfikatorów gniazd LEGO® Education SPIKE™ wraz z informacją, na którym gnieździe znajduje się jaki załadowany program. Uzyskujemy ją przy użyciu jednej z opcji dodatku w postaci "Upload to SPIKE PRIME",
* **Delete SPIKE PRIME file** - komenda odpowiadająca za usuniecie przesłanego do LEGO® Education SPIKE™ micropythonowego programu wprowadzonego przez użytkownika przy użyciu komendy "Upload to SPIKE PRIME". Usuwanie odbywa się poprzez wprowadzenie odpowiedniego identyfikatora gniazda, na którym załadowany został wybrany do usunięcia program,
* **Start SPIKE PRIME program** - komenda odpowiedzialna za uruchomienie programu dla LEGO® Education SPIKE™ z odpowiedniego identyfikatora gniazda określone przez użytkownika w momencie wzbudzenia komendy,
* **Stop SPIKE PRIME program** - komenda odpowiedzialna za zatrzymanie oraz zaprzestanie wykonywania się uruchomionego programu dla LEGO® Education SPIKE™, 
* **Move SPIKE PRIME program** - komenda odpowiedzialna za przeniesienie załadowanego program z gniazda o określonym w trakcie załadowania identyfikatorze do określonego oraz niezarezerwowanego jeszcze gniazda hubu LEGO® Education SPIKE™, 
* **SPIKE PRIME Firmware Info** - komenda odpowiedzialna za wyświetlanie informacji o oprogramowaniu LEGO® Education SPIKE™,
* **SET SPIKE PRIME Port** - komenda odpowiadająca za za zapis numeru portu połączenia LEGO® Education SPIKE™ z komputerem w celu wykorzystania go jako informacja dla pozostałych komend, 
* **Create new SPIKE PRIME micropython program** - komenda odpowiedzialna za stworzenie micropythonowego pliku inicjalizującego programu zawierającego elementy szablonu wygenerowanego dzięki dodatkowi dla LEGO® Education SPIKE™. 

## Kolejne kroki procesu konfiguracyjnego VS Code umożliwiającego pisanie programów na LEGO® Education SPIKE™

1. Pobierz oraz zainstaluj najnowszą wersję Visual Studio Code (obecnie 1.47) ze strony producenta [https://code.visualstudio.com/](https://code.visualstudio.com/) jeśli nie masz jeszcze jej zainstalowanej na swoim komputerze,
2. Po pomyślnej instalacji Visual Studio Code zainstaluj najnowszą wersje Pythona 3 ze strony producenta [https://www.python.org/downloads/](https://www.python.org/downloads/) jeśli nie jest ona już zainstalowana na Twoim systemie operacyjnym. Po uruchomieniu pliku instalacyjnego na samym dole okna instalacyjnego kliknij opcję "Add Python to PATH" a następnie przejdź do procesu instalacji poprzez kliknięcie frazy "Install Now",
3. Po pomyślnej instalacji Pythona 3 na Twoim systemie sklonuj lub też pobierz skompresowaną wersję repozytorium a następnie rozpakuj w dowolnym z katalogów na Twoim komputerze. Następnie uruchom plik o nazwie **install.windows.bat** poprzez dwukrotnie kliknięcie, tak aby zainstalować go na dysku C. Po uruchomieniu pliku instalacyjnego pojawi się konsola, która następnie poprosi Cię o kliknięcie dowolnego klawisza w celu rozpoczęcia procesu instalacyjnego. Jeśli instalacja nie powiedzie się, uruchom plik jako administrator klikając na niego prawym przyciskiem myszy oraz wybierając opcję "Uruchom jako Administrator". Program Windows Defender może oznaczyć go jako nierozpoznany instalator. Po prostu pozwól mu działać. Jeśli nadal się nie powiedzie, prawdopodobnie oznacza to, że zapomniałeś dodać Pythona do swojej ścieżki lub zainstalowałeś złą wersję Pythona. W takim wypadku cofnij się do punktu 2,
4. Po zakończeniu instalacji wyszukaj w katalogu plik instalacyjny o nazwie **spikeprime-0.1.0.vsix**, dzięki któremu zainstalowany zostanie dodatek do Visual Studio Code pozwalający w łatwy sposób na korzystanie z wymienionych wcześniej komend oraz programowanie LEGO® Education SPIKE™ w środowisku micropythona,
5. Po pobraniu uruchom zainstalowany z punktu 1 Visual Studio Code. Następnie otwórz linię komend poprzez wciśniecie klawisza F1, wpisz "Install from VSIX" a następnie zatwierdź operację klawiszem Enter na klawiaturze. Program przeniesie Cię do eksploratora plików, gdzie musisz odnaleźć pobrany plik z punktu 4 o nazwie **spikeprime-0.1.0.vsix**. Po jego odszukaniu wybierz go poprzez dwukrotne kliknięcie lewym przyciskiem myszy,
6. Po pomyślnej instalacji dodatku zrestartuj komputer.

## Utworzenie pierwszego przykładowego programu wraz z przesłaniem oraz uruchomieniem go na LEGO® Education SPIKE™

1. Utwórz folder poświęcony na składowanie swoich projektów oraz programów przeznaczonych do uruchomienia na LEGO® Education SPIKE™,
2. Uruchom Visual Studio Code a następnie przejdź do zakładki "File", z której wybierz opcję "Open Folder". Przy pomocy, którego wybierany zostanie utworzony wcześniej folder na składowane programy przeznaczone do przesłania do LEGO® Education SPIKE™,
3. Utwórz micropythonowy plik dla LEGO® Education SPIKE™ przy użyciu jednej z opcji dodatku do Visual Studio Code. W tym celu naciśnij klawisz F1 oraz wpisz frazę "spike" w górnym formularzu edytora Visual Studio Code. W efekcie wyświetlone zostaną wszystkie dostępne polecenia zainstalowanego dodatku z wcześniejszych kroków procesu konfiguracyjnego. Następnie z listy wybierz opcję "Create new SPIKE PRIME micropython program" oraz wprowadź odpowiednią nazwę pliku dla micropythonowego programu (Plik musi kończyć się odpowiednim rozszerzeniem pliku w postaci .py). W wyniku powyższych operacji utworzony zostanie przykładowy micropythonowy plik z dostępnego szablonu, dzięki któremu po przesłaniu i uruchomieniu go na LEGO® Education SPIKE™ jesteśmy w stanie stwierdzić czy powyższe kroki procesu konfiguracji wykonane zostały w poprawny sposób. Aby zmodyfikować jego zawartość musimy odnaleźć go w stworzonym wcześniej folderze przy pomocy skrótu klawiszowego Ctrl + P, który pojawi formularz dzięki któremu po wpisaniu dokładnej nazwy otworzymy wygenerowany plik programu dla LEGO® Education SPIKE™. Poniżej zaprezentowany został szablon programu utworzonegozaraz po wykonaniu komendy "Create new SPIKE PRIME micropython program". Zawiera on polecenia wywołujące wyświetlenie uśmiechu na wyświetlaczu huba LEGO® Education SPIKE™ oraz zmiennego sygnału dźwiękowego,

```
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

hub.speaker.beep(60, 0.5)
hub.speaker.beep(67, 0.5)
hub.speaker.beep(60, 0.5)

```
4. Włącz hub LEGO® Education SPIKE™ przy użyciu środkowego, okrągłego przycisku umieszczoego na głównym panelu urządzenia przytrzymując go przez około 3 sekundy,
5. Podłącz LEGO® Education SPIKE™ z komputerem przy użyciu złącza USB,
6. Zlokalizuj port szeregowy za pomocą Menedżera urządzeń (możesz go znaleźć w menu Start). Pod portami poszukaj czegoś o nazwie Porty (COM i LPT). Jeśli jest ich wiele, spróbuj odłączyć urządzenie a następnie podłączyć je ponownie, aby zobaczyć, który z portów pojawił się ponownie. Po odnalezieniu go zanotuj identyfikator, którym będzie COMX (np. COM3, COM25 itd.),
7. W kolejnym z korków uruchom ponownie edytor Visual Studio Code wraz z otwartym plikiem micropythonowego programu a następnie wywołaj komendę (poprzez wciśnięcie klawisza F1) "Upload to SPIKE PRIME" wraz z określeniem identyfikatora gniazda (zalecamy wybranie identyfikatora o numerze 1) oraz portu szeregowego urządzenia. Jeśli przesyłanie trwa dłużej niż 30 sekund, spróbuj anulować polecenie za pomocą skrótu klawiaturowego Ctrl + C kilka razy w oknie terminala a następnie spróbuj ponownie wykonać polecenie jeszcze raz. Jeśli nadal wywołana komenda nie zadziała lub też wyświetli błąd, sprawdź ponownie czy wprowadziłeś poprawny port szeregowy lub też masz otwarte okno programu SPIKE PRIME.
W razie potrzeby sprawdź poprawność działania pozostałych poleceń z listy lub wykonaj proces konfiguracji jeszcze raz,
8. W ostatnim już kroku przejdź do uruchomienia testowego lub też własnego załadowanego w poprzednim kroku programu do LEGO® Education SPIKE™, poprzez dwukrotne naciśnięcie przycisku prawej strzałki między środkowym przyciskiem przy pomocy, którego zatwierdzamy jednym kliknięciem zatwierdzamy uruchomienie się zapisanego przez nas programu.
