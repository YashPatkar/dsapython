nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for index1, row in enumerate(nums):
    for index2, col in enumerate(row):
        print(f"index1({row}), index2({col})")