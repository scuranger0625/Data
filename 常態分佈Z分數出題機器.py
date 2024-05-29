from scipy.stats import norm
import random

def calculate_probability_and_tail(mean, std_dev, score):
    """
    計算給定分數對應的Z分數、常態分佈概率和尾概率。

    參數：
    mean (float)：常態分佈的平均值。
    std_dev (float)：常態分佈的標準差。
    score (float)：要計算的分數。

    返回：
    tuple: 包含Z分數、常態分佈概率和尾概率的元組。
    """
    z_score = (score - mean) / std_dev
    probability = norm.cdf(z_score)
    tail_probability = norm.sf(z_score)
    return z_score, probability, tail_probability

def generate_question():
    """
    生成一個常態分佈的題目，包含隨機生成的平均值、標準差和分數。

    返回：
    tuple: 包含平均值、標準差、分數和正確答案的元組。
    """
    mean = random.randint(60, 80)  # 隨機生成整數平均值
    std_dev = random.randint(5, 15)  # 隨機生成整數標準差
    score = round(random.uniform(40, 100))  # 隨機生成40到100之間的浮點數，並四捨五入為整數

    z_score, probability, tail_probability = calculate_probability_and_tail(mean, std_dev, score)
    correct_answer = (z_score, probability, tail_probability)

    return mean, std_dev, score, correct_answer

def main():
    print("歡迎使用常態分佈的計算器！")
    print("請計算以下常態分佈的題目：")
    
    mean, std_dev, score, correct_answer = generate_question()
    print("給定常態分佈的平均值為 {}，標準差為 {}，要計算的分數為 {}。".format(mean, std_dev, score))
    
    user_answer = input("請輸入你認為的 Z 分數、常態分佈概率和尾概率（用空格分隔）：")
    try:
        user_z, user_prob, user_tail_prob = map(float, user_answer.split())
        if (user_z, user_prob, user_tail_prob) == correct_answer:
            print("回答正確！")
        else:
            print("回答錯誤。正確答案是：Z 分數 {:.2f}，常態分佈概率 {:.4f}，尾概率 {:.4f}".format(*correct_answer))
    except ValueError:
        print("輸入的值無效，請確保輸入的是有效的數字！")

if __name__ == "__main__":
    main()




