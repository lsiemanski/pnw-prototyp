import tkinter as tk
import style
from tkinter import ttk


class MultiresultDialog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Wyniki", font=style.labelFont)
        label.pack(pady=style.labelpady)

        scroll_y = ttk.Scrollbar(self, orient='vertical')
        self.history = ttk.Treeview(self, yscrollcommand=scroll_y.set, height=10)

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

