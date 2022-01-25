import tkinter as tk

import style
import dialog
import os
from tkinter import messagebox


class MenuDialog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Menu główne", font=style.labelFont)
        label.pack(pady=style.labelpady)

        self.labelCurrentUser = tk.Label(self, text='', font=style.labelFont)
        self.labelCurrentUser.pack(pady=style.labelpady)

        self.add_user_button = tk.Button(self, text="Dodaj użytkownika", font=style.buttonFont, command=self.add_user)
        self.add_user_button.pack(pady=style.buttonpady)

        self.add_data_button = tk.Button(self, text="Dodaj dane", font=style.buttonFont, command=self.add_data)
        self.add_data_button.pack(pady=style.buttonpady)

        self.train_button = tk.Button(self, text="Wyucz sieć", font=style.buttonFont, command=self.train_network)
        self.train_button.pack(pady=style.buttonpady)

        self.predict_button = tk.Button(self, text="Predykcja", font=style.buttonFont, command=self.predict)
        self.predict_button.pack(pady=style.buttonpady)

        self.history_button = tk.Button(self, text="Historia obliczeń", font=style.buttonFont, command=self.show_history)
        self.history_button.pack(pady=style.buttonpady)

        button = tk.Button(self, text="Wyjdź", font=style.buttonFont, command=self.quit)
        button.pack(pady=style.buttonpady)

    def add_user(self):
        self.controller.show_frame(dialog.adduserdialog.AddUserDialog)

    def add_data(self):
        self.controller.show_frame(dialog.adddatadialog.AddDataDialog)

    def train_network(self):
        self.controller.nn.train_network()
        messagebox.showinfo("Sukces!", "Sieć została wytrenowana!")

    def predict(self):
        self.controller.show_frame(dialog.predictdialog.PredictDialog)

    def show_history(self):
        self.controller.show_frame(dialog.historydialog.HistoryDialog)
        self.controller.frames[dialog.historydialog.HistoryDialog].update_data()

    def update_user(self):
        user_name = os.environ.get('currentUser')
        self.labelCurrentUser.config(text=f'Zalogowano jako: {user_name}')
        if os.environ.get('userRole') == 'Inżynier':
            self.add_data_button.forget()
        else:
            self.train_button.forget()
            self.add_user_button.forget()
            self.predict_button.forget()
            self.history_button.forget()

    def quit(self):
        exit(0)
