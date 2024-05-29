import statistics
import random

# 產生包含 20 個隨機正數的列表
#計算時 data需要更改
data = [random.randint(1, 100) for _ in range(20)]
data_sorted = sorted(data)

print("原始數據：", data_sorted)

# 計算平均值
def compute_average(data):
    return sum(data) / len(data)

average = compute_average(data)
print("平均值為：", average)

# 計算變異數
def compute_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / len(data)

variance = compute_variance(data, average)
print("變異數為：", variance)

# 計算標準差
standard_deviation = variance ** 0.5
print("標準差為：", standard_deviation)

# 計算中位數
def compute_median(data_sorted):
    n = len(data_sorted)
    if n % 2 == 0:
        return (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2
    else:
        return data_sorted[n // 2]

median = compute_median(data_sorted)
print("中位數為：", median)
