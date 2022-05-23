'''
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок
'''

from ex_2 import host_range_ping
from tabulate import tabulate

def host_range_ping_tab():
    return tabulate(host_range_ping(), headers='keys', tablefmt='pipe', stralign='center')

if __name__ == '__main__':
    print(host_range_ping_tab())
