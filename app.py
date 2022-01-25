import tkinter as tk

import dialog.adddatadialog
import dialog.historydialog
import dialog.logindialog
import dialog.menudialog
import dialog.adduserdialog
import dialog.predictdialog
from logic.nnlogic import NN


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title('Szacowanie wartości ugięcia belki żelbetowej')
        self.geometry("500x600")

        container = tk.Frame(self)
        container.pack(side="top", fill="x", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.container = container

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.nn = NN()

        for F in (dialog.logindialog.LoginDialog,
                  dialog.menudialog.MenuDialog,
                  dialog.adduserdialog.AddUserDialog,
                  dialog.adddatadialog.AddDataDialog,
                  dialog.historydialog.HistoryDialog,
                  dialog.predictdialog.PredictDialog):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(dialog.logindialog.LoginDialog)

    def show_frame(self, cont):
        frame = self.frames[cont]
        self.frame = frame
        self.frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
