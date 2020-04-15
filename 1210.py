import sys

with open('input1210.txt','r') as fp :
    for test_case in range(1,11):
        num = int(fp.readline().strip('\n'))
        lines = ['' for i in range(100)]
        for i in range(100):
            lines[i] = list(map(int,fp.readline().split()))
        where = lines[99].index(2)
        index = 100
        while index > 0 :
            index -=1
            if where < 99 and where >0 :
                if lines[index-1][where-1] == 1 :
                    while where > 0 and lines[index-1][where-1] == 1:
                        where = where -1
                    continue
                elif lines[index-1][where+1] == 1 :
                    while where < 99 and lines[index-1][where+1] ==1:
                        where = where+1
                        continue
            elif where == 0 :
                if lines[index-1][where+1]==1:
                    while where < 99 and lines[index-1][where+1] ==1:
                        where = where +1
                    continue
            elif where == 99:
                if lines[index-1][where-1]==1:
                    while where > 0 and lines[index-1][where-1] ==1:
                        where = where -1
                    continue
            
        print("#{} {}".format(test_case, where))

                