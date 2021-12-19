import time
import random
import multiprocessing

TIME_TO_SLEEP = 10


def sleepy_man():
    print('Starting to sleep')
    time_to_sleep = TIME_TO_SLEEP *(1.5 - random.random())
    time.sleep(time_to_sleep)
    print('Done sleeping')


if __name__ == '__main__':
    
    while True:
        tic = time.time()
        p =  multiprocessing.Process(target=sleepy_man)
        p.start()
        p.join()
        toc = time.time()
        time_spent = toc-tic
        print('Done in {:.4f} seconds'.format(time_spent))
        if toc-tic < TIME_TO_SLEEP:
            time.sleep(TIME_TO_SLEEP - time_spent)
            print('Done early, wait {:.4f} seconds'.format(TIME_TO_SLEEP - time_spent))
            