# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)

class IP_adresses(object):

    def __init__(self, lst_ip):
        self._lst_ip = lst_ip

    def getip(self):
        return self._lst_ip

    def deployip(self):
        res = []
        for ip in self._lst_ip:
            res.append('.'.join(ip.split('.')[::-1]))
        return res

    def threelastoktet(self):
        res = []
        for ip in self._lst_ip:
            res.append('.'.join(ip.split('.')[1:]))
        return res

    def last_oktet(self):
        res = []
        for ip in self._lst_ip:
            res.append(ip.split('.')[3])
        return res


ip = IP_adresses(['10.11.12.13', '10.6.4.7'])

print(ip.getip())
print(ip.deployip())
print(ip.threelastoktet())
print(ip.last_oktet())
