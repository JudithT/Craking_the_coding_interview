from LinkedLists import LinkedLists

def remove_middle_node(node):
    node.value = node.value.next
    node.next = node.next.next 

    