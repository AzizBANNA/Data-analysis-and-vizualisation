import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


df_by = pd.read_csv('https://raw.githubusercontent.com/entorb/COVID-19-Coronavirus-German-Regions/main/data/de-states/de-state-BY.tsv' ,sep='\t')
df_by['State'] = 'BY'
df_nw= pd.read_csv('https://raw.githubusercontent.com/entorb/COVID-19-Coronavirus-German-Regions/main/data/de-states/de-state-NW.tsv' , sep='\t')
df_nw['State']= 'NW'
df_sn =pd.read_csv('https://raw.githubusercontent.com/entorb/COVID-19-Coronavirus-German-Regions/main/data/de-states/de-state-SN.tsv' , sep= '\t')
df_sn['State']= 'SN'
df_th = pd.read_csv('https://raw.githubusercontent.com/entorb/COVID-19-Coronavirus-German-Regions/main/data/de-states/de-state-TH.tsv' , sep='\t')
df_th['State']= 'TH'
df_ger = pd.read_csv('https://raw.githubusercontent.com/entorb/COVID-19-Coronavirus-German-Regions/main/data/de-states/de-state-DE-total.tsv' , sep='\t')
#ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
fig = plt.figure(figsize=(12, 6)) 
axes = fig.add_subplot() 
axes.plot(df_by['Date'], df_by['Cases_Last_Week_Per_Million'], label='BY')
axes.plot(df_nw['Date'], df_nw['Cases_Last_Week_Per_Million'], label='NW')
axes.plot(df_sn['Date'], df_sn['Cases_Last_Week_Per_Million'], label='SN')
axes.plot(df_th['Date'], df_th['Cases_Last_Week_Per_Million'], label='TH')
axes.xaxis.set_major_locator(mdates.MonthLocator(interval=5))
df= pd.concat([df_by,df_nw, df_sn,df_th], ignore_index=True) 
maxcases = df['Cases_Last_Week_Per_Million'].max()
date_maxcases= df['Date'][df["Cases_Last_Week_Per_Million"].argmax()]
max_state = df['State'][df["Cases_Last_Week_Per_Million"].argmax()]
axes.annotate(f'Maximum n={maxcases} in {max_state} @{date_maxcases}' , xy=(date_maxcases,maxcases) , arrowprops=dict(facecolor='b')) 
plt.yscale(value='log')
plt.legend()
plt.xlabel('Date')
plt.title('7 days incidence/mio of covid cases')
plt.ylabel('n/(week . million)')
plt.grid()
inset_ax = inset_axes(axes, width="40%", height="25%" ,loc=4 , borderpad=2) 
inset_ax.plot(df_ger['Date'], df_ger['Cases_Last_Week_Per_Million'])
inset_ax.xaxis.set_major_locator(mdates.MonthLocator(interval=9))
inset_ax.grid()
plt.yscale(value='log')
plt.legend()
plt.title('incidence in whole germany')
plt.savefig('homeworks/chapter_6/ex1_covid_plot/plot.pdf')
plt.show()

