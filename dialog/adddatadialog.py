import tkinter as tk
from unittest import result

import dialog.abstractdialog
import style
import pandas as pd 
from tkinter import Button, messagebox, ttk, filedialog as fd
import logic.dbservice as dataBase
import re


class AddDataDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        scroll = ttk.Scrollbar(self, orient='vertical')

        label = tk.Label(self, text="Dodaj dane eksperymentalne", font=style.labelFont)
        label.pack(pady=style.labelpady)


        buttonPath = tk.Button(self, text="Wybierz plik", font=style.buttonFont, command=lambda: self.buttonOnClickPath())
        buttonPath.pack(pady=style.buttonpady)

        or_label = tk.Label(self, text="LUB:", font=style.entryLabelFont)
        or_label.pack()



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
        self.result_entry = tk.Entry(self, textvariable=self.result)
        self.result_entry.pack()

        ok_button = tk.Button(self, text="Dodaj dane", font=style.buttonFont, command=lambda: self.buttonOnClickManual())
        ok_button.pack(pady=style.buttonpady)



    def buttonOnClickPath(self):
        filename = fd.askopenfilename()
        if filename.endswith('.csv'):
            data = pd.read_csv(filename, sep=';')
            #print(data)
            counter = 0
            for index, row in data.iterrows():
                #self.write_to_database(row[0])
                counter += 1
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
                self.write_to_database(param=parameters, res=row[10])
                messagebox.showinfo('OK', f'Wprowadzono {counter} rekordów do bazy danych.')

        else:
            messagebox.showerror('Błąd!', f'Błędny format pliku: {filename}, plik musi być formatu .CSV')

    def buttonOnClickManual(self):

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
            float(self.result_entry.get())
        except:
            messagebox.showerror('Błąd', 'Nieprawidłowy format danych. Dane powinny być liczbą')
            return
        
    
        param = {'span': float(self.span_entry.get()),
                'section_height': float(self.section_height_entry.get()),
                'steel_young_modulus': float(self.steel_young_modulus_entry.get()),
                'reinforcement_grade': float(self.reinforcement_entry.get()),
                'load': float(self.load_entry.get()),
                'section_width': float(self.section_width_entry.get()),
                'cover': float(self.cover_entry.get()),
                'reinforcement_diameter': float(self.diameter_entry.get()),
                'concrete_tensile_strength': float(self.concrete_strength_entry.get()),
                'concrete_young_modulus': float(self.concrete_young_modulus_entry.get())
                }
        self.write_to_database(param=param, res=float(self.result_entry.get()))

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
        self.result_entry.delete(0, 'end')

        messagebox.showinfo('', 'Dodano do bazy danych')

    def write_to_database(self, param, res):
        db = dataBase.DataBase()
        db.insert_sample(parameters=param, result=res)



