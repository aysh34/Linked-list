class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# creating linked list
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

new_node = Node(500)
current = head
while current.next is not None and current.data != 2:
    current = current.next
new_node.next = current.next
current.next = new_node

current = head
while current:  # while current is not none
    print(current.data, "->", end=" ")
    current = current.next
print("None")
