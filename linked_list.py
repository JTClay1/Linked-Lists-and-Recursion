# linked_list.py

class Node:
    def __init__(self, data, next=None):
        # Node is just a little container:
        # it holds a value + a pointer to the next node
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # Start with an empty list
        self.head = None

    def insert_at_front(self, data):
        """
        O(1) insert at the front.
        This is the clean "linked list flex" move:
        new node points to the current head, then becomes the head.
        """
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        """
        Insert at the end.
        This is O(n) because we have to walk to the tail.
        The tests call this, so it HAS to exist.
        """
        new_node = Node(data)

        # If the list is empty, this is easy:
        # the new node becomes the head.
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, walk until we find the last node (tail)
        current = self.head
        while current.next is not None:
            current = current.next

        # Now current is the tail, so link it to the new node
        current.next = new_node

    def recursive_sum(self):
        """
        Public wrapper so tests can just call recursive_sum()
        and we start recursion at the head.
        """
        return self._recursive_sum(self.head)

    def _recursive_sum(self, node):
        """
        Base case: if node is None, we've hit the end -> sum is 0.
        Recursive case: node.data + sum of the rest.
        """
        if node is None:
            return 0
        return node.data + self._recursive_sum(node.next)

    def recursive_search(self, target):
        """
        Public wrapper for recursive search.
        Same idea: start at head and recurse forward.
        """
        return self._recursive_search(self.head, target)

    def _recursive_search(self, node, target):
        """
        Base case: node is None => we ran out of list -> not found.
        Match case: node.data == target => found.
        Otherwise: keep checking the next node.
        """
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search(node.next, target)

    def recursive_reverse(self):
        """
        Reverse the list IN PLACE using recursion.
        Big thing: after reversing, we must update self.head.
        """
        self.head = self._recursive_reverse(self.head, None)

    def _recursive_reverse(self, current, prev):
        """
        The idea:
        - flip the pointer of current to point backwards (to prev)
        - then move forward using saved next_node
        - when current becomes None, prev is the new head

        current: node we're currently processing
        prev:    node that should come after current once reversed
        """
        # Base case: if current is None, we went past the end.
        # prev is now the new head of the reversed list.
        if current is None:
            return prev

        # Save next before we mess with pointers
        next_node = current.next

        # Flip the pointer (this is the actual "reverse" step)
        current.next = prev

        # Recurse forward: next becomes current, current becomes prev
        return self._recursive_reverse(next_node, current)

    def __str__(self):
        """
        Not required for tests, but super useful for quick debugging/printing.
        """
        vals = []
        current = self.head
        while current is not None:
            vals.append(str(current.data))
            current = current.next
        return " -> ".join(vals) if vals else "(empty)"
