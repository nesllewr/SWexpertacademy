import sys

with open('input1244.txt', 'r') as fp :
    T = int(fp.readline().strip('\n'))
    for test_case in range(1, 1+T):
        lines = list(map(int,(fp.readline().split())))
        #numbers = [int(i) for i in str(lines[0])] 
        origin = list(map(int,str(lines[0])))
        num = origin
        cur = 0 
        while cur != lines[1] : 
            
                
            cur+=1
        print("#{} {}".format(test_case, lines))