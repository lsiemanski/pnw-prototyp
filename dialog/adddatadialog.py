import tkinter as tk
import dialog.abstractdialog
import style
import pandas as pd 
from tkinter import messagebox

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

        labelPath = tk.Label(self, text="ścieżka:", font=style.labelFont)
        labelPath.pack(pady=style.labelpady)

        pathEntry = tk.Entry(self)
        pathEntry.pack()

        buttonPath = tk.Button(self, text="Wczytaj", font=style.buttonFont, command=lambda: self.buttonOnClickPath(pathEntry.get()))
        buttonPath.pack(pady=style.buttonpady)


        # =================================

        spanLabel = tk.Label(self, text="Span:", font=style.labelFontDesc)
        spanLabel.pack(pady=style.labelpady)

        spanEntry = tk.Entry(self)
        spanEntry.pack()

        section_heightLabel = tk.Label(self, text="Section height:", font=style.labelFontDesc)
        section_heightLabel.pack(pady=style.labelpady)

        section_heightEntry = tk.Entry(self)
        section_heightEntry.pack()

        steel_young_modulusLabel = tk.Label(self, text="Steel young modulus:", font=style.labelFontDesc)
        steel_young_modulusLabel.pack(pady=style.labelpady)

        steel_young_modulusEntry = tk.Entry(self)
        steel_young_modulusEntry.pack()

        reinforcement_gradeLabel = tk.Label(self, text="Reinforcement grade:", font=style.labelFontDesc)
        reinforcement_gradeLabel.pack(pady=style.labelpady)

        reinforcement_gradeEntry = tk.Entry(self)
        reinforcement_gradeEntry.pack()

        loadLabel = tk.Label(self, text="Load:", font=style.labelFontDesc)
        loadLabel.pack(pady=style.labelpady)

        loadEntry = tk.Entry(self)
        loadEntry.pack()

        secton_widthLabel = tk.Label(self, text="Secton width:", font=style.labelFontDesc)
        secton_widthLabel.pack(pady=style.labelpady)

        secton_widthEntry = tk.Entry(self)
        secton_widthEntry.pack()    

        coverLabel = tk.Label(self, text="Cover:", font=style.labelFontDesc)
        coverLabel.pack(pady=style.labelpady)

        coverEntry = tk.Entry(self)
        coverEntry.pack()       



    def buttonOnClickPath(self, path):
        try:
            self.data = pd.read_csv(f"{path}", sep=';')
        except:
            messagebox.showerror('Błąd!','Nie odnaleziono pliku!')

        
        # TODO: sekcja druga - dodaj próbkę
        # TODO: dodanie pól tk.Entry na podstawie których można dodać dane
        # TODO: zapis tych danych do bazy
        # TODO: dodanie przycisku, który dodaje



    
        '''
            'reinforcement_diameter': parameters['reinforcement_diameter'],
            'concrete_tensile_strength': parameters['concrete_tensile_strength'],
            'concrete_young_modulus': parameters['concrete_young_modulus'],

'''


