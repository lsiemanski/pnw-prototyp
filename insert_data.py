import numpy as np
import pandas as pd

from logic.dbservice import DataBase
from logic.nnlogic import NN

df = pd.read_csv("data.csv", sep=';')
db = DataBase()

if len(db.get_samples()) == 0:
    for index, row in df.iterrows():
        parameters = {
            "span": row['rozpietosc'],
            "section_height": row['wysokosc przekroju'],
            "steel_young_modulus": row['Modul Younga stali'],
            "reinforcement_grade": row['stopien zbrojenia'],
            "load": row['Obciazenie'],
            "section_width": row['szerokosc przekroju'],
            "cover": row['otulina'],
            "reinforcement_diameter": row['srednica zbrojenia'],
            "concrete_tensile_strength": row['Wytrzymalosc betonu na rozciaganie'],
            "concrete_young_modulus": row['Modul Younga betonu']
        }
        db.insert_sample(parameters, row['Ugięcia'])

samples = np.array(list(map(lambda sample: list(sample.values()), db.get_samples())))
X, Y = np.split(samples, [-1], axis=1)


print(NN().predict(np.array([X[100]])))
print(Y[100])
