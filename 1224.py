
def check_priority(operator, stack, postfix):
    if stack[-1] == "(" :
        stack.append(operator)
        return
    elif operator == "*":
        if stack[-1] =="*":
            postfix.append(stack[-1])
            stack.pop()
            stack.append(operator)
        else :
            stack.append(operator)
    else :
        postfix.append(stack[-1])
        stack.pop()
        stack.append(operator)
    
def calculate(postfix):
    stack = []
    for idx in postfix:
        if idx.isdigit() == True:
            stack.append(int(idx))
        else :
            second = int(stack.pop())
            first = int(stack.pop())
            if idx == "*" :
                now = (first * second)
            elif idx=="+" :
                now = (first + second)
            stack.append(now)
    return stack[0]

with open('input1224.txt','r') as fp :
    for test_case in range(1,11) :
        length = int(fp.readline())
        line = list(fp.readline().strip("\n"))
        stack = list()
        postfix = list()
        mode = 0 ; num =0
        for idx in line :
            length = len(stack)
            if idx.isdigit()==True:
                postfix.append(idx)
            else :
                if not stack:
                    stack.append(idx)
                else :
                    if idx == "(":
                        stack.append(idx)
                    elif idx == ")":
                        i = length
                        while stack[i-1] != "(":
                            postfix.append(stack[i-1])
                            i-=1
                        del stack[i-1:length]
                    else :
                        check_priority(idx, stack, postfix)
        result = calculate(postfix)
        print("#{} {}".format(test_case, result))
