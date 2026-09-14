def uniq(strings : list[str]) -> list[str]:
    """Возращает список уникальных строк"""
    strings = set(strings)
    strings = sorted(strings)
    return strings


print(uniq(['apple', 'banana', 'orange', 'apple']))

































# from typing import List
#
#
# def get_new_average(numbers : list[int]) -> list[int]:
#     """Возращает список элементов меньше среднего значения"""
#     if not numbers:
#         return []
#     total = sum(numbers)
#     length= len(numbers)
#     avg = total / length
#     ans = []
#
#     for num in numbers:
#         if num < avg:
#             ans.append(num)
#         else:
#             break
#     return ans
#
#
# print(get_new_average([1, 2, 3, 4, 5]))
# print(get_new_average([]))
#
