ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen1 = ((a,b) for a in ports for b in ports)

amount = 0
for i in gen1:
    print(i)
    amount += 1

print(amount)
print(30 * "-")

gen2 = ((a,b) for a in ports for b in ports if a != b)

amount = 0
for i in gen2:
    print(i)
    amount += 1

print(amount)
print(30 * "-")

gen3 = ((a,b) for a in ports for b in ports if ports.index(b) > ports.index(a))

amount = 0
while True:
    try:
        print(next(gen3))
        amount += 1
    except:
        print("Koniec")
        break

print(amount)

