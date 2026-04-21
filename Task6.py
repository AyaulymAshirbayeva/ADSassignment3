class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxdep(root):
    if not root:
        return 0
    left=maxdep(root.left)
    right=maxdep(root.right)
    if left>right:
        return left+1
    else:
        return right+1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(maxdep(root)) 