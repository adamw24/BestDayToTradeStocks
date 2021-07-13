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
        A = plt.plot(xaxis, avg, marker='.')

        plt.ylabel("Percent gain based on Monday closing price")

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
plotAverage("SPY.csv")
plotAverage("GOOG.csv")
plotAverage("MSFT.csv")
plotAverage("AAPL.csv")
# plotAverage("TSLA.csv")
plotAverage("FB.csv")
plotAverage("NFLX.csv")
plotAverage("KO.csv")

plt.title(
    "Average percent gain each weekday over the past year")
plt.xticks([0, 1, 2, 3, 4], [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
plt.xlabel("Day of the Week")
plt.show()
