def calculate_paint(ltrPerM2, *args):
    return sum(args) * ltrPerM2

print(calculate_paint(3, 20, 30, 25))

rooms = [20, 30, 25]

print(calculate_paint(3, *rooms))

def log_it(*args):
    with open(r"D:\Projekty\Kursy Python\Python - Advanced - PyCharm\S04  - funkcje\PLIKI\log.txt", "a") as f:
        for i in args:
            f.write("{}\n".format(i))


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')