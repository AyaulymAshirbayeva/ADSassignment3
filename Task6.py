def maxdep(root):
    if not root:
        return 0
    left=maxdep(root.left)
    right=maxdep(root.right)
    if left>right:
        return left+1
    else:
        return right+1
