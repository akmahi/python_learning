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

class As:
    name = "Ajith"

    def changename(self, name):
        self.name - name

print(As.name)
obj = As()
obj.name = "kumar"
print(obj.name)
print(As.name)
