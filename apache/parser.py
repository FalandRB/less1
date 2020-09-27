import re
from collections import Counter


def reader(filename):
    ip_exp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(filename) as f:
        log = f.read()
        ips = re.findall(ip_exp, log)
        count = Counter(ips)
        print('Всего обращений:', len(ips))
        print('Уникальных IP:', len(count))
    return ips


reader('123.log')
