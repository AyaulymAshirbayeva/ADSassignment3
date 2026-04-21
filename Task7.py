class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def issym(root):
    if not root:
        return True
    
    def ismirror(t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        
        return ismirror(t1.left, t2.right) and ismirror(t1.right, t2.left)
    return ismirror(root.left, root.right)

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20, TreeNode(15), TreeNode(7))
print(issym(root))