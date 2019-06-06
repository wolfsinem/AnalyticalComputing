import numpy as np
import json

with open("gewichten.json") as test:
    lijst = json.load(test)

layer1 = lijst['layer1']['weights']
layer2 = lijst['layer2']['weights']

inputVector = [1,1,1,1,1]

x = []
for i in layer1:
    for j in layer1[i]:
        x.append(float(layer1[i][j]))
x = np.array(x)
x = np.reshape(x,(5,4))
x = x.transpose()
# print(x)

y = []
for i in layer2:
    for j in layer2[i]:
        y.append(float(layer2[i][j]))
y = np.array(y)
y = np.reshape(y,(4,2))
y = y.transpose()
# print(y)

def multiply(M, V):
    m = len(M)
    n = len(V)
    j = 0
    l = []
    while j < m:
        i = 0
        while i < n:
            h = M[j][i] * V[i]
            l += [h]
            i += 1
        j += 1
    w = 0
    hh = 0
    answer = []
    while w < len(l):
        w += n
        s = 0
        for k in l[hh:w]:
            s += k
        hh = hh+n
        answer += [s]
    return answer

hiddenLayer = multiply(x,inputVector)
output = multiply(y,hiddenLayer)

print("Uitkomst voor de hiddenlayer: {} ".format(multiply(x,inputVector)))
print("Output: {}".format(multiply(y,hiddenLayer)))
