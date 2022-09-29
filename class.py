# class As:
#     name="ajith"
#     pass

#Access through class
# print(As.name)
#Access through Object
# s = As()
# print(s.name)

# class As:
#     name = "Ajith"
#     pass
#
# print(As.name)
# As.name = "kumar"
# s = As()
# print(s.name)
# s.name = "dollyy"
# print(s.name)
# print(As.name)

# class As:
#     #class Attribute
#     name = "Ajith"
#
#     def changename(self, name):
#         #instance Atrribute
#         self.name - name
#
# print(As.name)
# obj = As()
# obj.name = "kumar"
# print(obj.name)
# print(As.name)

class As:
    #class Attribute
    name = "Ajith"

    def changename(self, name):
        #instance Atrribute
        self.name1 = name

obj = As()
obj1 = As()
obj.changename("kk")
del obj.name1
# print(obj.name1)
del obj1
print(obj1.name)


