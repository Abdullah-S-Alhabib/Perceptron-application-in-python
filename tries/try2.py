from random import *

bias = 0
data = list()
classCheck = ['class-1\n', 'class-2\n', 'class-3\n']
file = open("train1.data", 'r')
weight = list()
for i in file:
    data.append(i.split(','))
weight=[0.25,-0.25,0.25,0.25]
#for i in range(len(data)):
#    weight.append([])  # initiate empty rows.
#    for j in range(4):
#        weight[i].append(0)  # initiate empty columns.
#        weight[i][j] = randrange(-1,
#                                 1)  # Assign random values to weights, with rows and columns equal to training data.

rowNum = len(data)  # constant for the number of rows.

def perceptron(classiter):
    """
    perceptron function

    """
    y=0
    templist = list()

    for iteration in range (3):
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
                    for col in range(len(data[row])-1):  # the reason we use length of data instead of directly stating 4,
                        # is to make sure the program can fit data of any number of columns
                        activation += float(weight[col]) * float(data[row][col]) + bias
                        if y*activation <= 0:
                            updateWeight(row,activation,y)
                        else:
                            if row not in templist:
                                templist.append(row)



    print(templist)


def updateWeight(row,activation,y):
    global classCheck,bias,weight
    for i in range(len(data[row])-1):
        weight[row][i] = float(weight[row][i]) + y*(float(data[row][i]))
        bias +=y



def main():
    for classiter in range(3):
        perceptron(classiter)

main()