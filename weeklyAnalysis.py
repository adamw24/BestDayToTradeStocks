import numpy as np
import datetime
import csv
import matplotlib.pyplot as plt

fileName = "TSLA.csv"


def main():
    plotAverage(fileName)
    plt.title(
        "Relative price of " + fileName[0:-4] + " for every day of the week over the past year")
    plt.yticks([], [])
    plt.xticks(np.arange(0, 5, 1), [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    plt.xlabel("Day of the Week")
    plt.show()


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


# Plots the average/relative closing price at each day of the week, as well as the 95% confidence interval for each day.
def plotAverage(fileName):
    dayOfWeek, closingPrice = parseData(fileName)
    totalPrice = [[], [], [], [], []]
    for i in range(len(dayOfWeek)):
        index = dayOfWeek[i]
        totalPrice[index].append(closingPrice[i])
    avg = []
    dev = []
    for i in range(5):
        avg.append(np.mean(totalPrice[i]))
        dev.append(1.96*np.std(totalPrice[i])/avg[i])
    plt.errorbar(np.arange(0, 5, 1), avg, dev, linestyle='None', marker='^')
    plt.plot(np.arange(0, 5, 1), avg)


if __name__ == '__main__':
    main()
