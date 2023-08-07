line = input()
stack = []
max_len = 0
curr_len = 0

for i in range(len(line)):
    # print(stack)
    # print(curr_len)
    # print(max_len)
    if line[i] in ['(', '{', '[']:
        stack += [line[i]]
        curr_len += 1
    else:
        if [stack[-1] , line[i]] in [['(',')'],['{','}'],['[',']']]:
            stack.pop()
            curr_len += 1
            if len(stack) == 0:
                if max_len < curr_len:
                    max_len = curr_len
        else:
            stack.append(line[i])
            curr_len = 0

print(max_len)