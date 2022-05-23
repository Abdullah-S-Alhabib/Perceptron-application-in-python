import math
from random import *

# import math
# import matplotlib.pyplot as plt

errSum = list()
bias = 0
data = list()
test1 = list()
classCheck = ['class-1\n', 'class-2\n', 'class-3\n']
file = open("train.data", 'r')
file1 = open('test.data', 'r')

weight = [[1, 1, -1, -1], [1, 1, -1, -1], [1, 1, -1, -1]]
for i in file:
    data.append(i.split(','))

for j in file1:
    test1.append(j.split(','))

rowNum = len(data)  # constant for the number of rows.
rowNum1 = len(test1)

# random function to shuffle rows
shuffle(data)


def test2():
    """
    Test function, runs the test data on the already trained weights.
    :return: no return
    """
    global templist1
    templist1 = list()

    # for each row
    for row in range(rowNum1):

        sVal = []  # sigmoid values of the perceptron
        classtemp = 0  # temporary holder for the class number

        for classiter in range(3):
            # test for each class
            if classCheck[classiter] == data[row][4]:
                classtemp = classiter
            sVal.append(perceptronTest(row, classiter))
        # if the highest sVal represents the currect class, add to list.
        if sVal[classtemp] == max(sVal):
            templist1.append(row)
        else:
            continue


def perceptronTest(row, classiter):
    """
    The testing perceptron, uses a sigmoid function to test input.
    :param row: Row number for the input.
    :param classiter: class number to test against.
    :return: sigmoid activation value.
    """
    wSum = bias  # initiate weight sum with bias because we will add to it.
    # the reason we use length of data instead of directly stating 4, is to make sure the program can fit data of any number of columns
    for col in range(len(data[row]) - 1):
        # Calculate weight sum
        wSum += float(weight[classiter][col]) * float(data[row][col])

    activation = 1 / (1 + math.exp(-wSum))

    return activation


def perceptron(classiter):
    """
    main perceptron training function, uses an activation function to test input and train weights.
    :param classiter: the predicted class to train on.
    :return:
    """
    global templist
    y = 0
    templist = list()

    for row in range(rowNum):  # for each row
        activation = 0  # set/reset activation
        if data[row][4] == classCheck[classiter]:
            continue
        else:
            # run through each class with class iteration
            if classiter == 0:
                if data[row][4] == classCheck[1]:
                    y = -1
                elif data[row][4] == classCheck[2]:
                    y = 1
                for col in range(len(data[row]) - 1):  # the reason we use length of data instead of directly stating 4,
                    # is to make sure the program can fit data of any number of columns
                    activation += float(weight[classiter][col]) * float(data[row][col]) + bias

                if y * activation <= 0:
                    updateWeight(row, y, classiter)
                else:
                    if row not in templist:
                        templist.append(row)
            elif classiter == 1:
                if data[row][4] == classCheck[2]:
                    y = -1
                elif data[row][4] == classCheck[0]:
                    y = 1
                for col in range(len(data[row]) - 1):
                    activation += float(weight[classiter][col]) * float(data[row][col]) + bias

                if y * activation <= 0:
                    updateWeight(row, y, classiter)
                else:
                    if row not in templist:
                        templist.append(row)
            elif classiter == 2:
                if data[row][4] == classCheck[0]:
                    y = -1
                elif data[row][4] == classCheck[1]:
                    y = 1
                for col in range(len(data[row]) - 1):
                    activation += float(weight[classiter][col]) * float(data[row][col]) + bias

                if y * activation <= 0:
                    updateWeight(row, y, classiter)
                else:
                    if row not in templist:
                        templist.append(row)


def updateWeight(row, y, classiter):
    """
    update the weights to get closer to expected value
    :param row: Row number
    :param y: expected output
    :param classiter: current class iteration
    """
    global classCheck, bias, weight, errSum
    for i in range(len(data[row]) - 1):
        weight[classiter][i] = float(weight[classiter][i]) + y * float(data[row][i])
        bias += y


def main():
    """
    main function for the program.
    """
    # run the training
    for iteration in range(35):
        for classiter in range(3):
            perceptron(classiter)
    print('Weights =', weight)
    print('Training accuracy: ' + str(len(templist) / len(data) * 100))

    # run the test.
    test2()

    print('Test accuracy: ' + str(len(templist1) / len(test1) * 100))


main()
