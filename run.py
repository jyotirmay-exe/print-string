from random import randint
import os, time

os.system('cls')

st = "Hello World"

def Main(string:str):
    newStr = ""
    print(newStr)
    if len(newStr)==0:
        newStr = string[0]
    while True:
        ch = chr(randint(65,122))
        if string.startswith(newStr+ch):
            newStr+=ch
            print(newStr)
            time.sleep(0.2)
Main("Hello")