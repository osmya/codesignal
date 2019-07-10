def removeKFromList(s, k):
    return [i for i in s if i != k]
    

seq = [1, 2, 3, 3 ,3 ,4, 4, 5, [5, 6]]

ans = removeKFromList(seq, 3)



# using the linked list definition in the exercise...

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def removeKFromList(s, k):
    c = s
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return s.next if s and s.value == k else s

# not sure what count does in this solution
def removeKFromList(s, k):
    t = []
    count = 0
    while s:
        if k != s.value:
            t.append(s.value)
            s = s.next
    return t
