#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:54:29 2022

@author: Pablo Martínez
"""

from time import sleep 
from random import random
from multiprocessing import Process

def f ():
    for i in range(5):
        print ("hola",i)
        sleep (random())
        
if __name__ == "__main__":
    p = Process(target=f)
    q = Process(target=f)
    p.start()
    q.start()
    print ("fin")
