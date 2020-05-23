def convert(numbers):
    line = list()
    for i , v in enumerate(numbers):
        line.append(int("".join(v),16))
    return line

with open("sample_input5658.txt","r") as fp:
    num_test = int(fp.readline())
    for test_case in range( 1, num_test + 1) :
        num, k_th = list(map(int,fp.readline().split()))
        rotate = int(num / 4)
        lines = list(fp.readline().strip("\n"))
        hexa = list()
        for ro in range(rotate) :
            for idx in range(0, num, rotate):
                hexa.append(lines[idx:idx+rotate])
            finds = convert(hexa)
            last = lines.pop()
            lines.insert(0,last)
        finds = list(set(finds)) 
        finds.sort(reverse=True)
        # print(finds)
        print("#{} {}".format( test_case, finds[k_th-1]))