def merge_sort(unsorted, threshold, reverse):
    '''
    :param unsorted:
    :param threshold:
    :param reverse:
    :return: the list unsorted
    Use merge sort (Recursively!) to sort and return the list unsorted. merge_sort must
        be written recursively.
    When splitting lists in half, once the list reaches a size less than
        or equal to the threshold, use insertion_sort.
    Sort the list in increasing order if reverse is False, otherwise in decreasing order.
    '''
    unsorted_length = len(unsorted)
    if unsorted_length < 2:
        return unsorted
    mid = unsorted_length // 2
    if unsorted_length <= threshold:
        insertion_sort(unsorted, reverse)
    else:
        firsthalf = unsorted[0:mid]
        secondhalf = unsorted[mid:unsorted_length]
        firsthalf = merge_sort(firsthalf, threshold, reverse)
        secondhalf = merge_sort(secondhalf, threshold, reverse)
        unsorted = merge(firsthalf, secondhalf, reverse)
    return unsorted

def merge(first, second, reverse):
    '''
    :param first:
    :param second:
    :param reverse:
    :return: single,sorted list
    Given two lists, first and second, merge them into a single, sorted list and return it.
    Sort the list in increasing order if reverse is False, otherwise in decreasing order.
    '''
    S = first + second
    if reverse is False:
        i = j = 0
        while i + j < len(S):
            if j == len(second) or (i < len(first) and first[i] < second[j]):
                S[i + j] = first[i]
                i = i + 1
            else:
                S[i + j] = second[j]
                j = j + 1
    else:
        i = j = 0
        while i + j < len(S):
            if i == len(first) or (j < len(second) and first[i] < second[j]):
                S[i + j] = second[j]
                j = j + 1
            else:
                S[i + j] = first[i]
                i = i + 1
    return S


def insertion_sort(unsorted, reverse):
    '''
    :param unsorted:
    :param reverse:
    :return: thr list unsorted
    Use Insertion Sort to sort and return the list unsorted
    Sort the list in increasing order if reverse is False, otherwise in decreasing order.
    '''
    if reverse is False:
        unsorted_length = len(unsorted)
        for i in range(1, unsorted_length):
            j = i
            while (j > 0) and (unsorted[j] < unsorted[j - 1]):
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                j -= 1
    else:
        unsorted_length = len(unsorted)
        for i in range(1, unsorted_length):
            j = i
            while (j > 0) and (unsorted[j] > unsorted[j-1]):
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                j -= 1
    return unsorted
