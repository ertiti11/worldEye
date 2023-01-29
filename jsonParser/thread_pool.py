# SuperFastPython.com
# example of a concurrent for loop that is more responsive
from time import sleep
from random import random
from multiprocessing.pool import ThreadPool
 
# task to execute in another thread
def task(arg):
    # generate a value between 0 and 1
    value = random()
    # block for a fraction of a second to simulate work
    sleep(value)
    # return the generated value
    return value
 
# entry point for the program
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # call the same function with different data concurrently
        for result in pool.imap(task, range(1000)):
            # report the value to show progress
            print(result)