import tkinter as tk
from unittest import result

from pytest import param
import dialog.abstractdialog
import style
import pandas as pd 
from tkinter import Button, messagebox, ttk, filedialog as fd
import logic.dbservice as dataBase


class AddDataDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        scroll = ttk.Scrollbar(self, orient='vertical')
        
        #scroll.pack(fill=tk.Y)
        #scroll.config(command=self.controller. xview)

        label = tk.Label(self, text="Dodaj dane eksperymentalne", font=style.labelFont)
        label.pack(pady=style.labelpady)

        # TODO: sekcja pierwsza - dodaj dane z pliku
        # TODO: użytkownik ładuje plik csv, z którego dane zostają przeniesione do bazy
        # TODO: sprawdzić jakoś format pliku i czy się liczba kolumn zgadza
        # TODO: jak coś się nie zgadza to komunikat


        buttonPath = tk.Button(self, text="Wybierz plik", font=style.buttonFont, command=lambda: self.buttonOnClickPath())
        buttonPath.pack(pady=style.buttonpady)

        or_label = tk.Label(self, text="LUB:", font=style.entryLabelFont)
        or_label.pack()


        # =================================

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

        self.result = tk.StringVar()
        result_label = tk.Label(self, text="Znany wynik", font=style.entryLabelFont)
        result_label.pack()
        self.result_label_entry = tk.Entry(self, textvariable=self.result)
        self.result_label_entry.pack()

        ok_button = tk.Button(self, text="Dodaj dane", font=style.buttonFont, command=lambda: self.buttonOnClickManual())
        ok_button.pack(pady=style.buttonpady)



    def buttonOnClickPath(self):
        filename = fd.askopenfilename()
        if filename.endswith('.csv'):
            data = pd.read_csv(filename, sep=';')
            #print(data)
            for index, row in data.iterrows():
                #self.write_to_database(row[0])
                print(row[0], row[1])
                param = {
                'span': row[2],
                'section_height': row[1],
                'steel_young_modulus': row[6],
                'reinforcement_grade': row[3],
                'load': row[9],
                'section_width': row[0],
                'cover': row[5],
                'reinforcement_diameter': row[4],
                'concrete_tensile_strength': row[8],
                'concrete_young_modulus': row[7]
                }
                # 0 szerokosc przekroju;
                # 1 wysokosc przekroju;
                # 2 rozpietosc;
                # 3 stopien zbrojenia;
                # 4 srednica zbrojenia;
                # 5 otulina;
                # 6 Modul Younga stali;
                # 7 Modul Younga betonu;
                # 8 Wytrzymalosc betonu na rozciaganie;
                # 9 Obciazenie;
                # 10 Ugięcia

                self.write_to_database(param=param, res=row[10])

        else:
            messagebox.showerror('Błąd!', f'Błędny format pliku: {filename}, plik musi być formatu .CSV')

    def buttonOnClickManual(self):
        param = {'span': self.span_entry.get(),
                'section_height': self.section_height_entry.get(),
                'steel_young_modulus': self.steel_young_modulus_entry.get(),
                'reinforcement_grade': self.reinforcement_entry.get(),
                'load': self.load_entry.get(),
                'section_width': self.section_width_entry.get(),
                'cover': self.cover_entry.get(),
                'reinforcement_diameter': self.diameter_entry.get(),
                'concrete_tensile_strength': self.concrete_strength_entry.get(),
                'concrete_young_modulus': self.concrete_young_modulus_entry.get()
                }
        self.write_to_database(param=param, res=self.result_label_entry.get())

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
        self.result_label_entry.delete(0, 'end')

        messagebox.showinfo('', 'Dodano do bazy danych')

    def write_to_database(self, param, res):
        db = dataBase.DataBase()
        db.insert_sample(parameters=param, result=res)
        
        # TODO: sekcja druga - dodaj próbkę
        # TODO: dodanie pól tk.Entry na podstawie których można dodać dane
        # TODO: zapis tych danych do bazy
        # TODO: dodanie przycisku, który dodaje



