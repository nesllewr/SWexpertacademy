
with open("input1219.txt","r") as fp:
    for test_case in range(1,11):
        length = fp.readline().split()
        length = int(length[1])
        lines = list(map(int, fp.readline().split()))
        first = lines[:length]; second = lines[length:]
        checked =[]
        node = [first[0],second[0]]
        possible = 0
        n =0
        while node:
            now = node.pop()
            if now in checked:
                continue
            else :
                # print(now)
                if first[now] != 0:
                    # print("first: ", first[now])
                    node.append(first[now])
                if second[now] != 0:
                    # print("second ", second[now])
                    node.append(second[now])
                if first[now] ==0 and second[now]==0:
                    checked.append(now)
                if 99 in node:
                    print("HERE")
                    possible =1
                    break
      
        print("#{} {}".format(test_case, possible))

