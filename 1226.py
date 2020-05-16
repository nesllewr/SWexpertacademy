import sys

with open('input1226.txt','r') as fp:
    for test_case in range(1,2):
        fp.readline()
        lines = [[] for i in range(16)]
        #print(lines)
        for idx in range(16):
            lines[idx]= list(map(int,fp.readline().strip()))
            if 2 in lines[idx]:
                start = lines[idx].index(2)
            if 3 in lines[idx] :
                end = lines[idx].index(3)
        print(lines)    
        possible = 0
        #print("#{} {} {} {}".format(test_case, possible, start, end))
        # print(lines[start])