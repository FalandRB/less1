import re
from collections import Counter

#Функция чтения
def reader(filename):
    #Патерны
    ip_exp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    #Не успеваю дойти до RE конкретного браузера, но в целом логика такая
    br_exp = r'"."(.*?)" '
    #Читаем файл
    with open(filename) as f:
        log = f.read()
        ips = re.findall(ip_exp, log)
        browsers = re.findall(br_exp, log)
        count_ip = Counter(ips)
        count_br = Counter(browsers)
        for i in range (len(ips)):
            print(ips[i], '\n')
        print('Всего обращений:', len(ips))
        print('Уникальных IP:', len(count_ip))
        print('Все UserAgents:', count_br)
        print('От каждого UA:', len(count_br))
    #Вернем что надо, если надо
    return True

#Запуск функции
reader('d:/prog/less1/apache/error.log')

