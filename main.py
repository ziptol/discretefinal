import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import graphBase as gb
import dectobase as db

print("\nWould you like to:")
print("1. Graph the number of digits it takes to represent decimal number 'n' in base 2-36")
print("2. Graph the number of digits it takes to represent decimal 1-100000 in base 'n'")
print("Choice: ")
userChoice = int(input())

if(userChoice == 1):
    print("Enter the value you would like to plot: ")
    userValue = int(input())
    arr = db.dectobase(userValue)
    lengths = [len(i) for i in arr[0]]
    xvals = [i+2 for i in range(len(lengths))]

    plt.step(range(len(lengths)),lengths)
    plt.plot(range(len(lengths)),lengths, 'o--', color='grey', alpha = 0.3)
    plt.ylabel("Number of digits")
    plt.xlabel("Base")
    plt.title("Number of digits to represent "+str(userValue)+" in base 2-36")
    plt.show()

elif(userChoice == 2):
    print('Enter the base you would like to plot: ')
    userValue = int(input())
    fig,ax = plt.subplots()
    ax.set_xscale('log')
    inpvals = [(i*i) for i in range(1,100000)]
    arr = gb.graphBase(userValue, inpvals)

    ax.plot(inpvals, arr[0], '-', color='black')
    plt.ylabel("Number of digits")
    plt.xlabel("Value")
    plt.title("Number of digits to represent 1-1x10^5 in base "+str(userValue))
    plt.show()
