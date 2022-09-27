# class Foo():
#     def __init__(self, name):
#         self.name = name
#
#     def disp(self):
#         return self.name
#
# obj = Foo(name="Ajith")
# print(obj.disp())
# print(obj.name)


# class Foo():
#     def __init__(self, name):
#         self.__name = name
#
#     def disp(self):
#         return self.__name
#
#     def set(self, val):
#         self.__name = val
#
# obj = Foo(name="Ajith")
# print(obj.disp())
# obj.set("kumar")
# print(obj.disp())
# print(obj.__name)

# class Foo():
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, val):
#         self.__name = val
#
#
# obj = Foo(name="Ajith")
# print(obj.name)
# obj.name = "kumar"
# print(obj.name)
# print(obj.__name)


class Descriptor():
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Foo(Descriptor):
    name = Descriptor()


obj = Foo(name="Ajith")
print(obj.name)


