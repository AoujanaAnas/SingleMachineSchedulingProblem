
import copy
import random
from operator import itemgetter
import time


def swap(lst):
    indice1 = 0
    indice2 = 0
    while indice1 == indice2:
        indice1 = random.randint(0, len(lst) - 1)
        indice2 = random.randint(0, len(lst) - 1)
    lst[indice1], lst[indice2] = lst[indice2], lst[indice1]
    return lst


def twoOpt(lst):
    indice1 = random.randint(0, int(len(lst) / 2))
    indice2 = random.randint(int(len(lst) / 2), len(lst))
    s = lst[0:indice1 + 1]
    ss = lst[indice2:len(lst)]
    q = [x for x in lst if x not in s]
    q = [x for x in q if x not in ss]
    q.reverse()
    # print(s)
    # print(ss)
    # print(q)
    return s + q + ss


def insertion(lst):
    indice1, indice2 = 0, 0
    while indice1 == indice2:
        indice1 = random.randint(0, len(lst) - 1)
        indice2 = random.randint(0, len(lst) - 1)
    elm = lst[indice1]
    lst.pop(indice1)
    lst.insert(indice2, elm)
    return lst


def calcSequence(lst):
  calc = 0
  res = 0
  for i in range(0,len(lst)):
    calc += lst[i][1]
    if lst[i][2] - calc >= 0:
        res += (lst[i][2] - calc)*lst[i][3]
    else:
        res += (calc - lst[i][2])*lst[i][4]
  return res


def searchUsingTwoOpt(d, resF, resI):
    c1 = 0
    while (c1 < 50 and resF <= resI):
        d = twoOpt(d)
        resF = calcSequence(d)
        if resF < resI:
            resI = resF
            c1 = 0
            backup = list(d)
        elif resF == resI:
            c1 += 1
            backup = list(d)
        else:
            d = list(backup)
    return [resI, d]


def searchUsingSwap(d, resF, resI):
    c1 = 0
    while (c1 < 50 and resF <= resI):
        d = swap(d)
        resF = calcSequence(d)
        if resF < resI:
            resI = resF
            c1 = 0
            backup = list(d)
        elif resF == resI:
            c1 += 1
            backup = list(d)
        else:
            d = list(backup)
    return [resI, d]


def searchUsingInsertion(d, resF, resI):
    c1 = 0
    while (c1 < 50 and resF <= resI):
        d = insertion(d)
        resF = calcSequence(d)
        if resF < resI:
            resI = resF
            c1 = 0
            backup = list(d)
        elif resF == resI:
            c1 += 1
            backup = list(d)
        else:
            d = list(backup)
    return [resI, d]


struct_vois = [twoOpt, swap, insertion]
struct_vois2 = [searchUsingTwoOpt, searchUsingSwap, searchUsingInsertion]


def VND(DATA):
    d = list(DATA)
    lateJobs = calcSequence(d)
    l = 0
    x = [lateJobs, d]
    while l < 3:
        xPrime = struct_vois[l](x[1])
        if calcSequence(xPrime) < calcSequence(x[1]):
            l = 0
            x[0] = calcSequence(xPrime)
            x[1] = list(xPrime)
        else:
            l += 1
    return [x[0], x[1]]


def VNS(var):
    start_time = time.time()
    # Read data from file
    filename = "./"+var
    p = []
    with open(filename) as f:
        for line in f:
            p.append([int(n) for n in line.strip().split('\t')])
        # End Reading data from file
    nb0 = 99999999999
    data = []
    for i in range(0, (int(p[0][0]))):
        data.append([i + 1, int(p[1][i]), int(p[2][i]), int(p[3][i]), int(p[4][i])])

    data = sorted(data, key=itemgetter(2))
    lateJobs1 = nb0
    seqSolution1 = []
    initial = struct_vois2[0](data, 0, 99999999)
    lateJobs = initial[0]
    seqSolution = initial[1]
    t_end = time.time() + len(data) * 0.2
    while time.time() < t_end:
        k = 0
        x = list(data)
        while k < 3:
          shak = struct_vois2[k](x, 0, 99999999)
          b = VND(shak[1])
          if b[0] < shak[0]:
              lateJobs1 = b[0]
              seqSolution1 = list(b[1])
              x = list(b[1])
              k = 0
          else:
              k += 1
          if lateJobs > lateJobs1:
              seqSolution = seqSolution1
              lateJobs = lateJobs1

    return [lateJobs, seqSolution,(time.time() - start_time)]

