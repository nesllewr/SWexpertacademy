

with open("sample_input4012.txt","r") as fp:

    def compare(food_set):
        value = 0
        for i in range(N//2):
            for j in range(i+1,N//2):
                value += mat[food_set[i]][food_set[j]] + mat[food_set[j]][food_set[i]]

    # def choice_dfs(N,count):
    #     return
    def dfs(idx,k):
        global result
        if idx == N // 2: 
            A = [] 
            B = [] 
            for j in range(N): 
                if visited[j]: 
                    A.append(j)
                else:
                    B.append(j)
            recipe_A = compare(A)
            recipe_B = compare(B)
            if abs(recipe_A - recipe_B) < result:
                result = abs(recipe_A - recipe_B)
            return
    
        for i in range(k,N): 
            if not visited[i]:
                visited[i] = 1
                dfs(idx+1,i+1)
                visited[i] = 0

    num_test = int(fp.readline())
    for test_case in range(num_test):        
        N = int(fp.readline())
        visited = [0 for _ in range(N)]
        mat = list()
        for i in range(N):
            synergy = list(map(int, fp.readline().split()))
            mat.append(synergy)
        dfs(0,0)
        # print(mat)    
        print("#{} {}".format(test_case,value))





