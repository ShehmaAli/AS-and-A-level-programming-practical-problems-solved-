mylist = []

topptr = -1


def push(x):
    mylist.append(x)


def pop():
    mylist.remove(mylist[topptr])


def exit():
    print(mylist)

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
        topptr += 1
    if status == "2":
        if topptr == -1:
            print("The value can not be popped as the list is empty")
        else:
            print(f"The value {mylist[topptr]} has been popped")
            pop()
            topptr -= 1
    if status == "3":
        exit()
        break

