import sys

with open("input1284.txt",'r') as fp:
    T = int(fp.readline().strip('/n'))
    for test_case in range(1, 1+int(T)):
        prices = list(map(int,(fp.readline().split())))
        #print(prices)
        a_fee = prices[4] * prices[0]
        if prices[2] > prices[4]:
            b_fee = prices[1]
            #print(b_fee)
        else :
            b_fee = prices[1] + (prices[4]-prices[2]) * prices[3]
        total = min(a_fee, b_fee)
        #print (a_fee,' ' ,b_fee)
        print("#{} {}".format(test_case, total))

         