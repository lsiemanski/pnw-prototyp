import unittest

from app import App
import dialog


class AbstractDialogTest(unittest.TestCase):
    def test_go_to_main_menu(self):
        app = App()
        abstract_dialog = dialog.abstractdialog.AbstractDialog(app.container, app)
        abstract_dialog.go_to_main_menu()
        self.assertEqual(type(app.frame), dialog.menudialog.MenuDialog)
