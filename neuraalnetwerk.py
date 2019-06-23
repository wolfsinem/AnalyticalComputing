import numpy as np
import json

with open("gewichten.json") as test:
    lijst = json.load(test)

layer1 = lijst['layer1']
layer2 = lijst['layer2']

inputVector = [1,1,1,1,1]

def createMatrix(layer):
    x = int(layer["size_in"])
    y = int(layer["size_out"])
    a = np.zeros((y, x))
    for i in layer["weights"]:
        for key, value in layer["weights"][i].items():
            a[int(key) - 1, int(i) - 1] = float(value)
    return a

x = createMatrix(layer1)
y = createMatrix(layer2)


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


