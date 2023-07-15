import csv
import matplotlib.pyplot as plt


f = open('data.CSV')
data = CSV.reader(f)
next(data)
high = []
low = []

for row in data:
        if row[-1]!=''and row [-2]
            if 23.03 <= int(row[0].split('~')[0]):
                    if row [0].split('-')[1] == '02' and row[0].split('-')
[2] == '22' :

            high.appand(float(row[-1]))
            low.append(float(row[-2]))
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()
