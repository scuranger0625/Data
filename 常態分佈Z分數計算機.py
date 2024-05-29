# 常態分佈Z分數計算機.py   (本程式屬於統計與數據分析應用，可以使用在教育、市場研究、金融、醫學用途)
# 課本3-24 4-11

from scipy.stats import norm

def calculate_z_score(mean, std_dev, score):
    """
    計算給定分數對應的Z分數。

    參數：
    mean (float)：常態分佈的平均值。
    std_dev (float)：常態分佈的標準差。
    score (float)：要計算的分數。

    返回：
    float: Z分數。
    """
    z_score = (score - mean) / std_dev
    return z_score

def main():
    print("歡迎使用Z分數計算機！")
    try:
        # 讓使用者輸入常態分佈的參數和要計算的分數
        mean = float(input("請輸入常態分佈的平均值："))
        std_dev = float(input("請輸入常態分佈的標準差："))
        score = float(input("請輸入要計算的分數："))

        # 計算Z分數
        z_score = calculate_z_score(mean, std_dev, score)

        # 輸出結果
        print("給定分數 {}，對應的 Z 分數為: {:.2f}".format(score, z_score))
    except ValueError:
        print("輸入的值無效，請確保輸入的是有效的數字！")

if __name__ == "__main__":
    main()






