# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x, left = None, right = None):
         self.val = x
         self.left = left;
         self.right = right;

class Stack:
    m_stack = [];
    def __init__(self):
        self.m_stack = [];
        self.m_top = 0;

    def push(self, node, childvisitStatus):
        self.m_stack.append((node,childvisitStatus));
        self.m_top = self.m_top + 1;

    def pop(self):
        if (self.m_top == 0):
            return None;
        nodeTuple = self.m_stack[self.m_top-1];
        self.m_top = self.m_top - 1;
        self.m_stack.remove(nodeTuple);
        return nodeTuple;

    def isEmpty(self):
        return (self.m_top == 0);

class Solution:
    postOrderTraversal = [];
    def postorderTraversalInternal(self, root):
        if (root == None):
            return;
        stack = Stack();
        stack.push(root, 0);
        while (stack.isEmpty() == False):
            nodeTuple = stack.pop();
            node = nodeTuple[0];
            visitStatus = nodeTuple[1];
            if (node == None):
                continue;
            if (visitStatus == 0):
                stack.push(node, 1);
                stack.push(node.left, 0);
            if (visitStatus == 1):
                stack.push(node, 2);
                stack.push(node.right, 0);
            if (visitStatus == 2):
                self.postOrderTraversal.append(node.val);

    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        self.postOrderTraversal = [];
        self.postorderTraversalInternal(root);
        return self.postOrderTraversal;
sol = Solution();
print(sol.postorderTraversal(TreeNode(3, TreeNode(2, TreeNode(7), TreeNode(8)), TreeNode(1))));