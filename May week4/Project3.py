"""
Write a generator to get even numbers from 1 to infinity.
"""

import time
try:
    x = 0
    def gen_func(x):
        yield x
    while True:
        x+=1
        a = list(gen_func(x))
        print(a[0])
        time.sleep(1) 
except KeyboardInterrupt:
    print("Loop Exited")
