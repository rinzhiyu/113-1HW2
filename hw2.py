def number(nums):
    n = len(nums)
    sum1 = n * (n + 1) // 2  # 完整範圍的總和
    sum2 = sum(nums)  # 數組中已有數字的總和
    return sum1 - sum2

#輸入數組
nums = list(map(int, input("請輸入數組，以逗號分隔: ").split(',')))

# 計算缺失的數字
missing = number(nums)

#列印結果
print(f"nums = {nums}")
print(f"{missing}")
print(f"數組中包含了範圍 [0, {len(nums)}] 內的數字，其中缺少了 {missing}。")
