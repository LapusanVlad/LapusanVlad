import time

def bubble_sort_visualize(arr):
    n = len(arr)
    pasul = 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            print(f"Pasul {pasul}: {arr}")
            pasul += 1
            time.sleep(1.5)

    print("\nLista sortata: ", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visualize(arr)

