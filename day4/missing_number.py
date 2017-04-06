'''You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77'''

def find_missing(A , B):
    add_A=sum(A)
    add_B=sum(B)

    if add_A==add_B:
        return 0
    if add_A > add_B:
        return add_A-add_B
    else:
        return add_B-add_A
    pass
print(find_missing([2,3],[2]))
