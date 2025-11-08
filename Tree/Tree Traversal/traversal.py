"""
Tree Traversal
Breadth  First Search --> traversal rowwise top to bottom from left to right.
                      -->Level by level (explores all neighbors before going deeper)
                      --> datastructure used Queue(FIFO)
                      --> traversal type horizontal
                      --> when to use When you need the shortest path in an unweighted graph
                      --> Time complexity O(V+E)
                      --> Space complexity O(V) due to queue
                      -->completeness Will find a solution if exist
                      -->optimaility Optimal for unweighted graphs
                      -->applications Shortest path, level order traversal, finding connected components

Depth First search -->Depth first (explores as far as possible along one branch)
                    --> datastructure used Stack(LIFO)
                    --> traversal type vertical.
                    --> when to use When you need to explore all possible paths or check for cycles
                    --> Time complexity O(V+E)
                    --> Space complexity O(V) due to stack recursion
                    --> completeness May get stuck in infinite depth (unless depth-limited)
                    -->optimaility Not optimal (may not find shortest path)
                    -->applications Topological sorting, detecting cycles, solving mazes, backtracking problems

BFS: Good for finding shortest distance between two nodes in a maze.

DFS: Good for exploring all possible paths (like solving Sudoku or recursion-based problems).



"""                 


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right 

    def bfs(self):
        """
        method for tree traversal breadth first search
        """
        current_node = self.root
        queue = []   #using list for simplisity but for time complexity use real queue
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result 
    


    def dfs_preorder(self):
        """
        tree traversal depth first search preorder
        """
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

    def dfs_postorder(self):
        """
        tree traversal depth first search postorder
        """
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)


    def dfs_inorder(self):
        """
        tree traversal depth first search inorder
        """
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results



