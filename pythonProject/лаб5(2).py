LIST_NUMS = [1, 12, 34, 56, 12, 12]
def is_retry(list_nums: list):
    for i, num in enumerate(list_nums):
        if list_nums[i+1:].count(num) > 0:
            return num


retry_num = is_retry(LIST_NUMS)
if retry_num is not None:
    print(retry_num)