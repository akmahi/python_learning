#simple decorator
#Functions are first level object
#Inner function
#High level function
#
# first class object -> we can store function to variable then we can call that variable as a function it also return same o/p while access the function directly
# def hell():
#     return "hii"
#
# s = hell
# print(s())
# print(hell())

# Higher order function => it takes the function as a argument also return the function
# def changeValue(func):
#     def is_alter(a, b):
#         return func(a+b, b)
#     return is_alter

# Inner Function -> function declared inside the another function.it's not surprise, but inner function execute based on function call
# def inher():
#     print("hiii")
#     def inher1():
#         print("hi this is first function")
#     def inher2():
#         print("Hi this is Second function")
#
#     inher1()
#     inher2()
#
# inher()
    # We can't access inner function out side of inher() function.While access this raise NameError
    # But we can acces this inner functions through out side variables.Like

def inher():
    def inn():
        return "hello"
    return inn

s = inher()
print(s())
    # in above code after execute the inher() still inn() had hold the "heelo" value.in which some data attached to code is called closure.
# def changeValue(func):
#     def is_alter(a, b):
#         return func(a+b, b)
#     return is_alter
#
# @changeValue
# def get_value(a, b):
#     print(a, b)
#
#
# if __name__ == "__main__":
#     get_value(2,3)