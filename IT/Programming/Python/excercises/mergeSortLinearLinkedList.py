class Node:

    def __init__(self, data=None, next_node=None):
        """ data     : de gegevens die je wil opslaan in deze `Node`.
            next_node: de volgende `Node` in de lineair gelinkte lijst.
        """
        self.data = data
        self.next = next_node


def print_list(head):
    items = []

    ### BEGIN JOUW CODE
    currentNode = head

    while currentNode is not None:
        items.append(currentNode.data)
        currentNode = currentNode.next

    ### EINDE JOUW CODE

    print("[" + ",".join(str(_) for _ in items) + "]")


def merge(head_1, head_2):
    if head_1 is None: return head_2
    if head_2 is None: return head_1

    anchor = Node()
    if head_1.data < head_2.data:
        anchor.data = head_1.data
        head_1 = head_1.next
    else:
        anchor.data = head_2.data
        head_2 = head_2.next

    currentNode = anchor

    while not (head_1 is None and head_2 is None):

        # if one of em is None
        if head_1 is None:
            currentNode.next = head_2
            break
        elif head_2 is None:
            currentNode.next = head_1
            break
        if head_1.data < head_2.data:
            currentNode.next = head_1
            head_1 = head_1.next
        else:
            currentNode.next = head_2
            head_2 = head_2.next

        currentNode = currentNode.next
        currentNode.next = None

    return anchor


def split(head):        # REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return head, slow.next


def merge_sort(head):
    first, second = split(head)

    return