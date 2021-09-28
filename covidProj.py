#載入模組
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#讓文字靠右對齊
# 这两个参数的默认设置都是False
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

#讀取Excel資料
df = pd.read_excel('owl_world.xlsx', sheet_name="Sheet1") #pd會自動轉化成DataFrame

#查看資料形狀
print('Row:', df.shape[0], 'Column:', df.shape[1])

#讀取column中的title
title = pd.DataFrame({'Title': df.columns})
# print(title)

#獲取目標資料
confirmedCase = pd.DataFrame(df, columns=['日期','新增確診數'])
confirmedCase = confirmedCase.rename(columns={'日期':'Date', '新增確診數': 'New confirmed Case'})
# confirmedCase['New confirmed Case'][412]<0

#檢查是否有負值
print('最小值',np.amin(confirmedCase['New confirmed Case']))

#取代負數為0
list = confirmedCase['New confirmed Case'].tolist()
for idx, val in enumerate(list):
    if val<=0:
         list[idx] = 0
confirmedCase['New confirmed Case'] = list

#檢查是否有負值
print('再次檢查最小值',np.amin(confirmedCase['New confirmed Case']))

#反轉資料，讓越新的資料排到下面
confirmedCase = confirmedCase.iloc[::-1]

#用seaborn繪圖
sns.set()
sns.barplot(x='Date', y='New confirmed Case', color='b', linewidth=0 ,data=confirmedCase).set(xticks=[0,618], xticklabels=['2020/01/16','2020/09/25'])
plt.show()