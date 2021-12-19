import time
import random
import multiprocessing
import itertools
import math

TIME_TO_SLEEP = 2

def rest(time_spent, timer):
	periods = math.ceil(time_spent / timer)
	return (TIME_TO_SLEEP - time_spent) % TIME_TO_SLEEP , periods

def sleepy_man1():
    print('Man 1 is starting to sleep')
    time_to_sleep = TIME_TO_SLEEP * (1.5 - random.random())
    time.sleep(time_to_sleep)
    print('Man 1 done sleeping')

def sleepy_man2():
    print('Man 2 starting to sleep')
    time_to_sleep = TIME_TO_SLEEP * (1.5 - random.random())
    time.sleep(time_to_sleep)
    print('Man 2  done sleeping')

sleepy_people = [sleepy_man1, sleepy_man2]
 
sleepy_people = itertools.cycle(sleepy_people)
if __name__ == '__main__':
    period = 0
    time_diff = 0
    tic = time.time()
    for person in sleepy_people:
        local_tic = time.time()
        p =  multiprocessing.Process(target=person, args=())
        p.start()
        p.join()
        toc = time.time()
        time_spent = toc - local_tic
        print(f'Done in {time_spent:.4f} seconds')
        sleep, task_periods = rest(time_spent, TIME_TO_SLEEP)
        period += task_periods
        #print(period)
        time.sleep(sleep - time_diff)
        if task_periods == 1:
            print(f'Done early, wait {sleep:.4f} seconds')
        else:
            print(f'Done later, wait {sleep:.4f} seconds')
        
        local_toc = time.time()
        time_diff = local_toc - tic - TIME_TO_SLEEP * period
        print(f'{local_tic % TIME_TO_SLEEP} Period accuracy {time_diff:.4f} seconds')
        