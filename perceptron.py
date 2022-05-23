from random import *
#import math
#import matplotlib.pyplot as plt

errSum = list()
bias = 0
data = list()
test1 = list()
classCheck = ['class-1\n', 'class-2\n', 'class-3\n']
file = open("train1.data", 'r')
file1 = open('test.data','r')

weight = [1, 1, -1, -1]
for i in file:
    data.append(i.split(','))

for j in file1:
    test1.append(i.split(','))

rowNum = len(data)  # constant for the number of rows.
rowNum1 = len(test1)

# random function to shuffle rows
shuffle(data)
def test2(classiter):
    global templist1
    """
    perceptron function

    """
    y = 0
    templist1 = list()

    for row in range(rowNum1):  # for each row
        activation = 0  # calculate activation
        if classiter == 0:
            if test1[row][4] == classCheck[1]:
                y = -1
            elif test1[row][4] == classCheck[2]:
                y = 1
            for col in range(
                    len(test1[row]) - 1):  # the reason we use length of test instead of directly stating 4,
                # is to make sure the program can fit data of any number of columns
                activation += float(weight[col]) * float(test1[row][col]) + bias
            if activation * y >0:
                if row not in templist1:
                    templist1.append(row)



        elif classiter == 1:
            if test1[row][4] == classCheck[2]:
                y = -1
            elif test1[row][4] == classCheck[0]:
                y = 1
            for col in range(
                    len(test1[row]) - 1):  # the reason we use length of test instead of directly stating 4,
                # is to make sure the program can fit data of any number of columns
                activation += float(weight[col]) * float(test1[row][col]) + bias
            for col in range(
                    len(test1[row]) - 1):  # the reason we use length of test instead of directly stating 4,
                # is to make sure the program can fit data of any number of columns
                activation += float(weight[col]) * float(test1[row][col]) + bias
            if activation * y >0:
                if row not in templist1:
                    templist1.append(row)
        elif classiter == 2:
            if test1[row][4] == classCheck[0]:
                y = -1
            elif test1[row][4] == classCheck[1]:
                y = 1
            for col in range(
                    len(test1[row]) - 1):  # the reason we use length of test instead of directly stating 4,
                # is to make sure the program can fit data of any number of columns
                activation += float(weight[col]) * float(test1[row][col]) + bias
            if activation * y >0:
                if row not in templist1:
                    templist1.append(row)


def perceptron(classiter):
    global templist
    """
    perceptron function

    """
    y = 0
    templist = list()


    for row in range(rowNum):  # for each row
        activation = 0  # calculate activation
        if data[row][4] == classCheck[classiter]:
            continue
        else:
            if classiter == 0:
                if data[row][4] == classCheck[1]:
                    y = -1
                elif data[row][4] == classCheck[2]:
                    y = 1
                for col in range(
                        len(data[row]) - 1):  # the reason we use length of data instead of directly stating 4,
                    # is to make sure the program can fit data of any number of columns
                    activation += float(weight[col]) * float(data[row][col]) + bias

                if y * activation <= 0:
                    updateWeight(row, y)
                else:
                    if row not in templist:
                        templist.append(row)
            elif classiter == 1:
                if data[row][4] == classCheck[2]:
                    y = -1
                elif data[row][4] == classCheck[0]:
                    y = 1
                for col in range(
                        len(data[row]) - 1):  # the reason we use length of data instead of directly stating 4,
                    # is to make sure the program can fit data of any number of columns
                    activation += float(weight[col]) * float(data[row][col]) + bias

                if y * activation <= 0:
                    updateWeight(row, y)
                else:
                    if row not in templist:
                        templist.append(row)
            elif classiter == 2:
                if data[row][4] == classCheck[0]:
                    y = -1
                elif data[row][4] == classCheck[1]:
                    y = 1
                for col in range(
                        len(data[row]) - 1):  # the reason we use length of data instead of directly stating 4,
                    # is to make sure the program can fit data of any number of columns
                    activation += float(weight[col]) * float(data[row][col]) + bias

                if y * activation <= 0:
                    updateWeight(row, y)
                else:
                    if row not in templist:
                        templist.append(row)


def updateWeight(row, y):
    global classCheck, bias, weight, errSum
    loss = 0
    for i in range(len(data[row]) - 1):
        #loss += -(y * math.log10(float(weight[i])) + (1 - y) * math.log10(1 - float(weight[i])))
        weight[i] = float(weight[i]) + y * float(data[row][i])
        bias += y
    #errSum.append([loss,row])



def main():
    for iteration in range(30):
        for classiter in range(3):
            perceptron(classiter)
    #for i in range(len(templist)):
        #print(data[templist[i]][4])
    print('weights =',weight)
    print('perceptron accuracy ')
    print(len(templist)/len(data)*100)
    for classiter in range(3):
        test2(classiter)
    #for k in range(len(templist1)):
        #print(test1[templist1[k]][4])
    print('weights =',weight)
    print('Test accuracy ')
    print(len(templist1) / len(test1) * 100)


   #plt.plot(errSum[1],errSum[0])
   #plt.xlabel('row number')
   #plt.ylabel('Cross entropy loss')

   #plt.title('Error graph')

   #plt.show()


main()
