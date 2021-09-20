# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_s =  ""
        l2_s = ""
        sum_list=[]
        while l1:
            l1_s += str(l1.val)
            l1 = l1.next
        while l2:
            l2_s+= str(l2.val)
            l2 = l2.next
        l1_st = "".join(l1_s)
        l2_st = "".join(l2_s)
        sum_st=int(l1_st)+int(l2_st)  
        sum_list=ListNode(0)
        while sum_st%10 <10:
            sum_list.val= sum_st%10
            sum_list.next = sum_st/10
            sum_st = sum_st/10
        return sum_list
        
