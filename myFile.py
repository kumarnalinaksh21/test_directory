import sys
import json

n = len(sys.argv) #total arguments passed to the script
m = ""
c = 0

def CheckAndReturn(): 
    global n, m, c

    for i in range(1, n): #Forming message from the argument
        m = m + sys.argv[i] + " "

    for i in m: #counting number of characters in the message
        c = c + 1
    c = c - 1 #removing the count for the space character at the end of the message

    myDict = { "message" : m, "characters" : c}
    myDict = json.dumps(myDict, indent=4)
    print(myDict)
    return myDict
    


CheckAndReturn()