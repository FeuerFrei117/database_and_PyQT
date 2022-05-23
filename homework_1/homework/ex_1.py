'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
(Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! Крайне желательно использование потоков.)
'''
import platform
import subprocess
from ipaddress import ip_address
from tabulate import tabulate

result = {'Доступные узлы': [], 'Недоступные узлы': []}

def check_is_ipaddress(value):
    try:
        ipv4 = ip_address(value)
    except ValueError:
        raise Exception('Некорректный ip адрес')
    return ipv4

def host_ping(hosts_list, get_list=False):
    print('Начинаю проверку доступности хостов')
    for host in hosts_list:
        try:
            ipv4 = check_is_ipaddress(host)
        except Exception as e:
            print(f'{host} - {e} воспринимаю как доменное имя')
            ipv4 = host

        param = '-n' if platform.system().lower()=='windows' else '-c'

        response = subprocess.Popen(['ping', param, '1', '-w', '1', str(ipv4)],
                                    stdout=subprocess.PIPE)
        if response.wait() == 0:
            result['Доступные узлы'].append(f'{ipv4}')
        else:
            result['Недоступные узлы'].append(f'{ipv4}')
    if get_list:
        return result


if __name__ == '__main__':

    hosts_list = ['192.168.8.1', '8.8.8.8', 'yandex.ru', 'google.com',
                  '0.0.0.1', '0.0.0.2', '0.0.0.3', '0.0.0.4', '0.0.0.5',
                  '0.0.0.6', '0.0.0.7', '0.0.0.8', '0.0.0.9', '0.0.1.0']

    host_ping(hosts_list)
    print(tabulate(result, headers='keys', tablefmt='pipe'))