import tkinter as tk

import dialog.abstractdialog
import style
from tkinter import ttk, messagebox


class MultiresultDialog(dialog.abstractdialog.AbstractDialog):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Wyniki", font=style.labelFont)
        label.pack(pady=style.labelpady)

        button = tk.Button(self, text="Generuj raport", font=style.buttonFont, command=self.generate_report)
        button.pack(anchor=tk.NE, pady=style.buttonpady, padx=style.buttonpadx)

        scroll_y = ttk.Scrollbar(self, orient='vertical')
        self.history = ttk.Treeview(self, yscrollcommand=scroll_y.set, height=50)

        scroll_y.pack(fill=tk.Y, side=tk.RIGHT)
        scroll_y.config(command=self.history.yview)

        self.history['columns'] = ('rozpiętość', 'wys. przekroju', 'moduł Younga stali', 'stopień zbrojenia', 'obciążenie',
                              'szer. przekroju', 'otulina', 'śr. zbrojenia', 'wytrzymałość betonu',
                              'moduł Younga betonu', 'ugięcie')

        self.history.column("#0", width=0, stretch=tk.NO)
        self.history.column("rozpiętość", anchor=tk.CENTER, width=80)
        self.history.column("wys. przekroju", anchor=tk.CENTER, width=100)
        self.history.column("moduł Younga stali", anchor=tk.CENTER, width=120)
        self.history.column("stopień zbrojenia", anchor=tk.CENTER, width=100)
        self.history.column("obciążenie", anchor=tk.CENTER, width=80)
        self.history.column("szer. przekroju", anchor=tk.CENTER, width=100)
        self.history.column("otulina", anchor=tk.CENTER, width=80)
        self.history.column("śr. zbrojenia", anchor=tk.CENTER, width=100)
        self.history.column("wytrzymałość betonu", anchor=tk.CENTER, width=120)
        self.history.column("moduł Younga betonu", anchor=tk.CENTER, width=120)
        self.history.column("ugięcie", anchor=tk.CENTER, width=80)

        self.history.heading("#0", anchor=tk.CENTER)
        self.history.heading("rozpiętość", text="rozpiętość", anchor=tk.CENTER)
        self.history.heading("wys. przekroju", text="wys. przekroju", anchor=tk.CENTER)
        self.history.heading("moduł Younga stali", text="moduł Younga stali", anchor=tk.CENTER)
        self.history.heading("stopień zbrojenia", text="stopień zbrojenia", anchor=tk.CENTER)
        self.history.heading("obciążenie", text="obciążenie", anchor=tk.CENTER)
        self.history.heading("szer. przekroju", text="szer. przekroju", anchor=tk.CENTER)
        self.history.heading("otulina", text="otulina", anchor=tk.CENTER)
        self.history.heading("śr. zbrojenia", text="śr. zbrojenia", anchor=tk.CENTER)
        self.history.heading("wytrzymałość betonu", text="wytrzymałość betonu", anchor=tk.CENTER)
        self.history.heading("moduł Younga betonu", text="moduł Younga betonu", anchor=tk.CENTER)
        self.history.heading("ugięcie", text="ugięcie", anchor=tk.CENTER)

        self.history.pack()


    def show_results(self, data, results):
        self.data = data
        self.results = results
        for i in self.history.get_children():
            self.history.delete(i)
        for index, result in data.iterrows():
            self.history.insert(parent='', index='end', iid=index, text='',
                                values=(result['rozpietosc'], result['wysokosc przekroju'],
                                        result['Modul Younga stali'], result['stopien zbrojenia'],
                                        result['Obciazenie'], result['szerokosc przekroju'], result['otulina'],
                                        result['srednica zbrojenia'],
                                        result['Wytrzymalosc betonu na rozciaganie'], result['Modul Younga betonu'],
                                        results[index, 0]))

    def generate_report(self):
        self.data['Ugięcia'] = self.results
        self.data.to_csv('report.csv', index=False, sep=';')
        messagebox.showinfo("Sukces!", "Wygenerowano raport!")

