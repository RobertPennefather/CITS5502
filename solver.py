import sys
import math
import numpy as np

pts1 = [150.1428571, 94.85714286, 69.57142857, 35.57142857]
pts2 = [86.28571429, 54.71428571, 48.71428571, 39]
pts3 = [97.28571429, 61.42857143, 46.14285714, 43]

def updateProgress(done, total, finish = False):
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %f%%' % ('='*math.floor(50*done/total), 100*done/total))
    sys.stdout.flush()
    if finish:
        sys.stdout.write('\r%-50s\r\033[F' % (' '*200))

def calcMetric(t, a, b, c, metric):
    if metric == 1:
        return a+(b*t)+(c*t*t)
    elif metric == 2:
        return (a+(b*c*t))/((b*t)+1)
    elif metric == 3:
        return ((a-c)*math.exp(-b*t)) + c
    elif metric == 4:
        return ((a-c)*pow(t+1, -b)) + c
    else:
        print('[ERROR] Wrong metric')
        return 0

def findSOS(pts, a, b, c, metric):
    sos = 0
    for index in range(0,len(pts)):
        pt = pts[index]
        prd = calcMetric(index, a,b,c, metric)
        sos += (pt - prd)*(pt - prd)
    return sos

def findVRB(pts, MIN, MAX, INC, metric):

    vrbls = [0, 0, 0]
    sosMin = findSOS(pts, 0,0,0, metric)
    rng = np.arange(MIN, MAX+INC, INC).tolist()

    for i in rng:
        for j in rng:
            for k in rng:
                sos = findSOS(pts, i, j, k, metric)
                if sos < sosMin:
                    sosMin = sos
                    vrbls = [i,j,k]

        updateProgress(i*MAX*MAX+j*MAX+k, MAX*MAX*MAX+MAX*MAX+MAX)
    
    updateProgress(1,1, True)
    return sosMin, vrbls

print(findVRB(pts1, 0, 100, 1, 1))
print(findVRB(pts2, 0, 100, 1, 1))
print(findVRB(pts3, 0, 100, 1, 1))
print()
print(findVRB(pts1, 0, 100, 1, 2))
print(findVRB(pts2, 0, 100, 1, 2))
print(findVRB(pts3, 0, 100, 1, 2))
print()
print(findVRB(pts1, 0, 100, 1, 3))
print(findVRB(pts2, 0, 100, 1, 3))
print(findVRB(pts3, 0, 100, 1, 3))
print()
print(findVRB(pts1, 0, 100, 1, 4))
print(findVRB(pts2, 0, 100, 1, 4))
print(findVRB(pts3, 0, 100, 1, 4))
