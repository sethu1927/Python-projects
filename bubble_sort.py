A = [-5,-19,0,23,4,4,-8]


def bubble_sort(arr):

    n = len(arr)
    flag = True

    while flag : 
        flag = False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = True



    return arr
print(bubble_sort(A))       