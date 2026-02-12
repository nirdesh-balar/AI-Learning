import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  # for plot() function,line 52

df = pd.read_csv('matches.csv')   # path of .csv file for import file 

delivery = pd.read_csv('deliveries.csv')
# print(df.head())  # top 5 row show

# print(df.tail())   # last 5 row show

# print(df.shape)    # how many rows and cols

# print(df.info())   # preview of data..

# print(df.describe())   # only work on numeric cols..

# print(df['winner'])   # access data

# print(type(df['winner']))   #t ype of data

# print(df[['team1','team2','winner']])   # Multiple data access 

# print(df.iloc[0])   # Access data one single row

# print(df.iloc[1:11:2]) # Access data line by line


'''mask=df['city']=='Hyderabad'   # Access particular item
print(mask)
print(df[mask].shape[0])      # How many item.  '''


''' we can creat function also

def get_city(city):
    mask=df['city']==city  
    return df[mask].shape[0]

print(get_city('Bangalore'))  '''


'''Multiple condition

mask1=df['city']=='Hyderabad'
mask2=df['date']>'2010-01-10'

print(df[mask1 & mask2])
print(df[mask1 & mask2].shape[0])  # How many matches. '''


# print(df['winner'].value_counts())   # count value

''' df['winner'].value_counts().plot(kind='bar')   # bar graph 
plt.show()   # print graph '''

'''df['toss_decision'].value_counts().plot(kind='pie')  # Pie chart
plt.show()  '''

# print(df['winner'].value_counts().sort_values())   # sort value

# print(df.sort_values(['city','date']))   # multiple cols sort


#######  next ch  ######

#print(delivery.head())

# run = delivery.groupby('batsman')
# print(run)
# print(run.get_group('V Kohli'))

# print(run['batsman_runs'].sum().sort_values(ascending=False).head())

# sbase jyada four kisne mari he
# ms=delivery['batsman_runs']==4
# new_delivery=delivery[ms]
# print(new_delivery.shape[0])

# name of player who hit fours
# mx = new_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False)
# print(mx)


# virat kohli ne kis team ke samane sabase jyada 4 mari

# msak= delivery[delivery['batsman']=='V Kohli']
# vk=msak.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3)
# print(vk)

# Orange cap in every season using mearge function

# new = delivery.merge(df,left_on='match_id',right_on='id')
# cap = new.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending=False).reset_index().drop_duplicates(subset='season',keep='first')
# print(cap)


# Pivot table 

# mask = delivery['batsman_runs']==6
# six = delivery[mask]

# piv = six.pivot_table(index = 'over',columns = 'batting_team',values = 'batsman_runs',aggfunc = 'count')


# sns.heatmap(piv)
# plt.show()


# corelation 

# print(df.corr)


# rename of cols

# rm=df.rename(columns={'toss_winner' : 'tw','city': 'place'})   # this is not permanate change name but if you want than "inplace=True" add in .

# print(rm)


# set index

# print(df.set_index('id',inplace=True)) # convert any column into index and remove default index provide by pandas


# reset index

# print(df.reset_index(inplace=True))  # reset changes of index in column . it is opposite of set index
# print(df)