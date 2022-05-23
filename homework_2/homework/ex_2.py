'''
2. Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1) для перебора ip-адресов из
заданного диапазона. Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться
соответствующее сообщение.
'''

from ex_1 import host_ping
from ipaddress import ip_address
from tabulate import tabulate

def host_range_ping():
    while True:
        try:
            start_ip = ip_address(input('Введите первоночальный адрес: '))
            break
        except BaseException:
            print('Вы ввели не корректный ip адрес')

    end_ip = int(input('Сколько адресов проверить: '))

    while int(str(start_ip).split('.')[3]) + end_ip > 256:
        print(f'Можем менять только последний октет, '
              f'т.е. максимальное число хостов: {256 - int(str(start_ip).split(".")[3])}')
        end_ip = int(input('Сколько адресов проверить: '))

    ip_address_list = [start_ip + i for i in range(end_ip)]

    return host_ping(ip_address_list, get_list=True)


if __name__ == '__main__':
    print(tabulate(host_range_ping(), headers='keys', tablefmt='pipe'))