import tkinter as tk
import style
import dialog


class PredictDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Predykcja", font=style.labelFont)
        label.pack(pady=style.labelpady)

        # TODO: sekcja pierwsza - predykcja z pliku
        # TODO: użytkownik ładuje plik csv, z którego dane będą predykowane
        # TODO: sprawdzić jakoś format pliku i czy się liczba kolumn zgadza
        # TODO: jak coś się nie zgadza to komunikat

        # TODO: sekcja druga - predykcja z próbki
        # TODO: dodanie pól tk.Entry na podstawie których można dodać dane
        # TODO: dodanie przycisku, który predykuje

        # TODO: w obu przypadkach zapis do bazy wyników i nowy dialog/okienko modalne
        # TODO: prezentacja wyników w formie tabeli dla zestawu danych z pliku
        # TODO: prezentacja na pojedynczym polu dla jednej próbki
        # TODO: przycisk generujący raport na podstawie wyników
