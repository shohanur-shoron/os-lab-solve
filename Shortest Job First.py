process = int(input("Enter Number of process: "))

process_list = []
chart = "0"
wating = 0
wating_time = []
wating_time.append(wating)

for i in range(process):
    time = int(input(f"Enter burst time for P{i+1}: "))
    temp = (f'P{i+1}', time)
    process_list.append(temp)

process_list.sort(key=lambda x: x[1])

for temp in process_list:
    index = 1
    wating += temp[1]
    wating_time.append(wating)
    chart = chart + f' {temp[0]} ' + str(wating)
    
print(chart)
print(f'Avg watting time = {sum(wating_time[:-1])/ process}ms')