import unittest

from app import App
import logic.dbservice

class DataBaseTest(unittest.TestCase):
    def test_add_user(self):
        db = logic.dbservice.DataBase()
        db.insert_user('michal_test', '1234', 'm.bugno@metrological.com', 'Inzynier')
        self.assertTrue(db.check_login_data('michal_test', '1234'))

    def test_get_results(self):
        db = logic.dbservice.DataBase()
        res = db.get_results()
        self.assertTrue(res != None)

    def test_get_samples(self):
        db = logic.dbservice.DataBase()
        sam = db.get_samples()
        self.assertTrue(sam != None)