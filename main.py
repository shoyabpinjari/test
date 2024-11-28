l = [10, 20, 11, 23, 11042, 423, 687, 199]
op=[]
for i in l:
    if i not in op:
        if str(i).startswith('1'):
            op.append(i)

print(op)
