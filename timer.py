import time
from random import random

MAX_TIME = 1
	
def func(flag):
	work =  MAX_TIME * (random() + 0.5)
	print("begin", flag)
	time.sleep(work)
	print("end", flag, work)

def main():
    flag = "a"
    while True:   
        start = time.time()
        print(start)
        func(flag)
        end = time.time()
        duration = end - start
        time.sleep((MAX_TIME - duration) % MAX_TIME)   
        
if __name__ == "__main__":
    main()

    