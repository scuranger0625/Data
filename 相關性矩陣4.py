import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define your scores here
pe1_scores = [
    5, 3, 4, 2, 1, 2, 4, 4, 3, 5, 4, 4, 4, 5, 4, 4, 4, 3, 4, 4,
    4, 4, 3, 5, 5, 5, 4, 4, 4, 3, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 
    5, 4, 5, 5, 3
]
pe2_scores = [
    4, 3, 3, 3, 1, 2, 5, 3, 3, 5, 4, 3, 4, 5, 3, 4, 4, 4, 4, 4,
    5, 3, 3, 5, 5, 5, 4, 3, 5, 4, 5, 2, 5, 4, 3, 3, 4, 4, 4, 4, 
    4, 4, 5, 5, 3
]
pe3_scores = [
    5, 3, 4, 3, 1, 2, 4, 5, 3, 5, 4, 3, 5, 5, 4, 4, 4, 4, 3, 4, 
    4, 4, 3, 5, 4, 4, 4, 3, 4, 4, 4, 2, 5, 4, 3, 3, 4, 4, 3, 3, 
    4, 4, 5, 5, 3
]
ee1_scores = [
    4, 3, 3, 5, 5, 5, 4, 4, 5, 5, 4, 3, 3, 5, 3, 5, 5, 3, 3, 5, 
    4, 4, 3, 5, 5, 5, 4, 4, 4, 5, 5, 4, 5, 3, 4, 4, 4, 4, 4, 4, 
    4, 3, 5, 5, 5
]
ee2_scores = [
    4, 3, 3, 5, 5, 2, 4, 3, 5, 5, 4, 3, 3, 5, 4, 5, 5, 4, 4, 5, 
    5, 4, 3, 5, 5, 5, 4, 3, 5, 4, 5, 4, 5, 4, 4, 3, 4, 4, 4, 4, 
    4, 4, 5, 5, 4
]
ee3_scores = [
    4, 3, 2, 5, 5, 4, 4, 5, 5, 5, 4, 4, 3, 5, 4, 5, 5, 4, 4, 5, 
    4, 3, 3, 5, 5, 5, 4, 4, 4, 5, 5, 4, 5, 4, 4, 4, 4, 4, 4, 4, 
    4, 3, 5, 5, 4
]
ee4_scores = [
    3, 3, 2, 5, 5, 3, 4, 4, 4, 5, 3, 3, 3, 5, 4, 5, 5, 2, 4, 5, 
    4, 3, 3, 5, 5, 5, 4, 4, 5, 4, 5, 3, 5, 3, 4, 4, 4, 4, 2, 4, 
    5, 3, 5, 5, 4
]
si1_scores = [
    5, 3, 2, 3, 1, 1, 4, 3, 5, 5, 3, 2, 3, 5, 3, 4, 4, 2, 3, 3, 
    4, 4, 3, 5, 3, 3, 2, 3, 4, 2, 3, 3, 5, 3, 4, 3, 3, 3, 3, 3, 
    4, 3, 5, 5, 1
]
si2_scores = [
    4, 3, 4, 3, 1, 4, 4, 3, 5, 5, 3, 2, 2, 5, 2, 4, 4, 4, 3, 3, 
    4, 3, 3, 5, 3, 3, 3, 3, 4, 2, 3, 3, 5, 3, 4, 3, 3, 3, 2, 4, 
    4, 2, 4, 5, 1
]
si3_scores = [
    4, 3, 5, 3, 1, 1, 4, 3, 3, 3, 3, 3, 3, 5, 3, 4, 4, 2, 3, 3, 
    4, 3, 3, 5, 3, 3, 2, 3, 5, 2, 2, 4, 5, 2, 3, 3, 3, 3, 3, 3, 
    4, 3, 4, 5, 1
]
fc1_scores = [
    4, 3, 3, 4, 5, 3, 4, 4, 3, 5, 4, 4, 4, 5, 4, 5, 5, 4, 4, 4, 
    4, 3, 3, 5, 5, 5, 4, 4, 4, 4, 5, 4, 5, 3, 4, 4, 4, 3, 3, 4, 
    4, 5, 5, 5, 4
]
fc2_scores = [
    4, 3, 2, 5, 5, 2, 4, 4, 3, 5, 4, 4, 4, 5, 3, 5, 5, 2, 4, 4, 
    4, 4, 3, 5, 5, 5, 4, 5, 4, 4, 5, 2, 5, 2, 4, 4, 4, 3, 2, 3, 
    4, 4, 5, 5, 4
]
fc3_scores = [
    4, 3, 4, 4, 3, 4, 5, 4, 3, 5, 4, 4, 5, 5, 3, 4, 4, 3, 4, 3, 
    4, 4, 3, 5, 5, 5, 4, 4, 5, 5, 5, 3, 5, 4, 4, 4, 4, 3, 1, 4, 
    4, 5, 5, 5, 2
]
fc4_scores = [
    4, 3, 2, 3, 1, 2, 5, 4, 3, 5, 4, 4, 3, 5, 3, 4, 4, 2, 3, 4, 
    4, 4, 3, 5, 5, 5, 4, 3, 4, 4, 3, 3, 5, 4, 4, 3, 2, 3, 2, 4, 
    4, 4, 5, 5, 2
]
hm1_scores = [
    4, 4, 5, 5, 2, 3, 5, 5, 5, 5, 3, 4, 4, 5, 4, 4, 4, 3, 3, 4, 
    4, 4, 3, 5, 4, 4, 4, 5, 4, 5, 5, 5, 5, 5, 4, 4, 4, 3, 4, 5, 
    4, 4, 5, 5, 4
]
hm2_scores = [
    4, 4, 5, 5, 3, 3, 5, 5, 5, 5, 4, 4, 4, 5, 4, 4, 4, 3, 3, 4, 
    4, 4, 3, 5, 3, 3, 4, 5, 5, 5, 5, 4, 5, 3, 4, 4, 4, 3, 4, 5, 
    4, 4, 5, 5, 4
]
hm3_scores = [
    4, 4, 5, 5, 3, 4, 5, 3, 5, 5, 3, 4, 4, 5, 4, 4, 4, 4, 4, 4, 
    4, 4, 3, 5, 3, 3, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 5, 5, 
    4, 5, 5, 5, 4
]
pv1_scores = [
    4, 3, 3, 4, 3, 1, 3, 3, 5, 5, 4, 3, 4, 4, 3, 4, 4, 2, 3, 4, 
    3, 4, 3, 5, 4, 4, 4, 2, 4, 5, 3, 3, 5, 3, 3, 3, 3, 3, 2, 3, 
    4, 3, 3, 5, 3
]
pv2_scores = [
    4, 3, 3, 3, 3, 1, 3, 4, 5, 4, 3, 3, 3, 4, 3, 4, 4, 2, 3, 4, 
    3, 4, 3, 5, 3, 3, 4, 2, 4, 5, 5, 3, 5, 4, 3, 3, 3, 3, 3, 3, 
    4, 3, 4, 5, 3
]
pv3_scores = [
    4, 3, 2, 3, 3, 3, 3, 4, 5, 5, 4, 4, 3, 4, 3, 4, 4, 3, 3, 4, 
    3, 4, 3, 5, 5, 5, 4, 2, 5, 5, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 
    5, 4, 4, 5, 3
]
ht1_scores = [
    4, 3, 2, 2, 1, 1, 2, 2, 5, 5, 4, 4, 3, 5, 2, 4, 4, 2, 3, 4, 
    1, 4, 3, 5, 5, 5, 4, 3, 5, 2, 2, 3, 5, 3, 2, 3, 4, 3, 2, 3, 
    4, 3, 5, 5, 1
]
ht2_scores = [
    5, 3, 2, 2, 1, 1, 1, 2, 5, 5, 2, 2, 2, 5, 2, 4, 4, 1, 3, 2, 
    1, 3, 2, 5, 2, 2, 3, 1, 3, 1, 2, 4, 5, 3, 2, 3, 2, 4, 2, 3, 
    4, 1, 3, 5, 1
]
ht3_scores = [
    4, 3, 1, 1, 1, 1, 1, 2, 5, 5, 4, 2, 3, 5, 3, 4, 4, 2, 3, 3, 
    1, 4, 2, 5, 2, 2, 4, 2, 4, 2, 2, 2, 5, 3, 3, 3, 2, 2, 3, 3, 
    4, 3, 3, 5, 1
]
bi1_scores = [
    4, 3, 2, 2, 1, 1, 4, 4, 5, 5, 4, 4, 4, 5, 3, 4, 4, 3, 3, 4, 
    1, 4, 3, 5, 5, 5, 4, 4, 5, 3, 5, 3, 5, 4, 3, 4, 4, 4, 3, 3, 
    4, 4, 3, 5, 2
]
bi2_scores = [
    4, 3, 3, 1, 1, 1, 2, 3, 5, 5, 4, 4, 4, 5, 3, 4, 4, 2, 3, 4, 
    1, 3, 3, 5, 5, 5, 4, 4, 4, 2, 4, 2, 5, 4, 3, 3, 4, 3, 2, 3, 
    4, 4, 4, 5, 2
]
bi3_scores = [
    4, 3, 2, 2, 1, 1, 3, 3, 5, 5, 4, 4, 5, 5, 3, 4, 4, 2, 3, 4, 
    1, 3, 3, 5, 5, 5, 4, 4, 5, 3, 5, 4, 5, 4, 3, 4, 4, 3, 2, 3, 
    4, 3, 4, 5, 2
]

# 定義各變量的分數
pe_scores = [pe1_scores, pe2_scores, pe3_scores]
ee_scores = [ee1_scores, ee2_scores, ee3_scores, ee4_scores]
si_scores = [si1_scores, si2_scores, si3_scores]
fc_scores = [fc1_scores, fc2_scores, fc3_scores, fc4_scores]
hm_scores = [hm1_scores, hm2_scores, hm3_scores]
pv_scores = [pv1_scores, pv2_scores, pv3_scores]
ht_scores = [ht1_scores, ht2_scores, ht3_scores]
bi_scores = [bi1_scores, bi2_scores, bi3_scores]

# 合併相同構念的題目
pe_avg = pd.Series(sum(pe_scores, [])).rename("PE")
ee_avg = pd.Series(sum(ee_scores, [])).rename("EE")
si_avg = pd.Series(sum(si_scores, [])).rename("SI")
fc_avg = pd.Series(sum(fc_scores, [])).rename("FC")
hm_avg = pd.Series(sum(hm_scores, [])).rename("HM")
pv_avg = pd.Series(sum(pv_scores, [])).rename("PV")
ht_avg = pd.Series(sum(ht_scores, [])).rename("HT")
bi_avg = pd.Series(sum(bi_scores, [])).rename("BI")

# 將合併後的數據放入DataFrame
merged_data = pd.concat([pe_avg, ee_avg, si_avg, fc_avg, hm_avg, pv_avg, ht_avg, bi_avg], axis=1)

# 計算相關係數矩陣
correlation_matrix = merged_data.corr()

# 繪製熱圖
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Pearson Correlation Heatmap')
plt.show()