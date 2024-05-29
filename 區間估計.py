# 4-4 抽樣分配與標準誤
#隨機抽樣的兩個前提:每個個體的被抽中機率相同、每次抽出必須放回再抽
#抽樣分配:反覆無限次抽樣


import math

def interval_estimate(est_parameter, std_deviation, sample_size, confidence_level):
    if confidence_level == 95:
        z_value = 1.96
    elif confidence_level == 99:
        z_value = 2.58
    else:
        raise ValueError("Confidence level must be 95 or 99.")
    
    std_error = std_deviation / math.sqrt(sample_size)
    
    lower_bound = est_parameter - z_value * std_error
    upper_bound = est_parameter + z_value * std_error
    
    return lower_bound, upper_bound

def main():
    est_parameter = float(input("請輸入估計參數："))
    std_deviation = float(input("請輸入標準差："))
    sample_size = int(input("請輸入樣本數量："))
    confidence_level = int(input("請輸入信賴區間（95 或 99）："))

    lower_bound, upper_bound = interval_estimate(est_parameter, std_deviation, sample_size, confidence_level)

    print(f"{confidence_level}% 區間估計結果：({lower_bound}, {upper_bound})")

if __name__ == "__main__":
    main()

