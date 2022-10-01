
class Validmethod:
    school = "SKA"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_clas(cls, school):
        cls.school = school
        print(cls.__dict__)
    def change_obj(self, name):
        self.name = name

    @staticmethod
    def static_obj():
        return "This is static Method"

obj = Validmethod("Ajith")
print(obj.name)
print(obj.school)
print(obj.static_obj())
obj1 = Validmethod("Mahit")
print(obj1.name)
print(obj1.school)
print(obj1.static_obj())
obj1.change_clas("Metric")
print(obj1.school)
print(obj.school)
print(Validmethod.school)
