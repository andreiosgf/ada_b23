# Recursive Python Program for merge sort
import random
import time

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list):
    if len(list) < 2:
        return list

    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


#seq = [12, 11, 13, 5, 6, 7]
seq = list([random.randint(-1000,1000) for x in range(0,1000000)])
print("Given array is")
print(seq);
print("\n")
print("Sorted array is")
start=time.time()
print(mergesort(seq))
end=time.time()

print(f'Sorting executed in {end-start} sec')
# Code Contributed by Mohit Gupta_OMG
