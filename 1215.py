import sys

with open('input1215.txt','r') as fp :
    for test_case in range(1,11):
        found = int(fp.readline().strip('\n'))
        mid = int(found/2)
        cnt = 0
        lines = [[] for i in range(8)]
        for i in range(8) :
            lines[i] = fp.readline().strip('\n')
            index =0
            while index + found -1 < 8:
                start =0; end = found-1; condition = 0
                while start < mid :
                    if lines[i][index+start] == lines[i][index+end] :
                        #print(i, "      ",lines[i][index+start], lines[i][index+start+1])
                        #print(index+start, "   ", index+end)
                        start +=1
                        end -=1
                        condition+= 1
                    else :
                        break
                if condition == mid :
                    cnt +=1
                index += 1
            
        for i in range(8):
            index =0
            while index + found -1 < 8:
                start =0; end = found-1; condition = 0
                while start < mid :
                    if lines[index+start][i] == lines[index+end][i] :
                        start +=1
                        end -=1
                        condition+= 1
                    else :
                        break
                if condition == mid :
                    cnt +=1
                index += 1
    
        print("#{} {}".format(test_case, cnt))
