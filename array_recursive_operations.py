arr = [2, 4, 6]


# 6 + sum (2, 4)
# 4 + sum (2)
# 2 + 0

# divide and conquer
def sum_recursive(array):
    if not array:
        return 0
    return array[0] + sum_recursive(array[1:])


def count_recursive(array):
    if not array:
        return 0
    return 1 + count_recursive(array[1:])


if __name__ == '__main__':
    print(sum_recursive(arr))
    print(count_recursive(arr))
