class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Example usage:
# Constructing a sample BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

print("Minimum value in the BST:", find_min(root))  # Output: 3
print("Maximum value in the BST:", find_max(root))  # Output: 18
