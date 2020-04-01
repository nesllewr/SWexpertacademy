import sys

T = int(input())
out = []
for i in range(1, 1+T):
    cur = str(i)
    cnt = 0
    if cur.count('3') > 0 or cur.count('6') > 0 or cur.count('9') > 0 : 
        cnt = cur.count('3') +cur.count('6')+cur.count('9')
    if cnt > 0 :
        cur = '-' * cnt
    print(cur,end = " ")
