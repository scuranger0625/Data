import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distribution(mean, std_dev, value):
    # 生成一個包含從平均值-3倍標準差到平均值+3倍標準差的數據範圍
    x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)
    # 計算對應x值的標準常態分佈的概率密度函數值
    y = norm.pdf(x, mean, std_dev)

    # 繪製標準常態分佈曲線
    plt.plot(x, y, label='Normal Distribution')

    # 標註給定值對應的點
    plt.scatter(value, norm.pdf(value, mean, std_dev), color='red', label='Given Value')

    # 在圖表上標註68.2-95-99.7規則
    plt.axvline(mean - std_dev, color='red', linestyle='--', label='68.2% of data')
    plt.axvline(mean + std_dev, color='red', linestyle='--')
    plt.axvline(mean - 2*std_dev, color='green', linestyle='--', label='95% of data')
    plt.axvline(mean + 2*std_dev, color='green', linestyle='--')
    plt.axvline(mean - 3*std_dev, color='blue', linestyle='--', label='99.7% of data')
    plt.axvline(mean + 3*std_dev, color='blue', linestyle='--')

    # 添加顯示平均數的線
    plt.axvline(mean, color='orange', linestyle='--', label='Mean')

    # 設置圖表標題和軸標籤
    plt.title('Normal Distribution with Mean={} and Standard Deviation={}'.format(mean, std_dev))
    plt.xlabel('Values')
    plt.ylabel('Probability Density')

    # 添加圖例
    plt.legend()

    # 顯示圖表
    plt.show()

def calculate_z_score(mean, std_dev, value):
    # 計算Z分數
    z_score = (value - mean) / std_dev
    # 計算常態分佈的累積機率
    cum_prob = norm.cdf(value, mean, std_dev)
    # 計算尾機率
    tail_prob = 1 - cum_prob
    return z_score, cum_prob, tail_prob

def main():
    mean = float(input("請輸入常態分佈的平均值："))
    std_dev = float(input("請輸入常態分佈的標準差："))

    # 輸入要計算的值
    value = float(input("請輸入一個值："))

    # 計算Z分數、常態分佈的累積機率和尾機率
    z_score, cum_prob, tail_prob = calculate_z_score(mean, std_dev, value)

    # 輸出結果
    print("給定值的 Z 分數為：{:.4f}".format(z_score))
    print("常態分佈的累積機率：{:.4f}".format(cum_prob))
    print("常態分佈的尾機率：{:.4f}".format(tail_prob))

    # 繪製常態分佈圖表
    plot_normal_distribution(mean, std_dev, value)

if __name__ == "__main__":
    main()


