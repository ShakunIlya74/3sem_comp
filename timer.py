import time
from random import random
flag = "a "
max_time = 4
timer = 2

def rest(flo, timer):
	i = 0
	while((flo - timer*i) > 0):
		i+=1
	return (timer*i - flo, i)
	
def func(m_time, flag):
	a = random()
	work = m_time * a
	print("begin ", flag)
	time.sleep(work)
	print("end ", flag, work)
	return work
	
while(True):
	work = func(max_time, flag)
	sleep, i = rest(work, timer)
	print(sleep, i)
	time.sleep(sleep)
    