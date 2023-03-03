res = []
n = int(input())
for i in range(n):
    x = input()
    if x[2] == 'f':
        res.append((False,x.strip().split(' ')[2]))
    else:
        res.append((True,))

    
def check(records):
    all_valid = True
    errs = []
    for r in records:
        if not r[0]:
            all_valid = False
            errs.append(r[1])
    if not all_valid:
        print("No")
        print(" ".join(errs))
        return False, errs
    else:
        print("Yes")
        return True, []
      
valid, errors = check(res)
