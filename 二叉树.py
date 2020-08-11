# --*-- coding: utf-8 --*--
# @Time     : 2020/8/10 20:31
# @Author   : mrqinglang
# @software : PyCharm

class Node(object):
    def __init__(self, item):
        self.elem = item
        self.leftchild = None
        self.rightchild = None

class Tree(object):
    def __init__(self):
        self.root = None
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.leftchild is None:
                cur_node.leftchild = node
                return
            else:
                queue.append(cur_node.leftchild)
            if cur_node.rightchild is None:
                cur_node.rightchild = node
                return
            else:
                queue.append(cur_node.rightchild)
    def breadth_travel(self):
        '''广度优先遍历(层次遍历)'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.leftchild is not None:
                queue.append(cur_node.leftchild)
            if cur_node.rightchild is not None:
                queue.append(cur_node.rightchild)
    def preorder(self, node):
        '''深度优先遍历(先序遍历)'''
        if node is None:
            return
        print(node.elem, end=' ')
        self.preorder(node.leftchild)
        self.preorder(node.rightchild)
    def inorder(self, node):
        '''中序遍历'''
        if node is None:
            return
        self.inorder(node.leftchild)
        print(node.elem, end=' ')
        self.inorder(node.rightchild)
    def postorder(self, node):
        '''后序遍历'''
        if node is None:
            return
        self.postorder(node.leftchild)
        self.postorder(node.rightchild)
        print(node.elem, end=' ')



def main():
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)

if __name__ == '__main__':
    main()
