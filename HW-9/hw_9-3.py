# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен. каждый экземпляр класса должен иметь свое значение

class IntegerField:
    """
    Descriptor for saving unique status
    """

    def __get__(self, instance, owner):
        return instance.__dict__['number']

    def __set__(self, instance, num_value):
        instance.__dict__['number'] = num_value


class Data:
    number = IntegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
data_row.number

new_data_row.number = 10
new_data_row.number

print(data_row.__dict__)
print(new_data_row.__dict__)

assert data_row.number != new_data_row.number
