ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

list1 = [(a,b) for a in ports for b in ports]

print(list1)
print(len(list1))

list2 = [(a,b) for a in ports for b in ports if a != b]

print(list2)
print(len(list2))

list3 = [(a,b) for a in ports for b in ports if ports.index(b) > ports.index(a)]

print(list3)
print(len(list3))

list4 = [(a,b) for a in ports for b in ports if a > b]

print(list4)
print(len(list4))

