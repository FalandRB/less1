def my_gen(start, stop):
    while True:
        if start > stop:
            raise StopIteration
        yield start
        start += 1

start = int(input('От скольки считаем? '))
stop = int(input('До скольки считаем? '))

for i in my_gen(start, stop):
    if i % 3 != 0:
        print(i)
    else:
        print('Василий')
