import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pd
import analysisUsingCSV

# Uses the Pandas get_data_yahoo method to get the data of the specific asset. Returns the closing price and the day of the week.
# dayOfWeek is a list of 0, 1, 2, 3, 4 that represent Monday, Tuesday, Wednesday, Thursday, and Friday respectively.


def parseData(tickerName, start, end):

    closingPrice = []
    date = []
    hist = pd.get_data_yahoo(tickerName, start, end)
    for i in range(len(hist["Close"])):
        closingPrice.append(round(hist["Close"][i], 6))
        date.append(hist.index[i].date().weekday())

    closingPrice = list(map(float, closingPrice))
    return date, closingPrice


# returns the average percent gain of each day of the week based on the Monday price from the start date to end date inclusive.
def plotAverage(tickerName, start, end):
    dayOfWeek, closingPrice = parseData(tickerName, start, end)
    eachDayPrice = [[], [], [], [], []]
    for i in range(len(dayOfWeek)):
        index = dayOfWeek[i]
        eachDayPrice[index].append(closingPrice[i])

    avg = []
    mondayavg = np.mean(eachDayPrice[0])
    for i in range(5):
        avg.append((np.mean(eachDayPrice[i])-mondayavg)/mondayavg*100)
    return avg


def main():
    xaxis = np.arange(0, 5, 1)
    plot1 = plt.figure(1)
    s, = plt.plot(xaxis, plotAverage(
        "SPY", "2020-7-12", "2021-7-12"), marker='.')
    g, = plt.plot(xaxis, plotAverage(
        "GOOG", "2020-7-12", "2021-7-12"), marker='.')
    m, = plt.plot(xaxis, plotAverage(
        "MSFT", "2020-7-12", "2021-7-12"), marker='.')
    a, = plt.plot(xaxis, plotAverage(
        "AAPL", "2020-7-12", "2021-7-12"), marker='.')
    # t, = plt.plot(xaxis, plotAverage("TSLA", "2020-7-12", "2021-7-12"), marker='.')
    f, = plt.plot(xaxis, plotAverage(
        "FB", "2020-7-12", "2021-7-12"), marker='.')
    n, = plt.plot(xaxis, plotAverage(
        "NFLX", "2020-7-12", "2021-7-12"), marker='.')
    k, = plt.plot(xaxis, plotAverage(
        "KO", "2020-7-12", "2021-7-12"), marker='.')

    plt.title(
        "Average percent gain each weekday over the past two years")
    analysisUsingCSV.graphLabels(s, g, m, a, f, n, k)

    plot2 = plt.figure(2)
    s, = plt.plot(xaxis, plotAverage(
        "SPY", "2019-7-13", "2021-7-12"), marker='.')
    g, = plt.plot(xaxis, plotAverage(
        "GOOG", "2019-7-13", "2021-7-12"), marker='.')
    m, = plt.plot(xaxis, plotAverage(
        "MSFT", "2019-7-13", "2021-7-12"), marker='.')
    a, = plt.plot(xaxis, plotAverage(
        "AAPL", "2019-7-13", "2021-7-12"), marker='.')
    # t, = plt.plot(xaxis, plotAverage("TSLA", "2019-7-13", "2021-7-12"), marker='.')
    f, = plt.plot(xaxis, plotAverage(
        "FB", "2019-7-13", "2021-7-12"), marker='.')
    n, = plt.plot(xaxis, plotAverage(
        "NFLX", "2019-7-13", "2021-7-12"), marker='.')
    k, = plt.plot(xaxis, plotAverage(
        "KO", "2019-7-13", "2021-7-12"), marker='.')

    plt.title(
        "Average percent gain each weekday over the past two years")
    analysisUsingCSV.graphLabels(s, g, m, a, f, n, k)

    plt.show()


if __name__ == '__main__':
    main()

# Debugging the difference between CSV data and Pandas data.
# a = auc.parseData("GOOG2.csv")
# b = parseData("GOOG", "2019-7-13", "2021-7-12")
# for i in range(len(b[0])):
#     print(a[1][i] - b[1][i])


# b = parseData("GOOG", "2019-7-13", "2021-7-13")
# print(b[0][-1], b[1][-1])
