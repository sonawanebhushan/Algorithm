# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x, leftNode = None, rightNode = None):
         self.val = x;
         self.left = leftNode;
         self.right = rightNode;

class Queue:
    m_queue = None;
    def __init__(self):    
        self.m_queue = [];
        self.m_startIndex = 0;
        self.m_endIndex = 1;
    def qsize(self):
        return (self.m_endIndex - self.m_startIndex - 1);
    def put(self, val):
        self.m_queue.append(val);
        self.m_endIndex = self.m_endIndex + 1;
    def get(self):
        if(self.m_startIndex+1 > self.m_endIndex):
            return None;
        else:
            self.m_startIndex = self.m_startIndex + 1;
            return self.m_queue[self.m_startIndex-1];

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        q = Queue();
        q.put('x');
        q.put(root);
        print q.qsize();
        data = '';
        while q.qsize() > 0:
            node = q.get();
            if node == 'x':
                print "{0}]".format(data) if len(data) > 0 else '';
                q.put('x') if q.qsize() > 0 else 0;
                data =  '[';
            else:
                #print ('Node contents');
                #print (node);
                data = "{0}{1}".format(data, node.val) if data == '[' else "{0}, {1}".format(data,node.val);
                q.put(node.left) if node.left <> None else 0;
                q.put(node.right) if node.right <> None else 0;


node = TreeNode(3, TreeNode(9, None, TreeNode(4)), TreeNode(20, TreeNode(15), TreeNode(7)));
node = TreeNode(1);
solution = Solution();
solution.levelOrder(node);