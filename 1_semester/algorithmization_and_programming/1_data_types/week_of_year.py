import sys

def weekend(firstday,nowday):
    n = nowday-firstday
    counter = 0
    if(n < 0): return -1
    while n >= 0:
        n -= 7
        counter += 1
    return counter
 
print(weekend(int(sys.argv[1]),int(sys.argv[2])))