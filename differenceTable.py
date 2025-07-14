import numpy as np
# import pandas as pd

def f(x):
    return np.exp(x)

x_values = []
diffTable = []
y_values = []

def getDiffTable(y_values, iter=0):
    
    y_values2 = y_values[1:]
    for i in range(len(y_values2)):
        y_values2[i] = y_values2[i] - y_values[i]
    diffTable.append(y_values)
    # print(len(y_values))
    if(iter == 4 ):
        return 0
    else:
        getDiffTable(y_values2, iter+1)
    
    


def main():
    
    for i in range(-10,10+1, 1):
        x_values.append(i/10)
        y_values.append(f(i/10))
        
    getDiffTable(y_values)
    
    print("--------------------------------------------------------------------------")
    print("                        1st      2nd      3rd      4th ")
    print("S.N.    x      y       Order    Order    Order    Order ")
    print("--------------------------------------------------------------------------")
    
    for j in range(len(diffTable[0])):
        string = ""
        str0 = f" {j}    {x_values[j]}   {diffTable[0][j]:.4f}"
        string += str0
        if(j<len(diffTable[1])):
            str1 = f"   {diffTable[1][j]:.4f}"
            string += str1
        if(j<len(diffTable[2])):
            str2 = f"   {diffTable[2][j]:.4f}"
            string += str2
        if(j<len(diffTable[3])):
            str3 = f"   {diffTable[3][j]:.4f}"
            string += str3
        if(j<len(diffTable[4])):
            str4 = f"   {diffTable[4][j]:.4f}"
            string += str4
        print(string)

main()

# if "__name__" == "__main__":
#     main()
