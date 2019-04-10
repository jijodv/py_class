#!/usr/bin/env python

list1 = [10, 30, [454, 32], 24, 676, 77]

def func1(pos1):
    for it in list1:
        print it
        print (type(it))
        if 'int' not in str(type(it)):
            func1
        else:
            print (it)
func1(list1)
