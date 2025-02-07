#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    tempset = set(l1).union(set(l2))
    newlist = list(tempset)
    return newlist

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    tempset = set(l1).intersection(set(l2))
    newlist = list(tempset)
    return newlist

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    tempset = set(l1) ^ set(l2)
    newlist = list(tempset)
    return newlist

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
