with open("input2805.txt","r") as fp:
    test = int(fp.readline())
    for test_case in range(test):
        Nsize = int(fp.readline())
        middle = Nsize//2
        results = list()
        for idx in range(Nsize):
            lines = list(fp.readline().strip("\n"))
            for j in range(Nsize):
                if abs(idx- middle) + abs(j-middle) <= middle:
                    results.append(int(lines[j]))


        print("#{} {}".format(test_case+1, sum(results)))
