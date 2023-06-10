import csv
import matplotlib.pyplot as plt
f = open('data.csv')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] !='':
        result.append(float(row[-1]))

plt.plot(resultn,'r')
plt.show()