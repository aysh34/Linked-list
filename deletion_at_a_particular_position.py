class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# creating linked list
node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head
print("Before deletion")
while current is not None:
    print(current.data, "->", end=" ")
    current = current.next
print("None")

# delete 3rd node
current = head
while current.next is not None and current.data != 20:
    current = current.next

current.next = current.next.next # current points to node2

current = head
print("After deletion")
while current is not None:
    print(current.data, "->", end=" ")
    current = current.next
print("None")
