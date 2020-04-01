import sys

fp = open("input2071.txt","r")
T = int(fp.readline())
for test_case in range(1, 1+T):
    arr = list(map(int, fp.readline().split()))
    average = sum(arr)/len(arr)
    print("#{} {}".format(test_case,round(average)))