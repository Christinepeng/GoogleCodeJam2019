n = int(input())
cnt = 1
for i in range(n):
    for i in range(2):
        string = input()
        if i == 1:
            res = []
            for s in string:
                if s == 'E':
                    res.append('S')
                elif s == 'S':
                    res.append('E')
            print('Case #{IDX}: {RES}'.format(IDX=cnt, RES=''.join(res)))
            cnt += 1
