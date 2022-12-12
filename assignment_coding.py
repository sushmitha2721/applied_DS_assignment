import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dataframes_make(path_dataset):
    clim_df = pd.read_csv(path_dataset)
    clim_df_transpose = pd.DataFrame.transpose(clim_df)
    h = clim_df_transpose.iloc[0].values.tolist()
    clim_df_transpose.columns = h
    clim_df=clim_df.drop(columns=['Indicator Code','Country Code'])
    clim_df_transpose=clim_df_transpose.iloc[4:]
    return clim_df_transpose,clim_df

def lines_ploting(df,indicator):
    indicat_df = df[df['Indicator Name']== indicator]
    indicat_df=indicat_df.drop(columns=['Indicator Name'])
    indicat_df=indicat_df.transpose()
    indicat_df.columns = indicat_df.iloc[0].values.tolist()
    indicat_df=indicat_df.iloc[1:,:]
    indicat_df[40:60].plot(kind='line',figsize=(20,10))
    plt.ylabel(indicator)
    plt.title(indicator+" of countries in G7")
    plt.xlabel('years')
    plt.show()

def correlations_plotting(dataframe,indicatr_name,g7_country):
    correlation_df=dataframe[dataframe['Country Name']==g7_country]
    x=[]
    for indi in indicatr_name:
        tem_df=correlation_df[correlation_df['Indicator Name']==indi]
        tem_df=tem_df.squeeze()
        x.append(tem_df)
    correlation_df=pd.DataFrame(x)
    correlation_df=correlation_df.iloc[:,1:]
    correlation_df=correlation_df.transpose()
 
    correlation_df.columns = correlation_df.iloc[0].values.tolist()
    correlation_df=correlation_df.iloc[1:,:]
    correlation_df=correlation_df.iloc[45:60,:]
    correlation_df=correlation_df.fillna(correlation_df.mean())
    sns.heatmap(
        correlation_df.corr(), annot=True
    )
    plt.title(g7_country+" indicators correlation")
    plt.show()


#getting two dataframees
countries_cols, years_cols = dataframes_make('world_dataset.csv')
#getting indicators names and countries 
indicat_names=years_cols.iloc[:,1].unique()
countries= countries_cols.columns.unique()

G7_countries=['Canada',' France', 'Germany', 'Italy', 'Japan', 'United Kingdom','United States']

#using years as col dataframe to get all the G7countries data
g7_dataframe = years_cols[years_cols['Country Name'] == G7_countries[0]]
for country in G7_countries[1:]:
    g7_dataframe = pd.concat([g7_dataframe,years_cols[years_cols['Country Name'] == country]])


#barplot 
indicat='Urban population'
indicat_df = g7_dataframe[g7_dataframe['Indicator Name']== indicat]
indicat_df =indicat_df .drop(columns=['Indicator Name'])
indicat_df =indicat_df .transpose()

indicat_df.columns = indicat_df .iloc[0].values.tolist()
indicat_df =indicat_df.iloc[1:,:]
indicat_df [45:].plot(kind='bar',figsize=(20,10))
plt.ylabel("urban population in G7 from 2005")
plt.title('Urban population')
plt.xlabel('years')
plt.show()

#barplot 
indi='Total greenhouse gas emissions (kt of CO2 equivalent)'
indi_df = g7_dataframe[g7_dataframe['Indicator Name']== indi]
indi_df =indi_df .drop(columns=['Indicator Name'])
indi_df =indi_df .transpose()
header = indi_df .iloc[0].values.tolist()
indi_df .columns = header
indi_df =indi_df.iloc[1:,:]
   
indi_df [45:60].plot(kind='bar',figsize=(20,10))
plt.ylabel('Total greenhouse gas emissions (kt of CO2 equivalent)')
plt.title('Total greenhouse gas emissions (kt of CO2 equivalent) in G7 from 2005')
plt.xlabel('years')
plt.show()


#correlation plot
indi_for_correlation = ['Urban population','Mortality rate, under-5 (per 1,000 live births)','CO2 emissions (kt)','Electric power consumption (kWh per capita)','Electricity production from oil sources (% of total)']
correlations_plotting(g7_dataframe, indi_for_correlation, 'Canada')
correlations_plotting(g7_dataframe, indi_for_correlation,'Italy')

#line plot
lines_ploting(g7_dataframe, 'Electricity production from natural gas sources (% of total)')
lines_ploting(g7_dataframe, 'Electricity production from hydroelectric sources (% of total)')
lines_ploting(g7_dataframe, 'Electricity production from renewable sources, excluding hydroelectric (% of total)')

