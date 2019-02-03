# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class Switch(object):

    def __init__(self):
        self._unit_name = None
        self._mac_address = None
        self._ip_address = None
        self._login = None
        self._password = None

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.getter
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name_value):
        self._unit_name = unit_name_value

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.getter
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address_value):
        self._mac_address = mac_address_value

    @property
    def ip_adress(self):
        return self._ip_address

    @ip_adress.getter
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address_value):
        self._ip_address = ip_address_value

    @property
    def login(self):
        return self._login

    @login.getter
    def login(self):
        return self._login

    @login.setter
    def login(self, login_value):
        self._login = login_value

    @property
    def password(self):
        return self._password

    @password.getter
    def password(self):
        return self._password

    @password.setter
    def password(self,password_value):
        self._password = password_value


switch1 = Switch()
switch1.unit_name = 'unit1'
switch1.mac_address = '10;3d:6c:19:fe:88'
switch1.ip_address = '10.6.9.168'
switch1.login = 'login1'
switch1.password = 'qwerty'

print(switch1.__dict__)
