def swapkthnode(head,num,k):
    if n<k:
        return head
    if (2*k-1)==n:
        return head
    a=head
    a_pr = Node(None)
    for i in range(k-1):
        a_pr=a
        a=a.next
    b=head
    b_pr = Node(None)
    for i in range(n-k):
        b_pr=b
        b=b.next
    if a_pr is not None:
        a_pr.next = b
    if b_pr is not None:
        b_pr.next = a
    temp = a.next
    a.next = b.next
    b.next = temp
    if k == 1:
        head = b
    if k == n:
        head = a
    return head
