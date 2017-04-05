#use list comprehension to get a list containing only max and min no
def find_max_min(A):
    B=[i for i in A ]
    minB=min(B)
    maxB=max(B)
    if maxB==minB:
        return [len(B)]
    else:
        return([minB, maxB])
