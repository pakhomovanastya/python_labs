def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError('список пуст')
    else:
        return min(nums), max(nums)

print(min_max(nums=[3, -1, 5, 5, 0]))
# print(min_max(nums=[]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

print(unique_sorted(nums=[3, 1, 2, 1, 3]))


def flatten(mat: list[list | tuple]) -> list:
    a = []
    for row in mat:
        if isinstance(row, list) or isinstance(row, tuple):
            a.extend(row)
        else:
            raise TypeError('строка не строка строк матрицы')
    return a

print(flatten(mat=[[1, 2], [3, 4]]))


