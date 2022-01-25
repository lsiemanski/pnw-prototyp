import tkinter as tk
import style
import dialog

from tkinter import ttk
from logic.dbservice import DataBase


class HistoryDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = DataBase()
        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Historia obliczeń", font=style.labelFont)
        label.pack(pady=style.labelpady)


        scroll = ttk.Scrollbar(self, orient='horizontal')
        history = ttk.Treeview(self, xscrollcommand=scroll.set)

        history['columns'] = ('rozpiętość', 'wys. przekroju', 'moduł Younga stali', 'stopień zbrojenia', 'obciążenie',
                              'szer. przekroju', 'otulina', 'śr. zbrojenia', 'wytrzymałość betonu',
                              'moduł Younga betonu', 'ugięcie')

        history.column("#0", width=0, stretch=tk.NO)
        history.column("rozpiętość", anchor=tk.CENTER, width=80)
        history.column("wys. przekroju", anchor=tk.CENTER, width=100)
        history.column("moduł Younga stali", anchor=tk.CENTER, width=120)
        history.column("stopień zbrojenia", anchor=tk.CENTER, width=100)
        history.column("obciążenie", anchor=tk.CENTER, width=80)
        history.column("szer. przekroju", anchor=tk.CENTER, width=100)
        history.column("otulina", anchor=tk.CENTER, width=80)
        history.column("śr. zbrojenia", anchor=tk.CENTER, width=100)
        history.column("wytrzymałość betonu", anchor=tk.CENTER, width=120)
        history.column("moduł Younga betonu", anchor=tk.CENTER, width=120)
        history.column("ugięcie", anchor=tk.CENTER, width=80)

        history.heading("#0", anchor=tk.CENTER)
        history.heading("rozpiętość", text="rozpiętość", anchor=tk.CENTER)
        history.heading("wys. przekroju", text="wys. przekroju", anchor=tk.CENTER)
        history.heading("moduł Younga stali", text="moduł Younga stali", anchor=tk.CENTER)
        history.heading("stopień zbrojenia", text="stopień zbrojenia", anchor=tk.CENTER)
        history.heading("obciążenie", text="obciążenie", anchor=tk.CENTER)
        history.heading("szer. przekroju", text="szer. przekroju", anchor=tk.CENTER)
        history.heading("otulina", text="otulina", anchor=tk.CENTER)
        history.heading("śr. zbrojenia", text="śr. zbrojenia", anchor=tk.CENTER)
        history.heading("wytrzymałość betonu", text="wytrzymałość betonu", anchor=tk.CENTER)
        history.heading("moduł Younga betonu", text="moduł Younga betonu", anchor=tk.CENTER)
        history.heading("ugięcie", text="ugięcie", anchor=tk.CENTER)

        history_data = self.db.get_results()
        for result in history_data:
            history.insert(parent='', index='end', iid=0, text='',
                       values=(result['username'], result['span'], result['section_height'], result['steel_young_modulus'], result['reinforcement_grade'
                       ], result['load'], result['section_width'], result['cover'], result['reinforcement_diameter'], result['concrete_tensile_strength'
                       ], result['concrete_young_modulus'], result['result']))


        history.pack()
        scroll.pack(fill=tk.X)
        scroll.config(command=history.xview)

