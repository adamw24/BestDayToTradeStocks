import numpy as np
import datetime
import csv
import matplotlib.pyplot as plt


# fig, ax = plt.subplots()


# Parses the csv file in the data folder into the days of the week, and the closing price at each day
# dayOfWeek is a list of 0, 1, 2, 3, 4 that represent Monday, Tuesday, Wednesday, Thursday, and Friday respectively.
def parseData(fileName):
    closingPrice = []
    date = []
    with open("./data/"+fileName, newline="\n") as f:
        reader = csv.reader(f)
        for row in reader:
            closingPrice.append(row[5])
            date.append(row[0])

    closingPrice = closingPrice[1:]
    closingPrice = list(map(float, closingPrice))
    date = date[1:]

    dayOfWeek = []
    for d in date:
        split = d.split("-")
        dayOfWeek.append(datetime.date(
            int(split[0]), int(split[1]), int(split[2])).weekday())
    return dayOfWeek, closingPrice


# Plots all the closing prices of every day for all the weeks (Served as an initial step for the project, but now is for aesthetic purposes)
def plotAllWeeks(fileName):
    dayOfWeek, closingPrice = parseData(fileName)
    weekPrices = []
    weekDay = []

    for i in range(len(dayOfWeek)):
        weekPrices.append(closingPrice[i])
        weekDay.append(dayOfWeek[i])
        if i == len(dayOfWeek)-1 or dayOfWeek[i + 1] < dayOfWeek[i]:
            newWeekPrices = True
            plt.plot(weekDay, weekPrices)
            weekPrices = []
            weekDay = []


# Plots the average percent gain of each day of the week based on the Monday price
def plotAverage(fileName):
    dayOfWeek, closingPrice = parseData(fileName)
    eachDayPrice = [[], [], [], [], []]
    for i in range(len(dayOfWeek)):
        index = dayOfWeek[i]
        eachDayPrice[index].append(closingPrice[i])

    avg = []
    dev = []
    percentGain = True

    if percentGain:
        mondayavg = np.mean(eachDayPrice[0])
        for i in range(5):
            avg.append((np.mean(eachDayPrice[i])-mondayavg)/mondayavg*100)
        #     dev.append(1.96*np.std(eachDayPrice[i]-mondayavg))/avg[i])
        # ax.errorbar(xaxis, avg, dev, linestyle = 'None', marker = '^')
        return avg
        A = plt.plot(xaxis, avg, marker='.')

        plt.ylabel("Percent gain based on Monday closing price")
        return A
        # ax2 = ax.twinx()
        # avg = []
        # dev = []
        # for i in range(5):
        #     avg.append(np.mean(eachDayPrice[i]))
        #     dev.append(1.96*np.std(eachDayPrice[i])/avg[i])
        # ax2.errorbar(xaxis, avg, dev, c='red', marker='.')
        # # ax2.plot(xaxis, avg)
        # ax2.set_ylabel("Average Price ($)", c='red')


xaxis = np.arange(0, 5, 1)
plot1 = plt.figure(1)
s, = plt.plot(xaxis, plotAverage("SPY.csv"), marker='.')
g, = plt.plot(xaxis, plotAverage("GOOG.csv"), marker='.')
m, = plt.plot(xaxis, plotAverage("MSFT.csv"), marker='.')
a, = plt.plot(xaxis, plotAverage("AAPL.csv"), marker='.')
t, = plt.plot(xaxis, plotAverage("TSLA.csv"), marker='.')
f, = plt.plot(xaxis, plotAverage("FB.csv"), marker='.')
n, = plt.plot(xaxis, plotAverage("NFLX.csv"), marker='.')
k, = plt.plot(xaxis, plotAverage("KO.csv"), marker='.')

plt.title(
    "Average percent gain each weekday over the past year")
plt.xticks([0, 1, 2, 3, 4], [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
plt.xlabel("Day of the Week")
plt.ylabel("Percent gain based on Monday closing price")
plt.legend([s, g, m, a, t, f, n, k], [
    "SPY", "GOOG", "MSFT", "AAPL", "TSLA", "FB", "NFLX", "KO"])

plot2 = plt.figure(2)
s, = plt.plot(xaxis, plotAverage("SPY2.csv"), marker='.')
g, = plt.plot(xaxis, plotAverage("GOOG2.csv"), marker='.')
m, = plt.plot(xaxis, plotAverage("MSFT2.csv"), marker='.')
a, = plt.plot(xaxis, plotAverage("AAPL2.csv"), marker='.')
t, = plt.plot(xaxis, plotAverage("TSLA2.csv"), marker='.')
f, = plt.plot(xaxis, plotAverage("FB2.csv"), marker='.')
n, = plt.plot(xaxis, plotAverage("NFLX2.csv"), marker='.')
k, = plt.plot(xaxis, plotAverage("KO2.csv"), marker='.')

plt.title(
    "Average percent gain each weekday over the past two years")
plt.xticks([0, 1, 2, 3, 4], [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
plt.xlabel("Day of the Week")
plt.ylabel("Percent gain based on Monday closing price")
plt.legend([s, g, m, a, t, f, n, k], [
    "SPY", "GOOG", "MSFT", "AAPL", "TSLA", "FB", "NFLX", "KO"])
plt.show()
