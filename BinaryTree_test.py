class BinaryTreeList:

    def __init__(self, value = None):

        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryTreeList(val)
        else:
             if self.right:
                self.right.add(val)
             else:
                self.right = BinaryTreeList(val)

class binaryTree:

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = BinaryTreeList(value)
        else:
            self.root.add(value)

    def find(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True
            else:
                if target < node.value:
                    node = node.left

                else:
                    node = node.right
        return False
A=binaryTree()     
A.add(5)
A.add(3)
A.add(10)
A.add(51)
A.add(34)
A.add(7)
A.add(13)
print("find 51", A.find(51))
print("find 10", A.find(10))
import timeit
print("The timeit for this program is: ",timeit.timeit("binaryTree", globals=globals(), number=5))
