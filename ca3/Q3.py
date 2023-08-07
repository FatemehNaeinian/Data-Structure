n = int(input())
mex = 0
num = [0]*(n+1)
for i in range(n):
    new_num = input()
    # print(new_num)
    # print(new_num[0])
    # print(new_num[2])
    if new_num[0] == '+':
        if int(new_num[2:]) < n:
            num[int(new_num[2:])] += 1
            if(int(new_num[2:]) == mex):
                for j in range(n):
                    if num[j]==0:
                        mex = j
                        break
            
    if new_num[0] == '-':
        if int(new_num[2:]) < n:
            if num[int(new_num[2:])] > 0:
                num[int(new_num[2:])] -= 1
                if num[int(new_num[2:])] == 0:
                    if int(new_num[2:]) < mex:
                        mex = int(new_num[2:])
    print(mex)
    # print(num)
    