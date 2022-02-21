
#1) changing the file to include all the data for the year 2018
#2) change the title to - Daily low and high temperatures - 2018
#3) extract low temps from the file and add to chart
#4) shade in the area bewteen high and low

import csv
from datetime import datetime

open_file = open('sitka_weather_2018_simple.csv','r')

csv_file = csv.reader(open_file,delimiter=',')

header_row = next(csv_file)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []

for row in csv_file:
    lows.append(int(row[6]))
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(current_date)

print(highs)
print(dates)
print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')


plt.fill_between(dates,lows,highs,facecolor='yellow',alpha=0.4)
#three parameters: a-axis, y-point 1, y-point 2
#alpha adjusts transperancy

plt.title("Daily low and high temperatures, July 2018", fontsize=16)
plt.xlabel('Month of July 2018')
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

fig.autofmt_xdate()

#plt.show()

plt.subplot(2,1,1)
#2 rows, 1 column, which index in the graph we are working with (1 = top, 2 = bottom)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c='blue')
plt.title('Lows')

plt.suptitle("Highs and Lows of Sitka, Alaska 2018")

plt.show()