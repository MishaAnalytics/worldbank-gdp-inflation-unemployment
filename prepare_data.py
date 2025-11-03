import pandas as pd
gdp = pd.read_csv('raw data/gdp.csv', skiprows=3)
inflation = pd.read_csv('raw data/inflation.csv', skiprows=3)
unemployment = pd.read_csv('raw data/unemployment.csv', skiprows=3)

for df in [gdp, inflation, unemployment]:
    df.rename(columns={'Country Name': 'Country'}, inplace=True)


years = [str(y) for y in range(1960, 2025)]

gdp_long = pd.melt(gdp, id_vars=['Country'], value_vars=years,
                   var_name='Year', value_name='GDP')
inflation_long = pd.melt(inflation, id_vars=['Country'], value_vars=years,
                         var_name='Year', value_name='Inflation')
unemployment_long = pd.melt(unemployment, id_vars=['Country'], value_vars=years,
                            var_name='Year', value_name='Unemployment')

merged = gdp_long.merge(inflation_long, on=['Country','Year'], how='outer') \
                 .merge(unemployment_long, on=['Country','Year'], how='outer')


merged['Year'] = merged['Year'].astype(int)

average_df = merged.groupby('Year')[['GDP','Inflation','Unemployment']].mean().reset_index()
average_df['Country'] = 'Average'

merged_with_avg = pd.concat([merged, average_df[['Country','Year','GDP','Inflation','Unemployment']]],
                            ignore_index=True)

merged_with_avg = merged_with_avg.sort_values(by=['Country','Year'])

merged_with_avg.to_csv('merged_data_with_avg.csv', index=False)
print("final table is complete and named: 'merged_data_with_avg.csv'")

