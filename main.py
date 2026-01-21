# main.py
from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)  # List should be: 20 -> 10 -> 5

    # 3) Display the list to verify insertion
    print("List:", ll)

    # 4) Call recursive_sum and print the result
    print("Sum:", ll.recursive_sum())

    # 5) Call recursive_search with a target and print result
    target = 10
    print(f"Search {target}:", ll.recursive_search(target))
    print("Search 999:", ll.recursive_search(999))

    # 6) Call recursive_reverse, then display the reversed list
    ll.recursive_reverse()
    print("Reversed:", ll)
