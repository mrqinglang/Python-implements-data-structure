# --*-- coding: utf-8 --*--
# @Time     : 2020/8/2 8:40
# @Author   : mrqinglang
# @software : PyCharm
import random
def insert_sort(list):
    n = len(list)
    for i in range(1, n):
        num = list[i]
        for j in range(i, 0, -1):
            if num < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else:
                break
        print(list)


def main():
    list = random.sample(range(100), 10)
    print(list)
    insert_sort(list)
if __name__ == '__main__':
    main()
