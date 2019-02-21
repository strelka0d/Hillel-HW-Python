# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).


class Singleton(type):
    """
    Class for creating Singletons
    """

    clsdict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.clsdict:
            cls.clsdict[cls] = super().__call__(*args, **kwargs)
        return cls.clsdict[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()

assert id(c) == id(b)

print(c)
print(b)

