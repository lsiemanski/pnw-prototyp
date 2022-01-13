import tkinter as tk
import dialog.abstractdialog
import style


class AddDataDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Dodaj dane eksperymentalne", font=style.labelFont)
        label.pack(pady=style.labelpady)

        # TODO: sekcja pierwsza - dodaj dane z pliku
        # TODO: użytkownik ładuje plik csv, z którego dane zostają przeniesione do bazy
        # TODO: sprawdzić jakoś format pliku i czy się liczba kolumn zgadza
        # TODO: jak coś się nie zgadza to komunikat

        # TODO: sekcja druga - dodaj próbkę
        # TODO: dodanie pól tk.Entry na podstawie których można dodać dane
        # TODO: zapis tych danych do bazy
        # TODO: dodanie przycisku, który dodaje
