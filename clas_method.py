
class Validmethod:
    name = "Ajith"

    def __init__(self):
        self.school = "S S S"

    @classmethod
    def change_clas(cls, name):
        cls.name = name

    def change_obj(self, school):
        self.school = school
