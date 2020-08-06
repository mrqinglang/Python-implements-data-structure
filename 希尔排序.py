# --*-- coding: utf-8 --*--
# @Time     : 2020/8/6 7:54
# @Author   : mrqinglang
# @software : PyCharm
import random

def shell_sort(list):
    n = len(list)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -1):
                if list[j] < list[j - gap]:
                    list[j], list[j - gap] = list[j - gap], list[j]
                else:
                    break
        gap //= 2


def main():
    num = random.sample(range(100), 10)
    print('排顺前:' + str(num))
    shell_sort(num)
    print('排序后:' + str(num))
if __name__ == '__main__':
    main()
