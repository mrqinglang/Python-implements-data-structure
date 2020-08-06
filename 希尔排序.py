# --*-- coding: utf-8 --*--
# @Time     : 2020/8/1 21:10
# @Author   : mrqinglang
# @software : PyCharm
import random

def shell_sort(list):
    n = len(list)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if list[i] < list[i-gap]:
                    list[i], list[i-gap] = list[i-gap], list[i]
                    i -= gap
                else:
                    break
                print(list)
        print('--------')
        gap //= 2


def main():
    num = random.sample(range(100), 10)
    print('排顺前:' + str(num))
    shell_sort(num)
    print('排序后:' + str(num))
if __name__ == '__main__':
    main()
