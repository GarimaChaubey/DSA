class Solution:
    def buildTree(self, preorder, inorder):
        # Base case: if the list is empty, there is no tree
        if not preorder or not inorder:
            return None

        # 1. The first element of preorder is ALWAYS the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. Find where this root is in the inorder list
        # This tells us how many nodes are in the left subtree
        mid = inorder.index(root_val)

        # 3. Recursively build the left and right subtrees
        # Inorder: [left side] root [right side]
        # Preorder: root [left side] [right side]
        
        # Left subtree: 
        # Preorder: skip the root, take 'mid' number of elements
        # Inorder: everything before 'mid'
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Right subtree:
        # Preorder: everything after the left side
        # Inorder: everything after the root
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
