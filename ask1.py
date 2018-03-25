#!/usr/bin/python

import sys
import time

incount = 0
bicount = 0
def sorted(llist,rlist) :
    slist = []
    j = i = 0
    if len(llist) == 0 :
        return rlist
    if len(rlist) == 0 :
        return llist
    while len(slist) < len(llist) + len(rlist) :
        if len(llist) > i and len(rlist) > j :
            if llist[i] > rlist[j] :
                slist.append(rlist[j])
                j += 1
            else :
                slist.append(llist[i])
                i += 1
        elif len(llist) > i :
            slist.append(llist[i])
            i += 1
        elif len(rlist) > j :
            slist.append(rlist[j])
            j += 1
    return slist

def merge(llist,rlist) :
    s1 = []
    s2 = []
    f1 = 0
    f2 = 0
    if len(llist) > 1 :
        s1 = merge(llist[:len(llist)/2],llist[len(llist)/2:])
    else :
        s1 = llist
    if len(rlist) > 1 :
        s2 = merge(rlist[:len(rlist)/2],rlist[len(rlist)/2:])
    else :
        s2 = rlist
    return sorted(s1,s2)

def quick(ilist) :
    llist = []
    rlist = []
    cur = ilist[len(ilist)-1]
    del ilist[len(ilist)-1]
    for i in ilist :
        if i < cur :
            llist.append(i)
        else :
            rlist.append(i)
    if len(llist) > 1 :
        s1 = quick(llist)
    else :
        s1 = llist
    if len(rlist) > 1 :
        s2 = quick(rlist)
    else :
        s2 = rlist
    return s1 + [cur] + s2

def binary(ilist,x) :
    global bicount
    if x > ilist[len(ilist)-1] :
        print "Didnt found number %d" %x
    elif len(ilist) == 1 and ilist[0] != x :
        print "Didnt found number %d" %x
    elif x > ilist[len(ilist)/2] :
        bicount += 1
        binary(ilist[len(ilist)/2:],x)
    elif x < ilist[len(ilist)/2] :
        binary(ilist[:len(ilist)/2],x)
        bicount += 1
    else :
        print "Found number %d" %x

def interp(ilist,x) :
    global incount
    inter = ((len(ilist)-1)/(ilist[len(ilist)-1]-ilist[0])*x)-ilist[0]
    if x > ilist[len(ilist)-1] :
        print "Didnt found number %d" %x
    elif len(ilist) == 1 and ilist[0] != x :
        print "Didnt found number %d" %x
    elif x > ilist[inter] :
        incount += 1
        interp(ilist[inter:],x)
    elif x < ilist[inter] :
        incount += 1
        interp(ilist[:inter],x)
    else :
        print "Found number %d" %x

ilist = []
if (len(sys.argv) > 1) :
    #kwdikas gia arxeio
    try :
        infl = open(sys.argv[1],"r")
    except IOError :
        print "Unable to open the file %s" %(sys.argv[1])
        sys.exit(0)
    while True :
        try :
            inp = infl.readline()
            if (inp == '' or inp == '\n') :
                break
            try:
                tolist = int(inp[:len(inp)-1])
                ilist.append(tolist)
            except ValueError :
                print "Input must be Integers"
                sys.exit(0)
        except EOFError :
            break
else :
    print "No input file"
    print "Usage: ./ask1.py file_name"
    sys.exit(0)

print "Input list:"
print ilist

while True :
    print "1: Sort with merge sort"
    print "2: Sort with quick sort"
    print "Choise: "
    try :
        method = int(input())
        if method > 2 or method < 1 :
            print "Wrong choise"
        else :
            break
    except NameError ,SyntaxError:
        print "Input must be Integer"
if method == 1 :
    print "Executing merge sort"
    llen = len(ilist)/2
    t = time.time()
    sorlist = merge(ilist[:llen],ilist[llen:])
    print "Sorted in %fsec" %(time.time() - t)
    print sorlist
else :
    print "Executing quick sort"
    t = time.time()
    sorlist = quick(ilist)
    print "Sorted in %fsec" %(time.time() - t)
    print sorlist
while True :
    print "1: Binary Search"
    print "2: Interpolation Search"
    print "Choise: "
    try :
        method = int(input())
        if method > 2 or method < 1 :
            print "Wrong choise"
        else :
            break
    except NameError ,SyntaxError :
        print "Input must be Integer"
if method == 1 :
    while True :
        try :
            print "Give int for search"
            ts = int(input())
            break
        except NameError ,SyntaxError :
            print "Input must be Integer"
    print "Executing binary search"
    t = time.time()
    binary(sorlist,ts)
    print "Completed in %fsec" %(time.time() - t)
    print "With %d cmps" %bicount
else :
    while True :
        try :
            print "Give int for search"
            ts = int(input())
            break
        except NameError ,SyntaxError :
            print "Input must be Integer"
    print "Executing interpolation search"
    t = time.time()
    interp(sorlist,ts)
    print "Completed in %fsec" %(time.time() - t)
    print "With %d cmps" %incount
