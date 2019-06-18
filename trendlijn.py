import csv
import matplotlib.pyplot as plt

filename = 'utrecht.csv'
jaren = ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']

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
                rows.append(row)
                i = 0
                for c in row:
                    if is_number(c):
                        data[i].append(int(c))
                    else:
                        data[i].append(c)
                    i = i+1

aantalGeboren = data[4]

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


y = aantalGeboren
N = count(y)
x = range(N)
A = (sum_lijst(x[i] * y[i] for i in range(N)) - 1./N*sum_lijst(x)*sum_lijst(y)) / (sum_lijst(x[i]**2 for i in range(N)) - 1./N*sum_lijst(x)**2)
B = sum_lijst(y)/N - A * sum_lijst(x)/N
# print("( %f * x ) + %f " % (A,B))

predict=[A*index + B for index in range(10)]
# print(predict)


plt.plot(jaren,aantalGeboren,'ro',label='geboren')
plt.plot([A*index + B for index in range(17)],'g',label='trendlijn')
plt.xticks(rotation=90)
plt.xlabel('jaren')
plt.ylabel('aantal')
plt.legend()
plt.title('Kinderen levend geboren')
plt.show()


