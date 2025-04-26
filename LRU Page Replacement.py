def find_replacement(windows, past_pages):
    distance = []
    past_pages.reverse()

    for window in windows:
        i = 0
        for page in past_pages:
            if window == page:
                distance.append(i)
                break
            else: i += 1

    if len(distance) == 0:
        return 0

    max_value = max(distance)
    max_index = distance.index(max_value)
    return max_index


def page_faults(pages, capacity):
    window = []
    hit = 0
    faults = 0

    for i, page in enumerate(pages):
        if page in window:
            hit += 1
            print('Hit \t Queue: ', window)
        else:
            faults += 1
            if len(window) < capacity:
                window.append(page)
                print('Fault \t Queue: ', window)
            else:
                past_page = pages[:i]
                replace_index = find_replacement(window, past_page)
                window[replace_index] = page
                print('Fault \t Queue: ', window, ' -- replace_index: ', replace_index)

    return faults


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
faults = page_faults(pages, capacity)
print('Page fault: ', faults)