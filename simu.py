import random
import sys

args = sys.argv

# 建造回数
n_try = int(args[1])

# 目的キャラの排出率の内訳
pool = [int(i) for i in args[2:]]
win_total = sum(pool)

def win_build(num):
    if num > win_total:
        return 0
    else:
        l = 0
        label = 1
        for i in pool:
            if num > l and num <= l + i:
                return label
            label += 1
            l += i
        return 0

# 建造結果の内部表現: 1~1000の整数
l_build = [(random.randrange(1000)) + 1 for i in range(n_try)]

if len(set([win_build(i) for i in l_build])) == (len(pool) + 1):
    is_win = True
else:
    is_win = False

print(is_win)
