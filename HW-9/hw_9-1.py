# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить

import re


class EmailDescriptor:
    """
    Descriptor that checks e-mails
    """

    def __get__(self, instance, owner):
        print(self._email)
        return self._email

    def __set__(self, instance, email_value):
        pattern = r"([\w\.-]+)@([\w\.-]+).([\w\.]+)"
        if re.match(pattern, email_value):
            self._email = email_value
            return self._email
        else:
            raise Exception('Not valid e-mail')



class MyClass:
    check_email = EmailDescriptor()


my_class = MyClass()
my_class.check_email = "validemail@gmail.com"
my_class.check_email

my_class.check_email = "novalidemail"
my_class.check_email
# Raised Exception
