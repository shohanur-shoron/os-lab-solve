process = int(input("Enter Number of process: "))

process_list = []
chart = "0"
wating = 0
wating_time = 0
max_time = 5

for i in range(process):
    time = int(input(f"Enter burst time for P{i+1}: "))
    temp = [f'P{i+1}', time, time]
    process_list.append(temp)    
    
def total(time_list):
    return sum([temp[1] for temp in time_list])

copy_list = process_list.copy()

while total(process_list) != 0:
    for i, temp in enumerate(process_list):
        if temp[1] > max_time:
            wating += max_time
            chart = chart + f" {temp[0]} " + str(wating)
            process_list[i][1] -= max_time
        else:
            if temp[1] != 0:
                wating += temp[1]
                chart = chart + f" {temp[0]} " + str(wating)
                process_list[i][1] = 0
                process_list[i].append(wating)
            
for temp in process_list:
    wating_time += abs(temp[2] - temp[3])

print(f'Avg watting time = {wating_time/process}ms')
print(chart)