
stringNumber = 1

with open("results.txt") as f: 
    for line in f:  
        print(str(stringNumber) + ". " + line)  
        stringNumber += 1  

# We used the str() to convert a variable of type integer to a string.
