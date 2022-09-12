#  Write a program to perform bubble sort on a given set of elements.
print('Dona T John')
print('21/MCA/018')

def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


# Driver code to test above
arr = []
Num = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Num + 1):
    val = int(input("Enter the Value of %d Element : " % i))
    arr.append(val)

print("UnSorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

bubbleSort(arr)

print("\nSorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")