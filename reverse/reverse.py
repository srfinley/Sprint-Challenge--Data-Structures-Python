class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

    def __str__(self):
        return f'Node = {self.value}. next is {self.next_node}'


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        if self.head == None:
            return
        next = node.next_node
        node.next_node = prev
        if next == None:
            self.head = node
            return
        self.reverse_list(next, node)

l = LinkedList()
l.add_to_head(1)
l.add_to_head(2)
l.add_to_head(3)
l.add_to_head(4)
l.add_to_head(5)
l.reverse_list(l.head, None)
current = l.head
while current is not None:
    print(current.value)
    current = current.next_node