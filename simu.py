import random
import sys

args = sys.argv

# 建造回数
n_try = int(args[1])

# 目的キャラの排出率の内訳
pool = [int(i) for i in args[2:]]

def win_build(num):
    l = 0
    label = 1
    result = 0
    for i in pool:
        if num > l and num <= l + i:
            result = label
        label += 1
        l += i
    return result

l_build = []
for i in range(n_try):
    # 建造結果の内部表現: 1~1000の整数
    num = (random.randrange(1000)) + 1
    l_build.append(num)

if len(set([win_build(i) for i in l_build])) == (len(pool) + 1):
    is_win = True
else:
    is_win = False

print(is_win)
