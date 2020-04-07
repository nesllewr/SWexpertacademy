#달팽이 숫자

T = int(input())
for test_case in range(1, 1+T):
    n = int(input())
    mat = [[0 for col in range(n)] for row in range(n)]
    num = 1
    i = 0
    j = 0
    k = 0
    while( k < (n/2) ) : 
        #print(i, j, num)
        if j < n - k -1 and i == k: 
            mat[i][j] = num
            j+=1
            num+=1
            #print("{} {} n과 k {} {} {}".format(j,num, n, k, n-k))
            continue
        #print("두번째 if 전 {} {} {}".format(i, j, k))
        if j == n- 1- k and i < n -1 -k :
            #print("22222")
            #print("{} {}".format(i,j))
            mat[i][j] = num
            i +=1
            num +=1
            continue
        if i == n - 1 -k  and j >  k: 
            #print("here is threee333333")
            mat[i][j] = num
            j -=1
            num+=1
            continue
        if j == k and i > k :
            mat[i][j] = num
            i-=1
            num+=1
            if j ==k and i ==k:
                k+=1
                i+=1
                num-=1
                if num+1 == n *n:
                    mat[i][j+1]=n*n
                    break
            continue
        
    print("#{}".format(test_case))
    for row in range(n):
        for col in range(n):
            print(mat[row][col],end=" ")
        print()