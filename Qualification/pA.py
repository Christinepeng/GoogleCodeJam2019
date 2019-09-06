T = int(input())

cnt = 1
for i in range(T):
    num_str = input()

    res_A = []
    res_B = []
    for c in num_str:
        if c == '4':
            res_A.append('3')
            res_B.append('1')
        else:
            res_A.append(c)
            res_B.append('0')
    str_A = ''.join(res_A)
    str_B = ''.join(res_B).lstrip('0')
    print('Case #{IDX}: {A} {B}'.format(IDX=cnt, A=str_A, B=str_B))
    cnt += 1
