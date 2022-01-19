def EvaluateExpression(s):
    s=s.split()
    n=len(s)
    stack =[]
    for i in range(n):
        if s[i].isdigit():
            stack.append(int(s[i]))
        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)+int(b))
        elif s[i]=="*":
            if i!=n-1:
                if s[i+1] == '*':
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a)**int(b))
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)*int(b))
        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)/int(a))
        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)-int(a))            
    return stack.pop()
print(EvaluateExpression('3 7 + 12 2 - *'))