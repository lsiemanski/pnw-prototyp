from numpy import true_divide
import tinydb as tdb
import hashlib as hl

class UserError(Exception):
    pass

class DataBase:
    def __init__(self):
        db = tdb.TinyDB("database.json")
        self.users = db.table("users")
        self.samples = db.table("samples")
        self.results = db.table("results")

    def insert_user(self, username, password, email, role):
        password = password.encode()
        user = tdb.Query()
        users = self.users.search(user.username == username)
        if len(users) != 0:
            raise UserError("User already exists!")
        self.users.insert({
            'username' : username,
            'password' : hl.sha256(password).hexdigest(),
            'email' : email,
            'role' : role
        })

    def insert_sample(self, parameters, result):
        self.samples.insert({
            'span': parameters['span'],
            'section_height': parameters['section_height'],
            'steel_young_modulus': parameters['steel_young_modulus'],
            'reinforcement_grade': parameters['reinforcement_grade'],
            'load': parameters['load'],
            'secton_width': parameters['section_width'],
            'cover': parameters['cover'],
            'reinforcement_diameter': parameters['reinforcement_diameter'],
            'concrete_tensile_strength': parameters['concrete_tensile_strength'],
            'concrete_young_modulus': parameters['concrete_young_modulus'],
            'result': result
        })

    def insert_result(self, parameters, result, username):
        self.results.insert({
            'username' : username,
            'span': parameters['span'],
            'section_height': parameters['section_height'],
            'steel_young_modulus': parameters['steel_young_modulus'],
            'reinforcement_grade': parameters['reinforcement_grade'],
            'load': parameters['load'],
            'secton_width': parameters['section_width'],
            'cover': parameters['cover'],
            'reinforcement_diameter': parameters['reinforcement_diameter'],
            'concrete_tensile_strength': parameters['concrete_tensile_strength'],
            'concrete_young_modulus': parameters['concrete_young_modulus'],
            'result': result
        })

    def get_users(self):
        return self.users.all()

    def get_samples(self):
        return self.samples.all()

    def get_results(self):
        return self.samples.all()

    def get_user(self, username):
        user = tdb.Query()
        user = self.users.search(user.username == username)
        if len(user) == 0:
            return None
        return user[0]

    def get_results_for_user(self, username):
        result = tdb.Query()
        return self.results.search(result.username == username)

    def check_login_data(self, username, password):
        user = self.get_user(username)
        if user == None:
            raise UserError("User not found!")
        stored_password = user["password"]
        password = password.encode()
        password = hl.sha256(password).hexdigest()
        if password == stored_password:
            return True
        return False
