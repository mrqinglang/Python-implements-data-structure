# --*-- coding: utf-8 --*--
# @Time     : 2020/8/1 21:10
# @Author   : mrqinglang
# @software : PyCharm
import random
def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[min_index], list[i] = list[i], list[min_index]
    return list

def main():
    num = random.sample(range(100), 10)
    print('排顺前:' + str(num))
    print('排序后:' + str(selection_sort(num)))
if __name__ == '__main__':
    main()

