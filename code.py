# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)

#Code starts here



# --------------
#Code starts here

data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer',
(np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter')))


better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)

#data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])




# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(countries,cols):
    country_list=[];
    top10=countries.nlargest(10,cols);
    #print(top10)
    country_list=top10['Country_Name']
    return list(country_list)


top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
print(top_10_summer)
print(top_10_winter)
print(top_10)
common= list(set(top_10_summer) & set(top_10_winter) &  set(top_10));
#common= [x for x in top_10_summer if x in top_10_winter and x in top_10 ]
print(common)



# --------------
#Code starts here

summer_df= data[data['Country_Name'].isin(top_10_summer)];
winter_df= data[data['Country_Name'].isin(top_10_winter)];
top_df= data[data['Country_Name'].isin(top_10)];
#summer_df.set_index('Country_Name',inplace=True)
#print(summer_df.head(10))

summer_df.plot.bar(x='Country_Name',y='Total_Summer')
winter_df.plot.bar(x='Country_Name',y='Total_Winter')
top_df.plot.bar(x='Country_Name',y='Total_Medals')
#plt.bar(summer_df['Total_Summer'])



# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_df.set_index('Country_Name',inplace=True)
summer_country_gold=summer_df['Golden_Ratio'].idxmax()
#summer_country_gold=data['count']
print(summer_max_ratio)
print(summer_country_gold)




winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_df.set_index('Country_Name',inplace=True)
winter_country_gold=winter_df['Golden_Ratio'].idxmax()
#summer_country_gold=data['count']
print(winter_max_ratio)
print(winter_country_gold)



top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_df.set_index('Country_Name',inplace=True)
top_country_gold=top_df['Golden_Ratio'].idxmax()
#summer_country_gold=data['count']
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
le=len(data)
#print(le)
#print(data.tail(1))
data.drop(index=(le-1),axis=0,inplace=True)
#data_1=data[:]
#print(data.tail(1))
#data.drop(data.tail(1).index,inplace=True)
data_1=data[:]
data_1['Total_Points'] =  (3*data_1['Gold_Total'])+ (2*data_1['Silver_Total']) + 1*(data_1['Bronze_Total'])
data_1.set_index('Country_Name',inplace=True)
most_points=data_1['Total_Points'].max()
best_country=data_1['Total_Points'].idxmax()
print(data_1.head(5))
data_1.reset_index(inplace=True)
#print(data_1.head(1))
print(data_1.head(5))
print(most_points)
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name'] == best_country]
#print(best)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
#print(best)
best.plot.bar(stacked=True,figsize=(15,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


