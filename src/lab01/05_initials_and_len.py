fio = input('Введите ФИО: ')
fio_ = fio.strip()
fio_2 = fio.split()
inic = ''.join(x[0].upper() for x in fio_2)
len_fio = len(fio_)-len(fio_2)-1
print('Инициалы:',inic)
print('Длина (символов):', len_fio)

