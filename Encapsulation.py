
# Encapsulation using Public Access

# class EnpPub:
#     salary = 100
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age =age
#
#     def get_details(self):
#         return 'Employee name is {} and age is {}'.format(self.name, self.age)
#
#     def Age(self):
#         return self.age
#
#
# obj = EnpPub("ajith", 26)
# print(obj.get_details())
# print(obj.name)
# print(obj.age)
# print(obj.salary)
# print(obj.Age())


# Encapsulation using Private Access

# class EnpPri:
#     __salary = 100
#     __leave = 2
#
#     def __init__(self):
#         pass
#
# class OvrPri(EnpPri):
#     def __init__(self):
#         print(self.__leave)
#
# obj = EnpPri()
# # print(obj.salary)
# # print(obj.leave)
# print(dir(obj))
# print(obj._EnpPri__salary)
# obj1 = OvrPri()


# Encapsulation using Protected Access

# class EnpPro:
#     _salary = 100
#     _leave = 2
#
#     def __init__(self):
#         pass
#
#
# class OvrPri(EnpPro):
#     def __init__(self):
#         print(self._leave)
#
#
# obj = EnpPro()
# print(obj._salary)
# print(obj._leave)
# print(dir(obj))
# print(obj._EnpPri__salary)
# obj1 = OvrPri()


# Encapsulation Access private and protected member using getter/setter/@property method

class EnpPubPri:
    _name = "ajith"
    __age = 26

    def __init__(self):
        pass

    def getter(self):
        return self._name

    def setter(self, name):
        self._name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Exact(EnpPubPri):

    def __init__(self):
        print(self._name)
        # print(self.__age)

    def setter(self, name):
        # super.setter(name)
        self._name = name

    @property
    def get_age(self):
        return EnpPubPri.__dict__.get('__age')


obj = EnpPubPri()
# print(obj.getter())
# obj.setter("mahit")
# print(obj.getter())
# print(obj.age)
# obj.age = "3"
# print(obj.age)
obj1 = Exact()
print(obj1.getter())
obj1.setter("mahit")
print (obj1.getter())
print(obj1.get_age)
