import time
import random
import multiprocessing
import itertools

TIME_TO_SLEEP = 10



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
    tic = time.time()
    for person in sleepy_people:
        local_tic = time.time()
        p =  multiprocessing.Process(target=person)
        p.start()
        p.join()
        toc = time.time()
        time_spent = toc - local_tic
        print(f'Done in {time_spent:.4f} seconds')
        if time_spent < TIME_TO_SLEEP:
            time_to_wait = (toc - tic) % TIME_TO_SLEEP
            print(f'Done early, wait {time_to_wait:.4f} seconds')
            time.sleep((toc - tic) % TIME_TO_SLEEP)