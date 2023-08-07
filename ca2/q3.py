x, p, q = input().split()
x = int(x) # money
p = int(p) # price
q = int(q) # count

abnabat = []

abnabat.append(x // p)
rem = 0

while (abnabat[-1] )>0:
    abnabat.append((abnabat[-1] + rem)//q)
    rem = (abnabat[-2] + rem) % q
    # print(rem)

print(sum(abnabat))