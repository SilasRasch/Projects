import os
import time
import secrets
import string

class MyRNG:
    def __init__(self, a=48271*secrets.randbelow(10), c=secrets.randbelow(11), m=2**31-secrets.randbelow(6), seed=None):
        self.a = a
        self.c = c
        self.m = m
        
        if seed is None:
            self.x0 = int(os.getpid() + time.time() % 69 / 7 * secrets.randbelow(100))
        else:
            self.x0 = seed
    
        self.x_prev = (self.a * self.x0 + self.c) % self.m
    
    def gen_int(self, max=None):
        if max is None:
            range = None
        else:
            range = [0, max]

        self.x_prev = (self.a * self.x_prev + self.c) % self.m

        if range is None:
            return self.x_prev
        else:
            return int((self.x_prev / (self.m - 1)) * (range[1] - range[0]) + range[0])
    
    def gen_index(self, array):
        index = self.gen_int(array.__len__())
        return array[index]