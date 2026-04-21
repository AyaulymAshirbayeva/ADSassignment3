class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longest(root):
    def dfs(node, parent, current):
        if not node: 
            return current
        
        if parent and node.val==parent.val+1:
            length+=1
        else:
            length=1
        left=dfs(node.left, node, current)
        right=dfs(node.right, node, current)
        return max(current, left, right)
    if not root:
        return 0
    return dfs(root, None, 0)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(longest(root))   