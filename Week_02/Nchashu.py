'''
 N叉树的层序遍历
'''

def levelOrder(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        child = []
        node = []
        for item in queue:
            child.append(item.val)
            if item.children: node += item.children
        result.append(child)
        queue = node
    return result