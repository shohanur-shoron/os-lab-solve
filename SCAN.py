head = int(input("Head: "))
print("Enter path: ", end=" ")
path_list = [int(i) for i in input().split(' ')]
total = 0

def sortPath(path, head):
    smaller = []
    larger = []

    for i in path:
        if i < head:
            smaller.append(i)
        else:
            larger.append(i)

    smaller.sort(reverse=True)
    larger.sort()

    return smaller + larger

path_list = sortPath(path_list, head)

for num in path_list:
    total += abs(head-num)
    head = num

print(total)

