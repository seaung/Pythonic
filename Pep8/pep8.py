variable = 1

bvariable = 12 if variable >= 1 else bvariable = 21

print(bvariable)


class Foo:
    
    def __init__(self, id=1, name=""):
        self.id = id
        self.name = name

    def foo(self):
        return self.id

    @classmethod
    def goo(cls):
        print("cls")
       

def func(name=None):
    pass


def function():
    return 0


class Bar:

    def __init__(self, name):
        self._name = name

    def __say(self):
        print("my name is %s" % (self._name))
    

CONST = 1

if CONST:
    print("const")


