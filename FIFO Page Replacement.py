def page_faults(pages, capacity):
    old_frame_index = 0
    window = []
    hit = 0
    faults = 0

    for page in pages:
        if page in window:
            hit += 1
            print('Hit \t Queue: ', window)
        else:
            faults += 1
            if len(window) < capacity:
                window.append(page)
                print('Fault \t Queue: ', window)
            else:
                window[old_frame_index] = page
                old_frame_index = (old_frame_index+1) % capacity
                print('Fault \t Queue: ', window, ' -- Old Frame: ', old_frame_index)

    return faults


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
faults = page_faults(pages, capacity)
print('Page fault: ', faults)