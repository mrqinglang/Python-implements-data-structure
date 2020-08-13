# --*-- coding: utf-8 --*--
# @Time     : 2020/8/9 9:25
# @Author   : mrqinglang
# @software : PyCharm
import random

def binary_search_1(list ,item):
    '''递归实现二分查找'''
    n = len(list)
    mid = n//2
    if n > 0:
        if list[mid] == item:
            return True
        elif item < list[mid]:
            return binary_search_1(list[:mid], item)
        else:
            return binary_search_1(list[mid+1:], item)
    return False

def binary_search_2(list ,item):
    '''非递归实现二分查找'''
    n = len(list)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if list[mid] == item:
            return True
        elif item < list[mid]:
            last = mid-1
        else:
            first = mid+1
    return False



def main():
    num = [15, 16, 21, 36, 40, 43, 49, 67, 76, 95]
    print('排顺前:' + str(num))
    print(binary_search_1(num, 40))
    print(binary_search_2(num, 40))
    print('排序后:' + str(num))

    
if __name__ == '__main__':
    main()
