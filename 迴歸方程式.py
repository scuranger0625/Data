import numpy as np
from scipy import stats

# 提示用戶輸入 X 和 Y 的資料
X_str = input("請輸入 X 的資料（以空格分隔）：")
Y_str = input("請輸入 Y 的資料（以空格分隔）：")

# 將用戶輸入的資料轉換為數組
X = np.array(list(map(float, X_str.split())))
Y = np.array(list(map(float, Y_str.split())))

# 計算斜率和截距
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

# 顯示結果
print("斜率 (β1):", slope)
print("截距 (β0):", intercept)
print("R值:", r_value)
print("P值:", p_value)
print("標準誤差:", std_err)

# 顯示線性回歸方程式
print("線性回歸方程式：Y =", intercept, "+", slope, "X")
