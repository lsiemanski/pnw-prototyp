import unittest

from app import App
import logic.dbservice

class DataBaseTest(unittest.TestCase):
    def test_get_results(self):
        db = logic.dbservice.DataBase()
        db.insert_result({
            "span": 0.1,
            "section_height": 0.1,
            "steel_young_modulus": 0.1,
            "reinforcement_grade": 0.1,
            "load": 0.1,
            "section_width": 0.1,
            "cover": 0.2,
            "reinforcement_diameter": 0.1,
            "concrete_tensile_strength": 0.1,
            "concrete_young_modulus": 0.1
        }, 0.1, 'michal_test')
        res = db.get_results()
        self.assertTrue(res != None)

    def test_get_samples(self):
        db = logic.dbservice.DataBase()
        db.insert_sample({
            "span": 0.1,
            "section_height": 0.1,
            "steel_young_modulus": 0.1,
            "reinforcement_grade": 0.1,
            "load": 0.1,
            "section_width": 0.1,
            "cover": 0.2,
            "reinforcement_diameter": 0.1,
            "concrete_tensile_strength": 0.1,
            "concrete_young_modulus": 0.1
        }, 0.1)
        sam = db.get_samples()
        self.assertTrue(sam != None)