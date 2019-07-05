import csv
import numpy as np
import matplotlib.pyplot as plt

with open('snelheden.csv', 'r') as csvFile:
    posities = csv.reader(csvFile, delimiter=';')
    tijd = []
    beginPunt = []
    auto1 = []
    auto2 = []
    auto3 = []
    i=0
    for row in posities:
        if i == 0:
            beginPunt = [float(row[1]), float(row[2]), float(row[3])]
            i = 1
        else:
            tijd.append(float(row[0]))
            auto1.append(float(row[1]))
            auto2.append(float(row[2]))
            auto3.append(float(row[3]))

auto_1 = []
auto_2 = []
auto_3 = []
def intBerekenen(autoSoort,autoLijst):
    for i in range(len(tijd) - 1):
        intgr = np.trapz(autoSoort[0:i+2],tijd[0:i+2])
        autoLijst.append(intgr)
    return autoLijst

print(intBerekenen(auto1,auto_1)[:10])
print(intBerekenen(auto2,auto_2))
print(intBerekenen(auto3,auto_3))

plt.plot(tijd[1:],auto_1, label='auto 1')
plt.plot(tijd[1:],auto_2, label='auto 2')
plt.plot(tijd[1:],auto_3, label='auto 3')
plt.legend()
plt.show()

csvFile.close()