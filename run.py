from random import randint
import os, time

os.system('cls')

st = "Hello World"

def Main(string:str):
    newStr = ""
    if len(newStr)==0:
        newStr = string[0]
    while True:
        time.sleep(0.2)
        ch = chr(randint(65,122))
        if string.startswith(newStr+ch):
            newStr+=ch
            print("\r"+newStr,end="")
            print()
        else:
            print("\r"+newStr+ch,end="")
        if newStr==string:
            break
Main("Hello")