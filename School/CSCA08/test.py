def f(L: list[int]) -> None:
    new_lst = []
    for item in L:
        new_lst.append(2 * item)
        L = new_lst
L = [1, 2, 3, 4]
f(L)
print(L)