class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.dfs(root)
        return(self.arr[k-1])

    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)   
        self.dfs(root.right)