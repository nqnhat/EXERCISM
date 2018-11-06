class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.BST = TreeNode(tree_data[0])
        for i, data in enumerate(tree_data):
            if i == 0:
                continue
            self.insert_node(data, self.BST)

    def data(self):
        return self.BST

    def sorted_data(self):
        result = []
        self.get_lowest_value(self.BST, result)
        return result

    def insert_node(self,data, node):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            elif node.left is not None:
                self.insert_node(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            elif node.right is not None:
                self.insert_node(data, node.right)
                


    def get_lowest_value(self,node, result):
        if node is None:
            return
        else:
            self.get_lowest_value(node.left,result)
            result.append(node.data)
            self.get_lowest_value(node.right,result)
