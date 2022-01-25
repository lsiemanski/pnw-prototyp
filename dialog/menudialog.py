import tkinter as tk

from sqlalchemy import null
import style
import dialog
from logic.nnlogic import NN
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

        #TODO: weryfikacje roli zalogowanego użytkownika
        button = tk.Button(self, text="Dodaj użytkownika", font=style.buttonFont, command=self.add_user)
        button.pack(pady=style.buttonpady)

        button = tk.Button(self, text="Dodaj dane", font=style.buttonFont, command=self.add_data)
        button.pack(pady=style.buttonpady)

        button = tk.Button(self, text="Wyucz sieć", font=style.buttonFont, command=self.train_network)
        button.pack(pady=style.buttonpady)

        button = tk.Button(self, text="Predykcja", font=style.buttonFont, command=self.predict)
        button.pack(pady=style.buttonpady)

        button = tk.Button(self, text="Historia obliczeń", font=style.buttonFont, command=self.show_history)
        button.pack(pady=style.buttonpady)

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

    def update_user(self):
        user_name = os.environ.get('currentUser')
        self.labelCurrentUser.config(text=f'Zalogowano jako: {user_name}')

    def quit(self):
        exit(0)
