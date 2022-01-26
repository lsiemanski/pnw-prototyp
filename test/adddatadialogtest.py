import unittest

from app import App
import dialog

class AddDataDialogTest(unittest.TestCase):
    def test_adddata(self):
        app = App()
        add_data_dialog = dialog.adddatadialog.AddDataDialog(app.container, app)
        assert(add_data_dialog.controller != None)
