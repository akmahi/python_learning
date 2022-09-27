class Descriptor(object):
    # def __init__(self, name=None):
    #     print("Initialized")
    #     self.property_name = name

    def __set_name__(self, owner, name):
        self.property_name = name
        print(f"proerty name {name}")

    def __set__(self, instance, value=None):
        print("SET Called")
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.property_name] or None


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