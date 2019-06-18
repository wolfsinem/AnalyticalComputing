import csv
import matplotlib.pyplot as plt

filename = 'utrecht.csv'
gegevens1 = ['gemiddelde','mediaan','modus','std']
columns = {}
rows = []
data = {}

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            i = 0
            for c in row:
                columns[c] = i
                data[i] = []
                i += 1
        else:
            line_count += 1
            if 'JJ00' in row[columns['Perioden']]:
                pass
            else:
                rows.append(row)
                i = 0
                for c in row:
                    if is_number(c):
                        data[i].append(int(c))
                    else:
                        data[i].append(c)
                    i = i+1
    # print(f'Processed {line_count} lines.')
    # print(columns)
geboren = data[columns['LevendGeborenKinderen_2']]
overledenen = data[columns['Overledenen_3']]

def sum_lijst(variabele):
    sum = 0
    for x in variabele:
        sum += x
    return sum

def count(variabele):
  item_count = 0
  for x in variabele[:]:
    item_count += 1
  return item_count

def gemiddeldeBerekenen(variabele):
    totaal = 0
    lenoflist = count(variabele)
    for i in variabele:
        totaal += i
    gemiddelde = totaal / lenoflist
    return int(gemiddelde)

def min(variabele):
    min_waarde= 0
    for waarde in variabele:
        if not min_waarde:
            min_waarde = waarde
        elif waarde < min_waarde:
            min_waarde = waarde
    return min_waarde

def max(variabele):
    max_waarde= 0
    for waarde in variabele:
        if not max_waarde:
            max_waarde = waarde
        elif waarde > max_waarde:
            max_waarde = waarde
    return max_waarde

def mediaan(variabele):
    n = count(variabele)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(variabele)[n//2]
    else:
        return sum_lijst(sorted(variabele)[n//2-1:n//2+1])/2.0

def modus(data):
    modecnt=0
    for i in range(count(data)):
        icount = data.count(data[i])
        if icount > modecnt:
            mode = data[i]
            modecnt = icount
    return mode

def kwadraat(data):
    c = gemiddeldeBerekenen(data)
    ss = sum_lijst((x-c)**2 for x in data)
    return ss

def stddev(data):
    n = count((data))
    ss = kwadraat(data)
    pvar = ss/n
    return pvar**0.5

def gegevens(variabelen):
    gemiddelde = gemiddeldeBerekenen(variabelen)
    Mediaan = mediaan(variabelen)
    Modus = modus(variabelen)
    std = stddev(variabelen)
    return gemiddelde, Mediaan, Modus, std

def printGegevens(variabelen):
   gem = ("Gemiddelde: {} ".format(gegevens(variabelen)[0]))
   med = ("Mediaan: {}".format(gegevens(variabelen)[1]))
   mod = ("Modus: {} ".format(gegevens(variabelen)[2]))
   st =  ("Std: {}".format(gegevens(variabelen)[3]))
   return gem,med,mod,st
# for elem in printGegevens(geboren):
#     print(elem)

x = gegevens(geboren)
y = gegevens(overledenen)
plt.plot(gegevens1,x, 'ro', label='geboren')
plt.plot(y, 'go', label='overledenen')
plt.xlabel('gegevens')
plt.ylabel('aantal')
plt.title('statistieken')
plt.legend()
plt.show()