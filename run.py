import os, sys
from src.main import Main
import time

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

inp = input("Type in the text you want to print: ")
print("Trying to print \"%s\".. Hold up\n"%inp)
start = time.time()
try:
    Main(inp)
except KeyboardInterrupt:
    print("\nExiting :(")
    sys.exit()
print("\n^-^ printed finally! (took %s seconds)"%round(time.time()-start,2))