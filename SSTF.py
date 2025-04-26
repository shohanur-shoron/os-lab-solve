head = int(input("Head: "))
print("Enter path: ", end=" ")
path_list = [int(i) for i in input().split(' ')]
total = 0


def closest_number(target, numbers):
    differences = [abs(num - target) for num in numbers]
    min_difference = min(differences)

    closest_index = differences.index(min_difference)
    closest_value = numbers[closest_index]

    return closest_value, closest_index


while(len(path_list) != 0):
    print(head, end=" ")
    val, index = closest_number(head, path_list)

    total += abs(head - val)
    head = val

    del path_list[index]


print(head)
print("total: ", total)