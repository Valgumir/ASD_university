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

    if head is not None:
        items.append(head.data)
        while head.next is not None:
            head = head.next
            items.append(head.data)

    ### EINDE JOUW CODE

    print("[" + ",".join(str(_) for _ in items) + "]")


def merge(head_1, head_2):
    head = Node()
    anker = head

    # Blijf in de lus tot dat de einden van beide gelinkte lijsten bereikt zijn.
    while head_1 is not None or head_2 is not None:
        # Als de eerste lijst leeg is, voeg het volgende element van lijst 2 toe aan de gesorteerde lijst.
        if head_1 is None:
            next = head_2
            head_2 = head_2.next

        # Als de eerste lijst leeg is, voeg het volgende element van lijst 2 toe aan de gesorteerde lijst.
        elif head_2 is None:
            next = head_1
            head_1 = head_1.next

        # else: er zitten nog elementen in beide lijsten
        else:
            # Haal de data van het eerste element uit beide gelinkte lijsten
            data1 = head_1.data
            data2 = head_2.data

            # Vergelijk de twee elementen met elkaar.
            # Voeg de kleinste toe aan de gesorteerde array, en verwijder het uit de originele gelinkte lijst
            if data1 < data2:
                next = head_1
                head_1 = head_1.next
            else:
                next = head_2
                head_2 = head_2.next

        anker.next = next
        anker = next

    return head.next


def split(head):
    if head.next is None:
        return [head, None]

    # Hier hebben we een fast, slow en even variable.
    # slow: the first half of the list
    # fast: the whole list

    slow = head
    fast = head
    even = False
    while head is not None:
        even = not even
        if even:
            slow = slow.next
        head = head.next

    # Hier gaan we door de gehele lijst tot dat we het eerste element van de slow lijst tegenkomen.
    # Als dit gebeurd zetten we het 'next' attribuut naar None zodat de gelinkte lijst hier stopt.
    fastcopy = fast
    while fastcopy.next.data is not slow.data:
        fastcopy = fastcopy.next
    fastcopy.next = None
    return [fast, slow]


# Algmeen merge sorting algoritme
def merge_sort(head):
    if head is None or head.next is None:
        return head

    left, right = split(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
