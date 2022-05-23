from random import *

bias = 0
data = list()
classCheck = ['class-1\n', 'class-2\n', 'class-3\n']
file = open("train.data", 'r')

for i in file:
    data.append(i.split(','))

for i in range(len(data)):
    weight.append([])  # initiate empty rows.
    for j in range(4):
        weight[i].append(0)  # initiate empty columns.
        weight[i][j] = randrange(-1,
                                 1)  # Assign random values to weights, with rows and columns equal to training data.

rowNum = len(data)  # constant for the number of rows.

weight=[0.5,0.5,0.5,0.5]
def perceptron():
    """
    perceptron function

    """

    templist = list()
    for iteration in range (100):
        for row in range(rowNum):  # for each row
            activation = 0  # calculate activation
            if [row] in templist:
                continue
            else:
                for col in range(len(data[row])):  # the reason we use length of data instead of directly stating 4,
                    # is to make sure the program can fit data of any number of columns
                    if col == 4:
                        if activation in range(0, 1)  and data[row][4] == classCheck[0]:  # class-1 check
                                templist.append([row])  # add the row to a list of successfully activated rows.
                                print('success ' + data[row][4])

                        elif activation in range(1, 2) and data[row][4] == classCheck[1]:  # class-2 check
                                templist.append([row])
                                print('success ' + data[row][4])


                        elif activation in range(2, 3) and data[row][4] == classCheck[2]:  # class-3 check
                                templist.append([row])
                                print('success ' + data[row][4])
                        else:
                            updateWeight(row, activation)

                        continue  # since data[4] is the class, skip this iteration.
                    activation += float(weight[col]) * float(data[row][col]) + bias

    print(templist)


def updateWeight(iteration,activation):
    global classCheck,bias,weight
    if data[iteration][4]== classCheck[0]:
        d=-1
        error= d-activation
    elif data[iteration][4]== classCheck[1]:
        d=-2
        error = d - activation
    elif data[iteration][4]== classCheck[2]:
        d=-3
        error = d - activation
    for i in range(4):
        f=2.5*float(data[iteration][i])*float(error)
        weight[i]=weight[i]*f
        #bias=bias+weight[i]+f



perceptron()
