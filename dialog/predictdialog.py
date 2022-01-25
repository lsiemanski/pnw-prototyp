import os
import tkinter as tk
import style
import dialog
import numpy as np
from tkinter import messagebox, filedialog as fd
import pandas as pd

from logic.dbservice import DataBase


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

        buttonPath = tk.Button(self, text="Wybierz plik", font=style.buttonFont, command=lambda: self.buttonOnClickPath())
        buttonPath.pack(pady=style.buttonpady)

        or_label = tk.Label(self, text="LUB:", font=style.entryLabelFont)
        or_label.pack()

        # TODO: sekcja druga - predykcja z próbki
        # TODO: dodanie przycisku, który predykuje

        self.span = tk.StringVar()
        span_label = tk.Label(self, text="Rozpiętość", font=style.entryLabelFont)
        span_label.pack()
        self.span_entry = tk.Entry(self, textvariable=self.span)
        self.span_entry.pack()

        self.section_height = tk.StringVar()
        section_height_label = tk.Label(self, text="Wysokość przekroju", font=style.entryLabelFont)
        section_height_label.pack()
        self.section_height_entry = tk.Entry(self, textvariable=self.section_height)
        self.section_height_entry.pack()

        self.steel_young_modulus = tk.StringVar()
        steel_young_modulus_label = tk.Label(self, text="Moduł Younga stali", font=style.entryLabelFont)
        steel_young_modulus_label.pack()
        self.steel_young_modulus_entry = tk.Entry(self, textvariable=self.steel_young_modulus)
        self.steel_young_modulus_entry.pack()

        self.reinforcement = tk.StringVar()
        reinforcement_label = tk.Label(self, text="Stopień zbrojenia", font=style.entryLabelFont)
        reinforcement_label.pack()
        self.reinforcement_entry = tk.Entry(self, textvariable=self.reinforcement)
        self.reinforcement_entry.pack()

        self.load = tk.StringVar()
        load_label = tk.Label(self, text="Obciążenie", font=style.entryLabelFont)
        load_label.pack()
        self.load_entry = tk.Entry(self, textvariable=self.load)
        self.load_entry.pack()

        self.section_width = tk.StringVar()
        section_width_label = tk.Label(self, text="Szerokość przekroju", font=style.entryLabelFont)
        section_width_label.pack()
        self.section_width_entry = tk.Entry(self, textvariable=self.section_width)
        self.section_width_entry.pack()

        self.cover = tk.StringVar()
        cover_label = tk.Label(self, text="Otulina", font=style.entryLabelFont)
        cover_label.pack()
        self.cover_entry = tk.Entry(self, textvariable=self.cover)
        self.cover_entry.pack()

        self.diameter = tk.StringVar()
        diameter_label = tk.Label(self, text="Średnica zbrojenia", font=style.entryLabelFont)
        diameter_label.pack()
        self.diameter_entry = tk.Entry(self, textvariable=self.diameter)
        self.diameter_entry.pack()

        self.concrete_strength = tk.StringVar()
        concrete_strength_label = tk.Label(self, text="Wytrzymałość betonu na rozciąganie", font=style.entryLabelFont)
        concrete_strength_label.pack()
        self.concrete_strength_entry = tk.Entry(self, textvariable=self.concrete_strength)
        self.concrete_strength_entry.pack()

        self.concrete_young_modulus = tk.StringVar()
        concrete_young_modulus_label = tk.Label(self, text="Moduł Younga betonu", font=style.entryLabelFont)
        concrete_young_modulus_label.pack()
        self.concrete_young_modulus_entry = tk.Entry(self, textvariable=self.concrete_young_modulus)
        self.concrete_young_modulus_entry.pack()

        # TODO: w obu przypadkach zapis do bazy wyników i nowy dialog/okienko modalne
        # TODO: prezentacja wyników w formie tabeli dla zestawu danych z pliku
        # TODO: prezentacja na pojedynczym polu dla jednej próbki
        # TODO: przycisk generujący raport na podstawie wyników

        button = tk.Button(self, text="Predykuj", font=style.buttonFont, command=self.predict)
        button.pack(pady=style.buttonpady)

    def buttonOnClickPath(self):
        filename = fd.askopenfilename()
        if filename.endswith('.csv'):
            data = pd.read_csv(filename, sep=';')
            self.predict_for_file(data)
        elif filename:
            messagebox.showerror('Błąd!', f'Błędny format pliku: {filename}, plik musi być formatu .CSV')

    def predict_for_file(self, data):
        data = data[['rozpietosc', 'wysokosc przekroju', 'Modul Younga stali', 'stopien zbrojenia', 'Obciazenie',
                     'szerokosc przekroju', 'otulina', 'srednica zbrojenia', 'Wytrzymalosc betonu na rozciaganie',
                     'Modul Younga betonu']]
        results = self.controller.nn.predict(data.to_numpy())
        self.save_results(data, results)
        self.controller.frames[dialog.multiresultdialog.MultiresultDialog].show_results(data, results)
        self.controller.show_frame(dialog.multiresultdialog.MultiresultDialog)

    def save_results(self, data, results):
        for index, row in data.iterrows():
            parameters = {
                "span": row['rozpietosc'],
                "section_height": row['wysokosc przekroju'],
                "steel_young_modulus": row['Modul Younga stali'],
                "reinforcement_grade": row['stopien zbrojenia'],
                "load": row['Obciazenie'],
                "section_width": row['szerokosc przekroju'],
                "cover": row['otulina'],
                "reinforcement_diameter": row['srednica zbrojenia'],
                "concrete_tensile_strength": row['Wytrzymalosc betonu na rozciaganie'],
                "concrete_young_modulus": row['Modul Younga betonu']
            }
            DataBase().insert_result(parameters, str(round(results[index, 0], 5)), os.environ.get('currentUser'))

    def predict(self):
        if (self.span_entry.get() == '' or 
                self.section_height_entry.get() == '' or 
                self.steel_young_modulus_entry.get() == '' or 
                self.reinforcement_entry.get() == '' or 
                self.load_entry.get() == '' or 
                self.section_width_entry.get() == '' or 
                self.cover_entry.get() == '' or
                self.diameter_entry.get() == '' or
                self.concrete_strength_entry.get() == '' or
                self.concrete_young_modulus_entry.get() == ''
            ):
            messagebox.showerror('Błąd!', 'Żadne z pól nie może być puste!')
            return

        try:
            float(self.span_entry.get())
            float(self.section_height_entry.get())
            float(self.steel_young_modulus_entry.get())
            float(self.reinforcement_entry.get())  
            float(self.load_entry.get()) 
            float(self.section_width_entry.get())  
            float(self.cover_entry.get()) 
            float(self.diameter_entry.get()) 
            float(self.concrete_strength_entry.get()) 
            float(self.concrete_young_modulus_entry.get())
        except:
            messagebox.showerror('Błąd', 'Nieprawidłowy format danych. Dane powinny być liczbą')
            return

        X = np.array([[float(self.span.get()), float(self.section_height.get()), float(self.steel_young_modulus.get()),
                      float(self.reinforcement.get()), float(self.load.get()), float(self.section_width.get()),
                      float(self.cover.get()), float(self.diameter.get()), float(self.concrete_strength.get()),
                      float(self.concrete_young_modulus.get())]])

        result = self.controller.nn.predict(X)[0, 0]
        parameters = {
            "span": self.span.get(),
            "section_height": self.section_height.get(),
            "steel_young_modulus": self.steel_young_modulus.get(),
            "reinforcement_grade": self.reinforcement.get(),
            "load": self.load.get(),
            "section_width": self.section_width.get(),
            "cover": self.cover.get(),
            "reinforcement_diameter": self.diameter.get(),
            "concrete_tensile_strength": self.concrete_strength.get(),
            "concrete_young_modulus": self.concrete_young_modulus.get()
        }
        result = str(round(result, 5))
        DataBase().insert_result(parameters, result, os.environ.get('currentUser'))
        messagebox.showinfo("Sukces!", "Predykcja wynosi: %s" % result)
        self.span_entry.delete(0, 'end')
        self.section_height_entry.delete(0, 'end')
        self.steel_young_modulus_entry.delete(0, 'end')
        self.reinforcement_entry.delete(0, 'end')
        self.load_entry.delete(0, 'end')
        self.section_width_entry.delete(0, 'end')
        self.cover_entry.delete(0, 'end')
        self.diameter_entry.delete(0, 'end')
        self.concrete_strength_entry.delete(0, 'end')
        self.concrete_young_modulus_entry.delete(0, 'end')
