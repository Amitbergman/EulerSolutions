def print_fibo(how_much_to_print):
    count = 3
    cur = 1
    next_num = 1
    to_print = 0
    print("hi")
    while (len(str(to_print)) < how_much_to_print):
        to_print = cur + next_num
        cur = next_num
        next_num = to_print
        count= count+1
        print(len(str(to_print)))
    print(to_print,count-1)
print_fibo(1000)