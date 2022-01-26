import unittest

from app import App
import dialog.multiresultdialog
import logic.dbservice as db
import os
from os.path import exists

class MultiresultDialogTest(unittest.TestCase):
    def test_generate_report(self):
        app = App()
        multi_result_dialog = dialog.multiresultdialog.MultiresultDialog(app.container, app)
        multi_result_dialog.show_results()
        multi_result_dialog.generate_report()
        self.assertTrue(exists('report.csv'))