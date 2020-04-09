import sys

with open('input2007.txt','r') as fp:
    T = int(fp.readline().strip('\n'))
    for test_case in range(1, 1+T):
        lines = str(fp.readline().strip('\n'))
        pattern = str()
        for idx in range(len(lines)) :
            if pattern.find(lines[idx]) == -1 :
                #print("NNNNNNNNNN")
                pattern += (lines[idx])
            else :
                #print("WHERE ARE YOU ",lines[idx])
                length = len(pattern)
                i = 0
                while i + length < len(lines): 
                    #print("WHILE   ", lines[i:i+length],"        ",pattern )
                    if lines[i:i+length] == pattern :
                        i += length
                        continue
                    else : 
                        pattern += (lines[idx])
                        #print("here             ", pattern)
                        break
        print("#{} {}".format(test_case, pattern))