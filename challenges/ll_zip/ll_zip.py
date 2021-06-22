def merge_lists(ll_1, ll_2):
    ll_1_current = ll_1.head
    ll_2_current = ll_2.head

    temp_1 = ll_1_current.next
    temp_2 = ll_2_current.next

    while ll_1_current is not None and ll_2_current is not None:
        if temp_1 is None and temp_2 is not None:
            ll_1_current.next = ll_2_current
            ll_2_current.next = temp_2
        else:
            ll_1_current.next = ll_2_current
            ll_2_current.next = temp_1

        ll_1_current = temp_1
        ll_2_current = temp_2

        if temp_1 is not None and temp_2 is not None:
            temp_1 = temp_1.next
            temp_2 = temp_2.next
    return ll_1
