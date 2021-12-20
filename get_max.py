import numpy as np


def get_max(rep):
    w, n = 500-10, 11*rep

    name = ['开心果', '葡萄干', '菜籽油', '茉莉花茶', '红枣', '旺旺大礼包', '腰果', '猪肉脯', '核桃', '枸杞', '每日坚果'] * rep
    weight = [28, 17, 65, 36, 37, 30, 14, 12, 12, 45, 34] * rep
    value = [28, 17, 65, 36, 37, 30, 14, 12, 12, 45, 34] * rep

    p = [[0 for j in range(w + 1)] for i in range(n)]
    rec = [[0 for j in range(w + 1)] for i in range(n)]
    for j in range(w + 1):
        if weight[0] <= j:
            p[0][j] = value[0]
            rec[0][j] = 1
    for i in range(1, n):
        for j in range(w + 1):
            if weight[i] <= j and value[i] + p[i-1][j-weight[i]] > p[i-1][j]:
                p[i][j] = value[i] + p[i-1][j-weight[i]]
                rec[i][j] = 1
            else:
                p[i][j] = p[i-1][j]
    print(p[n-1][w])
    print("choose item ", end="")
    tmp = w
    s_list = []
    for i in range(n-1, -1, -1):
        if rec[i][tmp] == 1:
            print(i, name[i], end=" ")
            s_list.append(name[i])
            tmp -= weight[i]

    print(" ")
    print(sorted(s_list))
    print('=================')


if __name__ == '__main__':
    for i in range(1,6):
        get_max(i)
