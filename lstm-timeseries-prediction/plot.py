#!/usr/bin/python
#
# author:
#
# date:
# description:
#
import pandas
import matplotlib.pyplot as plt

dataset = pandas.read_csv('../data/international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()
