def add_no(*args):
    total = 0
    for i in args:
        total += i
    print("Total:", total)


add_no()
add_no(1)
add_no(1, 2)
add_no(1, 2, 3)
add_no(1, 2, 3, 4)
