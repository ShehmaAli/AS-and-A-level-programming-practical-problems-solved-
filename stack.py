mylist = [0 for _ in range(10)]
maxsize = 10
topptr = -1


def push(x):
    global maxsize, topptr, mylist
    if topptr == maxsize-1:
        print("Overflow")
    else:
        topptr += 1
        mylist[topptr] = x


def pop():
    global topptr, mylist
    delitem = -1
    if topptr == -1:
        print("Underflow")
    else:
        delitem = mylist[topptr]
        topptr -= 1
    return delitem


while True:
    status = input("...............\n"
                   "1: push\n"
                   "2: pop\n"
                   "3: exit\n"
                   "...............\n"
                   "Enter one: ")
    if status == "1":
        push(input("Enter a value to be pushed"
                   ": "))
    if status == "2":
        print(f"This {pop()} has been popped")
        mylist[topptr + 1] = 0
    if status == "3":
        print(mylist)
        break
