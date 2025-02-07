#!/usr/bin/env python3


def join_sets(s1, s2):
    # join_sets will return a set that contains every value from both s1 and s2
    join = s1.union(s2)
    return join

def match_sets(s1, s2):
    # match_sets will return a set that contains all values found in both s1 and s2
    match = s1.intersection(s2)
    return match

def diff_sets(s1, s2):
    # diff_sets will return a set that contains all different values which are not shared between the sets
    diff = s1.symmetric_difference(s2)
    return diff

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))


