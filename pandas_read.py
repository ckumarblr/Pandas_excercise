import pandas as pd

#
df = pd.read_csv('pokemon_data.csv')
# # print(df.head(4))
#
# # Print all columns
print(list(df.columns))
# print(type(df.columns))  # INDEX
#
# # Read column
# print(df['Defense'])
# print(type(df['Defense']))  # Series
#
# # Read columns
#
# print(df[['Defense','Speed'][0:5]])
# print(df[['Defense','Speed']][0:5])
# print(type(df['Defense']))  # Series

# print a specific row
# print(df.iloc[0])
# print a specific row between 0 and 6
# print(df.iloc[0:6])

# print a specific row and column
# print(df.iloc[1, 4])


# # iterate over rows - iterrows
# for index, row in df.iterrows():
#     print(index, row[2],row[3],row[-1])
# print(index[5],row[5])

# loc methods for showing only a subset as per the condition passed
# print(df.loc[df['Type 1'] == 'Fire'])
# print(df.loc[df['Legendary'] == False])


# describe the data
# print(df.describe())

# sort values
# print(df.sort_values('Name', ascending=False))
# print(df.sort_values(['Name', 'Speed'], ascending=(1, 0)))

# having a total column and then dropping it \
df['Total'] =  df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# Question for AVi
# for index, rows in df.iterrows():
#     df['Total_len'] += rows[4:9]
#
# print(df['Total_len'])

# drop in place a specific column , the input is a hashable :
df.drop(columns=['Total'],inplace=True)
# alternate way to store sum  :

print(df.columns)


    # df_excel = pd.read_excel('pokemon_data.xlsx')
    # print(df_excel.head(4))
    # print(df_excel.columns)
