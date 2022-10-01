#single inheritance
#
# class Vehicle:
#
#     def disp(self):
#         return "This is vehicle"
#
#
# class Car(Vehicle):
#
#     def name(self):
#         return "This is car"
#
#
# obj = Car()
# print(obj.name())
# print(obj.disp())

#multiple Inheritance

# class Car:
#
#     def name(self):
#         return "This is car"
#
#
# class Bike:
#
#     def name(self):
#         return "This is bike"
#
#
# class Vehicle(Car, Bike):
#
#     def disp(self):
#         return self.name()
#
#     def name(self):
#         return "This is Vehicle"
#
#
# obj = Vehicle()
# print(obj.name())

#multi level Inheritance

# class Car:
#
#     def name(self):
#         return "This is car"
#
#
# class Vehicle(Car):
#     def disp(self):
#         return "This is Vehicle"
#
#
# class Bike(Vehicle):
#
#     def model(self):
#         return "This is bike"
#
#
# obj = Bike()
# print(obj.name())
# print(obj.model())
# print(obj.disp())

#hybrid inheritance
#herirical inheritance

#Super in python2
# class Area(object):
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_area(self):
#         return self.length * self.width
#
#
# class Square(Area):
#
#     def __init__(self, length):
#         super(Square, self).__init__(length, length)
#
#
# obj = Square(2)
# print(obj.get_area())

#############Super in python3

# class Area:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_area(self):
#         return self.length * self.width
#
#
# class Square(Area):
#
#     def __init__(self, length):
#         super().__init__(length, length)
#
#
# obj = Square(2)
# print(obj.get_area())


###############################multiple inheritance with Super()

class Area:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def para(self):
        return "This is Area class"


class Side:

    def __init__(self, side):
        self.side = side

    def get_side(self):
        return self.side

    def para(self):
        return "This is side class"


class Square(Area, Side):

    def __init__(self, length, side):
        Area.__init__(self,length, length)
        Side.__init__(self,side)

    def get_para(self):
        return Side.para(self)


obj = Square(2, 4)
print(obj.get_area())
print(obj.get_side())
print(obj.get_para())



