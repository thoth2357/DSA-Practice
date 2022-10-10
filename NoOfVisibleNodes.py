"""
There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.
Signature
int visibleNodes(Node root) {
Input
The root node of a tree, where the number of nodes is between 1 and 1000, and the value of each node is between 0 and 1,000,000,000
Output
An int representing the number of visible nodes.

Example
8 <------ root
/
3 10
/ \
1 6 14
/ \ /
4 7 13
output = 4
"""


def max_depth_level(root,level):
    return 1 + max(max_depth_level(root.left,level+1),max_depth_level(root.right,level+1)) if root else 0

def visible_nodes(root):
    return max_depth_level(root,0)
