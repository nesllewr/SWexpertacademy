
def choice_dfs(N,count):


with open("sample_input4012.txt","r") as fp:
    num_test = int(fp.readline())
    for test_case in range(num_test):        
        N = int(fp.readline())
        mat = list()
        for i in range(N):
            synergy = list(map(int, fp.readline().split()))
            mat.append(synergy)
        
        print(mat)    
        # print("#{} {}".format(test_case,value))





