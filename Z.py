import scipy.stats as stats
import pandas as pd

# 设置Z分数范围，从0.00到4.00，步长为0.01
z_scores = [round(0.01 * i, 2) for i in range(401)]

# 计算累积概率和尾概率
cumulative_probs = [stats.norm.cdf(z) for z in z_scores]
tail_probs = [2 * (1 - cp) for cp in cumulative_probs]

# 创建DataFrame
data = {'Z': z_scores, 'Cumulative Probability': cumulative_probs, 'Tail Probability': tail_probs}
df = pd.DataFrame(data)

# 输出到CSV文件
df.to_csv('normal_distribution_table_consistent.csv', index=False)

print("Consistent table generated and saved as 'normal_distribution_table_consistent.csv'.")

