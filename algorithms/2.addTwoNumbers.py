#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from helper import ListNode


def addTwoNumbers(l1, l2):
    """
    You are given two linked lists representing two non-negative numbers.
    The digits are stored in reverse order and each of their nodes contain a
    single digit. Add the two numbers and return it as a linked list.
    @l1, listNode
    @l2, listNode
    rtype: listNode
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    else:
        ret = ListNode(0)
        cur = ret       # python class like pointer
        carry = 0       # deal with sum more than 10
        while l1 or l2:
            sum2 = 0
            if l1:
                sum2 += l1.val
                l1 = l1.next
            if l2:
                sum2 += l2.val
                l2 = l2.next
            sum2 += carry
            cur.next = ListNode(sum2 % 10)
            cur = cur.next
            carry = 1 if sum2 >= 10 else 0

        if carry:
            cur.next = ListNode(1)
        ret = ret.next   # pop the first node that not use
        return ret
