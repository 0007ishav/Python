username = "strnge"

# def test():
#     pass

# if True:
#     pass

# def func():
#     username = "chai"
#     print(username)

# print(username)
# func()

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x   # Dont try to do this.
#     x  = 88

# func3()
# print(x)

def f1():
    x = 77
    def f2():
        print(x)
    f2()
f1()