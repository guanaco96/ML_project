from network import *
from gradient_descent import *
from utility import *

import csv
import numpy as np
import random

def preprocess_monks(filename, val_split=0.05):
    train_data = []
    with open("monks/"+filename+".train") as infile:
        reader = csv.reader(infile, delimiter=" ")
        for row in reader:
            label = np.array([int(row[1]), 1 - int(row[1])])
            data = np.zeros(17)
            data[int(row[2]) - 1] = 1
            data[int(row[3]) + 2] = 1
            data[int(row[4]) + 5] = 1
            data[int(row[5]) + 7] = 1
            data[int(row[6]) + 10] = 1
            data[int(row[7]) + 14] = 1
            train_data.append((data, label))
    print("Loaded {} train datapoints".format(len(train_data)))

    test_data = []
    with open("monks/"+filename+".test") as infile:
        reader = csv.reader(infile, delimiter=" ")
        for row in reader:
            label = np.array([int(row[1]), 1 - int(row[1])])
            data = np.zeros(17)
            data[int(row[2]) - 1] = 1
            data[int(row[3]) + 2] = 1
            data[int(row[4]) + 5] = 1
            data[int(row[5]) + 7] = 1
            data[int(row[6]) + 10] = 1
            data[int(row[7]) + 14] = 1
            test_data.append((data, label))
    print("Loaded {} test datapoints".format(len(test_data)))

    n = int(val_split*len(train_data))
    random.shuffle(train_data)

    return train_data[:n], train_data[n:], test_data

val, train, test = preprocess_monks("monks-1")


lrate = 0.1
mu = 0.001
epochs = 3000
beta = 0.95

size_list = [17, 15, 2]
network = Network(size_list, reLU, softMax, mu)

algo = GradientDescent(crossEntropy, lrate, epochs, network)
algo.train(train, val, beta)
print("TOPOLOGIA = " + str(size_list))
print("Train = " + str(network.accuracy(train))) 
print("Validation = " + str(network.accuracy(val)))
print("Test = " + str(network.accuracy(test)))