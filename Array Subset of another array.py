def isSubset( a1, a2, n, m):
    for i in a2:
        if i not in a1:
            return "No"
    return "Yes"
