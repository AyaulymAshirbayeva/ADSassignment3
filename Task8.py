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
        