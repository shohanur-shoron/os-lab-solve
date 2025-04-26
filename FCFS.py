head = int(input("Head: "))
print("Enter path: ", end=" ")
path_list = [int(i) for i in input().split(' ')]
total = 0


for num in path_list:
    total += abs(head-num)
    head = num


print(total)