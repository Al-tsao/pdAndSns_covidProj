#載入模組
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime #用來設定treshold時間格式
from dateutil.relativedelta import relativedelta #用來做日期加減

#讓文字靠右對齊
# 这两个参数的默认设置都是False
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

#讀取Excel資料
df = pd.read_excel('covidtable_taiwan_cdc_death.xlsx', sheet_name="Sheet1") #pd會自動轉化成DataFrame

#查看資料形狀
print('\n')
print('資料型態')
print('Row:', df.shape[0], 'Column:', df.shape[1])
print('============================================')

#讀取column中的title
title = pd.DataFrame({'Title': df.columns})
print('Title名稱', title, sep='\n')
print('============================================')

#獲取目標資料
DeathCase = pd.DataFrame(df, columns=['性別','年齡','確診日'])
DeathCase = DeathCase.rename(columns={'性別':'Gender','年齡': 'Age','確診日': 'Confirmed Date'})

#檢查年齡是否有負值
print('檢查是否有負值: 最小值',np.amin(DeathCase['Age']))
print('============================================')

#轉換日期成日期格式
DeathCase['Confirmed Date'] = pd.to_datetime(DeathCase['Confirmed Date'], format='%Y/%m/%d')

#因為所有資料都是2021年，因此如果資料中日期>2021/10/1號的資料，全部將年改成2020
threshold = datetime.datetime.strptime("2021/09/30","%Y/%m/%d")
confirmedDateList = []
for inx, val in enumerate(DeathCase['Confirmed Date']):
    if val > threshold:
        # DeathCase['Confirmed Date'].iloc[inx]= val - relativedelta(years=1)
        confirmedDateList.append(val - relativedelta(years=1))
    else:
        confirmedDateList.append(val)
DeathCase['Confirmed Date'] = confirmedDateList

#依照日期排序
DeathCase = DeathCase.sort_values(by='Confirmed Date', ascending=True)
# print(DeathCase)

#取代男女變成英文
genderList = []
for inx, val in enumerate(DeathCase['Gender']):
    if val == '男':
        # DeathCase['Gender'].iloc[inx] = 'Male'
        genderList.append('Male')
    elif val == '女':
        # DeathCase['Gender'].iloc[inx] = 'Female'
        genderList.append('Female')
DeathCase['Gender'] = genderList

#繪圖
sns.set()
heatmap = sns.scatterplot(data=DeathCase, x="Age", y="Confirmed Date", hue="Gender")
plt.show()

#另存成excel檔
# DeathCase.to_excel('result.xlsx') 