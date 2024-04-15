# find middle element

def find_middle(head):
    if not head:
        return None
    
    slow_pointer = head
    fast_pointer = head
    
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        
    return slow_pointer


