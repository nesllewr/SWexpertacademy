import sys

fp = open("input1206.txt", "r")
for test_case in range(1, 12) :
    T = int(fp.readline().strip('/n'))
    height_of_buildings = map(int, fp.readline().split())
    height = list(height_of_buildings)
    maxheight = max(height)
    cnt = 0 
    '''
    cur = '0010000000111000111111111001001100'
    b = cur.find('001')
    if b != -1 :
        while(cur[b+1:].find('001') != -1):
            print("b위치 : {}".format(b))
            if b< T-3 and cur[b+3]=='0' and cur[b+4]=='0' :
                cnt +=1
                print("cnt 더한 b위치: {}".format(b))
            b = cur[b+1:].find('001') + b + 1
    print("# {}".format(cnt))
    '''
    for i in range(1, maxheight+1) :
        cur = ''
        for col in range(T):
            if height[col] >= i : 
                cur += '1'
            else: 
                cur += '0' 
        #print("# {} {} ".format(i, cur))
                    
        b = cur.find('001')
        while(cur[b+1:].find('001') != -1):
            #print("b위치 : {}".format(b))
            if cur[b+3]=='0' and cur[b+4]=='0' :
                cnt +=1
            #    print("cnt 더한 b위치: {}".format(b))
            b = cur[b+1:].find('001') + b + 1
            #print("b 조정 후 위치 : {}".format(b))
            #print(cur[b+1:].find('001'))
        if cur[b+3]=='0' and cur[b+4]=='0' :
            cnt +=1
            #print("cnt 더한 b위치: {}".format(b))
            
           
    print("{} {} {}".format(test_case,T,cnt))
