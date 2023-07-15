from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.horizontal_distance = 0

def print_bottom_view(root):
    if root is None:
        return

    queue = deque()
    node_dict = {}

    queue.append(root)

    while queue:
        node = queue.popleft()

        # Update the horizontal distance of the child nodes
        if node.left:
            node.left.horizontal_distance = node.horizontal_distance - 1
            queue.append(node.left)
        if node.right:
            node.right.horizontal_distance = node.horizontal_distance + 1
            queue.append(node.right)

        # Update the node in the dictionary
        node_dict[node.horizontal_distance] = node.data

    # Print the nodes from the dictionary in ascending order of their horizontal distance
    for key in sorted(node_dict.keys()):
        print(node_dict[key], end=" ")

# Example usage
# Create the binary tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# Print the bottom view of the binary tree
print_bottom_view(root)
