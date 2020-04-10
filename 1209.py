import sys

with open('input1209.txt','r') as fp : 
    for test_case in range(10):
        now = int(fp.readline().strip('\n'))
        #lines=[[ 0 for col in range(100)] for row in range(100)]
        lines = [0 for idx in range(100)]
        sumlist = [[],[ 0 for i in range(100)], 0, 0]
        for row in range(100):
            lines[row] = list(map(int, fp.readline().split()))
            sumlist[0].append(sum(lines[row]))
            for idx in range(100):
                sumlist[1][idx] += lines[row][idx]
        n=0
        while(n<100) :
            sumlist[2] += lines[n][n]
            sumlist[3] += lines[n][100-1-n]
            n+=1
        maxrow= max(sumlist[0])
        maxcol= max(sumlist[1])
        maxsum = max(maxrow, maxcol, sumlist[2],sumlist[3])
        print("#{} {}".format(test_case+1, maxsum))
        