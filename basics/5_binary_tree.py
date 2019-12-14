import random


class BinaryTreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left, self.right = None, None

    def print(self, end='\n'):
        print(self.key, end=end)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key: int):
        node = BinaryTreeNode(key)

        if self.root is None:
            self.root = node
            return

        ptr, ptr_parent = self.__locate(key)

        if key < ptr_parent.key:
            ptr_parent.left = node
        else:
            ptr_parent.right = node

    def remove(self, key: int):
        pass

    def traverse_preorder(self):
        self.__preorder(self.root)
        print('')

    def traverse_inorder(self):
        self.__inorder(self.root)
        print('')

    def traverse_postorder(self):
        self.__postorder(self.root)
        print('')

    def traverse_levelorder(self):
        pass

    def __preorder(self, node: BinaryTreeNode):
        if node is None:
            return

        node.print(end=' ')

        self.__preorder(node.left)
        self.__preorder(node.right)

    def __inorder(self, node: BinaryTreeNode):
        if node is None:
            return

        self.__inorder(node.left)

        node.print(end=' ')

        self.__inorder(node.right)

    def __postorder(self, node: BinaryTreeNode):
        if node is None:
            return

        self.__postorder(node.left)
        self.__postorder(node.right)

        node.print(end=' ')

    def __locate(self, key: int):
        ptr, ptr_parent = self.root, None

        while ptr is not None:
            ptr_parent = ptr

            if key < ptr.key:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return ptr, ptr_parent


if __name__ == "__main__":
    bst = BinarySearchTree()

    for _ in range(20):
        bst.add(random.randint(0, 100))

    bst.traverse_preorder()
    bst.traverse_inorder()
    bst.traverse_postorder()
