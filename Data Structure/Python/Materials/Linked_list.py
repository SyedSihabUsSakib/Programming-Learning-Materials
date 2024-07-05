import numpy as np

class Node:
    def __init__(self,elem,next=None):
        self.elem,self.next = elem,next

def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1,len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head

def printLinkedList(head):
    temp = head
    while temp != None:
        if temp.next != None:
            print(temp.elem, end = '-->')
        else:
            print(temp.elem)
        temp = temp.next
    print()


# Counting number of element in the list
def count(head):
    count = 0
    temp = head
    while temp != None:
        count += 1
        temp = temp.next
    return count


# Getting node of an specific index
def nodeAt(head, idx):
    count = 0
    temp = head
    obj = None
    while temp != None:
        if count == idx:
            obj = temp
            break
        temp = temp.next
        count += 1
    if obj == None:
        print("Invalid index")
    return obj



def insert(head, elem, idx):
    total_nodes = count(head)
    if idx == 0: # Inserting at the beginning
        n = Node(elem,head)
        head = n
    elif idx >= 1 and idx < total_nodes: # Inserting at the middle
        n = Node(elem, head)
        n1 = nodeAt(head, idx - 1)
        n2 = nodeAt (head, idx)
        n.next = n2
        n1.next = n
    elif idx == total_nodes: # Inserting at the end
        n = Node(elem, None)
        n1 = nodeAt(head, total_nodes - 1)
        n1.next = n
    else:
        print("Invalid Index")
    return head


def remove(head, idx):
    if idx == 0: # Removing first element
        head = head.next
    elif idx >= 1 and idx < count(head): # Removing middle element
        n1 = nodeAt(head, idx - 1)
        removed_node = n1. next
        n1. next = removed_node.next
    else:
        print("Invalid Index")
    return head


def rotate_left(head):
    new_head = head.next
    temp = new_head
    while temp.next != None:
        temp = temp.next
    temp.next = head
    head.next = None
    head = new_head
    return head


def rotate_right(head):
    last_node = head.next
    second_last_node = head
    while last_node.next != None:
        last_node = last_node.next
        second_last_node = second_last_node.next
    last_node.next = head
    second_last_node.next = None
    head = last_node
    return head


def reverse_out_of_place(head) :
    new_head = Node(head.elem, None)
    temp = head.next
    while temp != None:
        n = Node (temp.elem, new_head)
        new_head = n
        temp = temp.next
    return new_head



def reverse_in_place(head):
    new_head = None
    temp = head
    while temp != None:
        n = temp.next
        temp.next = new_head
        new_head = temp
        temp = n
    return new_head




def partial_reverse(head, start_idx, stop_idx):
    if start_idx > 0:
        st = start_idx
        node_bfr_start = nodeAt(head, start_idx-1)
        p = node_bfr_start.next
    # handle negative start index
    else:
        st = 0
        node_bfr_start = head
        p = head
    
    node_aftr_stop = nodeAt(head, stop_idx)

    rh = node_aftr_stop
    while st < stop_idx:
        # print(p.elem)
        t = p.next
        p.next = rh
        rh = p
        p = t 
        st += 1

    if start_idx > 0:
        node_bfr_start.next = rh
    else:
        head = rh

    return head

head = createList(np.array([10,15,34,41,56,72,78,91]))
printLinkedList(head)
# print(nodeAt(head, 4).elem)
head = partial_reverse(head, 2, 7)
printLinkedList(head)
head = partial_reverse(head, 2, 7)
printLinkedList(head)
head = partial_reverse(head, -2, 7)
printLinkedList(head)
head = partial_reverse(head, -2, 7)
printLinkedList(head)