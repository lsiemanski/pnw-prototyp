import unittest

from app import App
import dialog


class MenuDialogTest(unittest.TestCase):
    def test_add_user(self):
        app = App()
        menu_dialog = dialog.menudialog.MenuDialog(app.container, app)
        menu_dialog.add_user()
        self.assertEqual(type(app.frame), dialog.adduserdialog.AddUserDialog)

    def test_add_data(self):
        app = App()
        menu_dialog = dialog.menudialog.MenuDialog(app.container, app)
        menu_dialog.add_data()
        self.assertEqual(type(app.frame), dialog.adddatadialog.AddDataDialog)

    def test_predict(self):
        app = App()
        menu_dialog = dialog.menudialog.MenuDialog(app.container, app)
        menu_dialog.predict()
        self.assertEqual(type(app.frame), dialog.predictdialog.PredictDialog)

    def test_show_history(self):
        app = App()
        menu_dialog = dialog.menudialog.MenuDialog(app.container, app)
        menu_dialog.show_history()
        self.assertEqual(type(app.frame), dialog.historydialog.HistoryDialog)
