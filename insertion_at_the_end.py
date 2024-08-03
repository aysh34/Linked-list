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
# insertion at the end
new_node = Node(5)
current = head
while current.next is not None:
    current = current.next

current.next = new_node
current = head  # reset the current to head
while current:  # while current is not none
    print(current.data, "->", end=" ")
    current = current.next
print("None")
