# import itertools
#
# def queens ():
#     for p in itertools.permutations (range (8) ):
#         yield [x for x in enumerate (p) ]
#
# board_list = []
# count = 4
# while count:
#     for q in queens ():
#         err = False
#         for a, b in ( (a, b) for a in q for b in q if a [0] < b [0] ):
#             if abs (a [0] - b [0] ) == abs (a [1] - b [1] ):
#                 err = True
#                 break
#         if not err:
#             count -= 1
#             board_list.append(q)
#
# print(board_list)


import itertools


def queens():
    for p in itertools.permutations(range(8)):
        yield [x for x in enumerate(p)]

def board() -> list[list[tuple()]]:
    board_list = []
    count = 4

    for q in queens():
        err = False
        for a, b in ((a, b) for a in q for b in q if a[0] < b[0]):
            if abs(a[0] - b[0]) == abs(a[1] - b[1]):
                err = True
                break
        if not err:
            count -= 1
            board_list.append(q)
            if count == 0:
                return board_list

print(board())
