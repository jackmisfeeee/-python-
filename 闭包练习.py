def outer():
    def inner():
        print("hello world")

    return inner


f = outer()
f()
