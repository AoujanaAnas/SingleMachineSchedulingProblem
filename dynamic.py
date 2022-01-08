import itertools
from operator import itemgetter
import time

# ******************************************************************************************************
# Read data from file
filename = "./P1_n10.txt"
p = []
with open(filename) as f:
    for line in f:
        p.append([int(n) for n in line.strip().split('\t')])
# End Reading data from file
nb0 = int(p[0][0])
data = []
for i in range(0, 10):
    data.append([i + 1, int(p[1][i]), int(p[2][i])])

data = sorted(data, key=itemgetter(2))

combData = []
D = {}
for i in range(1, len(data) + 1, 1):
    combData += list(itertools.combinations(data, i))
#******************************************************************************************************

def U(elm, currentTime):
    if currentTime + elm[1] < elm[2]:
        return 0
    else:
        return 1


def f(lst, Seq):
    v_min = 1637494949
    R = []
    if len(lst) != 0:
        for elm in range(0, len(lst)):
            Slist = []
            currTime = 0
            Rlist = list(lst)
            Rlist.pop(elm)
            Slist = list(Rlist)
            Slist.append(lst[elm])
            for x in range(0, len(Rlist)):
                currTime += Rlist[x][1]
                # get key to ensure if the result already exist in dict
            identifier = ",".join("'%s'" % a[0] for a in Rlist)
            # get key to ensure if the result already exist in dict
            if identifier in D.keys():
                res = U(lst[elm], currTime) + D[identifier]
            else:
                res = f(Rlist, Seq) + U(lst[elm], currTime)
            if v_min > res:
                v_min = res
                Seq = list(Slist)
        R = [[v_min], Seq ]
        return R
    else:
        return 0

def main_function():
    start_time = time.time()

    for DATA in combData:
        identifier = ",".join("'%s'" % a[0] for a in DATA)
        R = f(list(DATA), [])
        D[identifier] = R[0][0]
    time_execution = (time.time() - start_time)
    dynamic_result = [R[0], [x[0] for x in R[1]], time_execution]
    return dynamic_result


ff = main_function()
print(ff[0])
print(ff[1])
print(ff[2])