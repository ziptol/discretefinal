# Import plotting packages
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
# Import external classes
import graphBase as gb
import dectobase as db

# Print user prompt
print("\nWould you like to:")
print("1. Graph the number of digits it takes to represent decimal number 'n' in base 2-36")
print("2. Graph the number of digits it takes to represent decimal 1-100000 in base 'n'")

# Take user input
while(1):
    try:
        print("Choice: ",end="")
        userChoice = int(input())
        if(userChoice!=1 and userChoice!=2):
            raise
        break

    except:
        print("Invalid input, please try again")
    
    
# Graph varying bases
if(userChoice == 1):

    # Take user input
    while(1):
        try:
            print("Enter the value you would like to plot: ",end="")
            userValue = int(input())
            break
        except:
            print("Invalid input, please try again")
    
    # Generate list of representations in base 2-36
    arr = db.dectobase(userValue)
    # Generate list of lengths of representations
    lengths = [len(i) for i in arr[0]]
    # X values for plotting
    xvals = [i+2 for i in range(len(lengths))]

    # Generate plot
    plt.step(range(len(lengths)),lengths)
    plt.plot(range(len(lengths)),lengths, 'o--', color='grey', alpha = 0.3)
    plt.ylabel("Number of digits")
    plt.xlabel("Base")
    plt.title("Number of digits to represent "+str(userValue)+" in base 2-36")
    plt.show()

# Graph varying numbers
elif(userChoice == 2):

    # Take user input
    while(1):
            try:
                print("Enter the base you would like to plot: ",end="")
                userValue = int(input())
                if(userValue<2 or userValue>36):
                    raise
                break
            except:
                print("Invalid input, please try again")
    
    
    # Generate input values for graphbase function
    inpvals = [(i*i) for i in range(1,100000)]
    arr = gb.graphBase(userValue, inpvals)

    # Generate plot
    fig,ax = plt.subplots()
    ax.set_xscale('log')
    ax.plot(inpvals, arr[0], '-', color='black')
    plt.ylabel("Number of digits")
    plt.xlabel("Value")
    plt.title("Number of digits to represent 1-1x10^11 in base "+str(userValue))
    plt.show()
