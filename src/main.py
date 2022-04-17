from random import randint
import time

def Main(string:str):
    newStr = ""
    ind = 0
    while True:
        time.sleep(0.05)
        #generate a random printable ascii char
        ch = chr(randint(65,122))
        #test patience
        if string.startswith(newStr+ch):
            newStr+=ch
            print("\r"+newStr,end="")
            ind+=1
            try:
                if ord(string[ind])==32:
                    newStr+=" "
                    ind += 1
            except IndexError:
                pass
        else:
            print("\r"+newStr+ch,end="")
        #break when success
        if newStr==string:
            break