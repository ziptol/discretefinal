import matplotlib.pyplot as plt
import numpy as np

print("\nWould you like to:")
print("1. Graph the number of digits it takes to represent decimal number 'n' in base 2-36")
print("2. Graph the number of digits it takes to represent decimal 1-100000 in base 'n'")
print("Choice: ")
userChoice = int(input())


if(userChoice == 1):
    print("1")
    testData = [1,5,10,123,50,12]
    plt.plot(testData)
    plt.show()
elif(userChoice == 2):
    print("2")