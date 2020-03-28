import sys

fp = open('input1204.txt','r')
T = int(fp.readline())
for test_case in range(1, 1 + T):
    score = [ 0 for i in range(101)]
    num = fp.readline().strip('\n')
    #print("{} num {} ".format(test_case, num))
    now = list(map(int,fp.readline().split()))
    for j in range(1000):
        score[now[j]] += 1
    res_list = [i for i, value in enumerate(score) if value == max(score)]
    print("#{} {}".format(test_case,max(res_list)))
#    print(score.index(max(score)))