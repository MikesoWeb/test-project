from plus_def import name


# name = 'from globals()'

def a():
    # name = 'is a()'

    def b():
        # name = 'is b()'
        print(name)
        print(locals())

    b()


a()
