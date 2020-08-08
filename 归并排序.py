# --*-- coding: utf-8 --*--
# @Time     : 2020/8/8 8:49
# @Author   : mrqinglang
# @software : PyCharm
import random

def merge_sort(list):
    n = len(list)
    # 分到只剩一个的时候
    if n <= 1:
        return list
    mid = n // 2
    # left 采用归并排序后形成的有序新的列表
    left_li = merge_sort(list[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(list[mid:])
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result

def main():
    num = random.sample(range(100), 10)
    print('排顺前:' + str(num))
    a = merge_sort(num)
    print('排序后:' + str(a))

if __name__ == '__main__':
    main()
