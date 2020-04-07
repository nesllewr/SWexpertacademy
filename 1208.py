import sys

with open('input1208.txt','r') as fp :
    for test_case in range(10):
        dump_num = int(fp.readline().strip('\n'))
        blocks  = list(map(int,(fp.readline().split())))
        n = 0
        while( n < dump_num+1) :
            highest = max(blocks)
            high_index = blocks.index(highest)
            lowest = min(blocks)
            low_index = blocks.index(lowest)
            diff = highest - lowest
            if diff == 0 :
                break
            else :
                blocks[high_index] -= 1
                blocks[low_index] +=1
                n +=1
        
        print("#{} {}".format(test_case, diff))
