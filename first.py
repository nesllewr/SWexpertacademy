import sys

list_file =  open('input.txt', 'r').read().split('\n')
#sys.stdout = open('output.txt','w')
numline = int(list_file[0])

for i in range(numline):
    numset = list_file[i+1].split(" ")
    intset = list(map(int, numset))
    sum = 0
    for j in range(10) :
        if intset[j] %2 !=0 :
            sum += intset[j]
   # print(sum)
    print("#"+str(i+1)+" "+str(sum))