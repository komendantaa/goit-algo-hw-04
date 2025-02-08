import random
import timeit

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Функція для порівняння часу виконання
def compare_sorting_algorithms():
    # Генерація випадкових даних
    data_sizes = [1000, 2500, 5000, 10000, 20000]

    print("Результати порівняння:")
    print("Розмір масиву | Сортування вставками | Сортування злиттям | Timsort")
    for size in data_sizes:
        print(f"{size:13} | ", end="")
        data = [random.randint(0, 100000) for _ in range(size)]

        # Копії масивів для кожного алгоритму
        data_insertion = data[:]
        data_merge = data[:]
        data_timsort = data[:]

        # Вимірювання часу для сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(data_insertion), number=1)
        print(f"{insertion_time:20.6f} | ", end="")

        # Вимірювання часу для сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(data_merge), number=1)
        print(f"{merge_time:18.6f} |", end="")

        # Вимірювання часу для Timsort (вбудований sorted)
        timsort_time = timeit.timeit(lambda: sorted(data_timsort), number=1)
        print(f"{timsort_time:10.6f}")

if __name__ == "__main__":
    compare_sorting_algorithms()
