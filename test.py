import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline
plt.style.use('seaborn')

crimes = pd.read_csv('file.csv',error_bad_lines=False)

print ('Dataset ready..')

print('Dataset Shape before drop_duplicate : ', crimes.shape)
crimes.drop_duplicates(subset=['COMPNOS'], inplace=True)
print('Dataset Shape after drop_duplicate: ', crimes.shape)

crimes.drop(['COMPNOS', 'NatureCode', 'MAIN_CRIMECODE', 'Location', 'UCRPART',
    'DOMESTIC', 'REPORTINGAREA', 'XSTREETNAME'], inplace=True, axis=1)

#print(crimes.head(3))

crimes.Date = pd.to_datetime(crimes.FROMDATE, format='%m/%d/%Y %I:%M:%S %p')
# setting the index to be the date will help us a lot later on
crimes.index = pd.DatetimeIndex(crimes.Date)

print(crimes.info())
print(crimes.shape)

#loc_to_change = list(crimes['STREETNAME'].value_counts()[20:].index)
#desc_to_change = list(crimes['INCIDENT_TYPE_DESCRIPTION'].value_counts()[20:].index)

#crimes.loc[crimes['STREETNAME'].isin(loc_to_change), crimes.columns=='STREETNAME'] = 'OTHER'
#crimes.loc[crimes['INCIDENT_TYPE_DESCRIPTION'].isin(desc_to_change), crimes.columns=='INCIDENT_TYPE_DESCRIPTION'] = 'OTHER'

#crimes['STREETNAME'] = pd.Categorical(crimes['STREETNAME Type'])
#crimes['INCIDENT_TYPE_DESCRIPTION'] = pd.Categorical(crimes['INCIDENT_TYPE_DESCRIPTION Type'])

plt.figure(figsize=(11, 7))
crimes.resample('M').size().plot(legend=False)
plt.title('Number of crimes per month (2012-2015)')
plt.xlabel('Month')
plt.ylabel('Number of crimes')
plt.show()

plt.figure(figsize=(11, 4))
crimes.resample('D').size().rolling(365).sum().plot()
plt.title('Rolling sum of all crimes from 2012 - 2015')
plt.ylabel('Number of crimes')
plt.xlabel('Days')
plt.show()

#crimes_count_date = crimes.pivot_table('REPTDISTRICT',
#        aggfunc=np.size, columns='INCIDENT_TYPE_DESCRIPTION',
#        index=crimes.index.date, fill_value=0)
#crimes_count_date.index = pd.DatetimeIndex(crimes_count_date.index)
#plo = crimes_count_date.rolling(365).sum().plot(figsize=(12, 30), subplots=True,
#        layout=(-1, 3), sharex=False, sharey=False)

