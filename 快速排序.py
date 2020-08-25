# --*-- coding: utf-8 --*--
# @Time     : 2020/8/6 7:54
# @Author   : mrqinglang
# @software : PyCharm
import random

def quick_sort(list, start, end):
    if start < end:
        low, high = start, end
        base = list[low]
        while low < high:
            # 如果low与high没有相遇那么high的游标左移
            while (low < high) and (list[high] >= base):
                high -= 1
            list[low] = list[high]
            while (low < high) and (list[low] <= base):
                low += 1
            list[high] = list[low]
        list[low] = base
        print('-------------')
        print(base, list)
        # 递归
        quick_sort(list, start, low - 1)
        quick_sort(list, low+1, end)


def main():
    num = random.sample(range(100), 10)
    print('排顺前:' + str(num))
    quick_sort(num, 0, len(num)-1)
    print('排序后:' + str(num))

if __name__ == '__main__':
    main()
