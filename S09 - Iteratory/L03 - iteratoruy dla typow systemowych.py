import csv

with open(r'D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S09 - Iteratory\PLIKI\plik.csv', newline='')\
        as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))

    # print(next(csvfile))
    # print(next(csvfile))
    # print(next(csvreader))
    # print(next(csvreader))

    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break