import csv
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 2.5, 2 # mean and standard deviation
depth = np.random.normal(mu, sigma, 1000)

count = 0
# height = 0
# inflow = 0
# outflow = 0
# rain = 0
# # output = 0
# for i in range(1000):
# 	if depth[i] < 0:
# 		count = count + 1
# print(count)

# row = []
# for i in range(100):
# 	height = randint(0,3)


# with open('train.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(row)
# writeFile.close()