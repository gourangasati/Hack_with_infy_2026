class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.path = float('-inf')
class Solution:
    def cal(self,root):
        self.path = float('-inf')
        self.max_path(root)
        return self.path
    def max_path(self,root):
        if not root:
            return 0 
        le = max(0, self.max_path(root.left))
        ri = max(0, self.max_path(root.right))
        self.path = max(self.path,le+ri+root.val)
        return root.val+max(le,ri)

if __name__ == "__main__":
    # Build test tree
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print("Maximum Path Sum:",
          sol.cal(root))