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



class Foo:
    name = Descriptor()
    age = Descriptor()
    # pass

if __name__ == "__main__":
    obj = Foo()
    obj.name = "Ajith"
    obj.age = 26
    print(obj)
    print(obj.name, obj.age)
    # obj.name = "Kumar"
    print(obj.name, obj.age)

# class RequiredString:
#     def __set_name__(self, owner, name):
#         self.property_name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#
#         return instance.__dict__[self.property_name] or None
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'The {self.property_name} must be a string')
#
#         if len(value) == 0:
#             raise ValueError(f'The {self.property_name} cannot be empty')
#
#         instance.__dict__[self.property_name] = value
#
#
# class Person:
#     first_name = RequiredString()
#     last_name = RequiredString()
#
#
# try:
#     person = Person()
#     person.first_name = ''
# except ValueError as e:
#     print(e)