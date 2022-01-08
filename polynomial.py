from flask import Flask, json, jsonify, render_template,url_for
import copy
from operator import itemgetter
import time

#function of poly algo
def removeMax(lst):
    max = 0
    index = 0
    for i in range(0, len(lst)):
        if lst[i][1] > max:
            max = lst[i][1]
            index = i
    res = lst[index]
    del lst[index]
    return res
"""
Plynomial algorithm for 10 tasks 
"""
def polyFor(var):
    start_time = time.time()
    # Read data from file
    filename = "./"+var
    p = []
    with open(filename) as f:
        for line in f:
            p.append([int(n) for n in line.strip().split('\t')])
    # End Reading data from file
    nb0 = int(p[0][0])
    data = []
    # make data in format [[a,b,c] , [a,b,c], ......] with a = task number, b = process time, c = due date
    for i in range(0, nb0):
        data.append([i + 1, int(p[1][i]), int(p[2][i])])
    # End of making data in format [[a,b,c] , [a,b,c], ......] with a = task number, b = process time, c = due date
    data = sorted(data, key=itemgetter(2))   #Sort data acording to due date
    sol = []   # Solution list
    rem = []   # List of removed element
    sum_ = 0   # Current time at the begining = 0
    for x in range(0, len(data)):
        sum_ += data[x][1]
        sol.append(data[x])
        if sum_ > data[x][2]:  # test if current time grater than due date
            elm = removeMax(sol)
            rem.append(elm)
            sum_ -= elm[1]
    #print(sol + rem)
    #print(len(rem))

    return [len(rem) ,[x[0] for x in (sol + rem)] , (time.time() - start_time)]

