import csv
import numpy as np
import matplotlib.pyplot as plt

with open('posities.csv', 'r') as csvFile:
    posities = csv.reader(csvFile, delimiter=';')
    tijd = []
    auto1 = []
    auto2 = []
    for row in posities:
        tijd.append(float(row[0]))
        auto1.append(float(row[1]))
        auto2.append(float(row[2]))

tijdVerschil = np.diff(tijd)
snelheid_x1 = np.diff(auto1) / tijdVerschil
snelheid_x2 = np.diff(auto2) / tijdVerschil
tijd_y = (np.array(tijd)[:1] + np.array(tijd)[1:]) / 2

print("Auto 1: minimum snelheid {} en maximum snelheid {}.".format(round(min(snelheid_x1),2),round(max(snelheid_x1),2)))
print("Auto 2: minimum snelheid {} en maximum snelheid {}.".format(round(min(snelheid_x2),2),round(max(snelheid_x2),2)))

plt.plot(tijd_y,snelheid_x1)
plt.title('snelheid auto 1')
plt.xlabel('tijd')
plt.ylabel('snelheid')
plt.show()

plt.plot(tijd_y,snelheid_x2)
plt.title('snelheid auto 2')
plt.xlabel('tijd')
plt.ylabel('snelheid')
plt.show()

csvFile.close()