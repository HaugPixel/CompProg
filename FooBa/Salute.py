def solution(s):
    salutees = 0
    salutations = 0
    for x in s:
        if x == ">":
            salutees += 1
        elif x == "<":
            salutations += salutees * 2
    return salutations

print(solution("<--->---<--<>"))