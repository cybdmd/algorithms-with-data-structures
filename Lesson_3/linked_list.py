# Односвязанный список:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)
        n = self
        while n.next:
            n = n.next
        n.next = end


# Разворот списка через рекурсию:
def recursive(_curr, _pre=None):
    if not _curr:
        return _pre

    p_next = _curr.next
    _curr.next = _pre

    return recursive(p_next, _curr)


if __name__ == '__main__':

    ll = Node(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    node = ll
    print(node.data)
    while node.next:
        node = node.next
        print(node.data)

    print('Reverse:')
    linkReverse = recursive(ll)
    # linkReverse = reverse(link)
    while linkReverse:
        print(linkReverse.data)
        linkReverse =linkReverse.next