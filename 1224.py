
def check_priority(operator, stack,length,postfix):
    if operator == "*":
        if stack[length-1] =="*":
            postfix.append(stack[length-1])
            del stack[length-1]
            stack.append(operator)
        else :
            stack.append(operator)
    else :
        if stack[length-1] != "*":
            postfix.append(stack[length-1])
            del stack[length-1]
            stack.append(operator)
        else :
            stack.append(operator)


with open('input1224.txt','r') as fp :
    for test_case in range(1,11) :
        length = int(fp.readline())
        line = list(fp.readline())
        stack = list()
        postfix = list()
        mode = 0
        for idx in range(length) :
            length = len(stack)
            print(line[idx], end="  ")
            if line[idx].isdigit()==True:
                postfix.append(line[idx])
            else :
                if length == 0:
                    stack.append(line[idx])
                    continue                  
                elif line[idx] == "(":
                    stack.append(line[idx])
                    continue
                elif line[idx] ==")":
                    i = length
                    print(i, stack)
                    while stack[i-1] != "(":
                        postfix.append(stack[i-1])
                        i-=1
                    del stack[i-1:length]
                    continue
                else :
                    check_priority(line[idx],stack, length,postfix)
        

        #print(length, postfix)
#        print("#{} {}".format(test_case, result))

