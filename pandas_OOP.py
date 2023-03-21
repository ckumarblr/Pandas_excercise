import pandas as pd
from typing import List


class PokemonData:
    def __init__(self, csv_file_path: str):
        self.df = pd.read_csv(csv_file_path)

    def print_head(self, n: int) -> None:
        print(self.df.head(n))

    def get_columns(self) -> List[str]:
        return list(self.df.columns)

    def get_column(self, column_name: str) -> pd.Series:
        return self.df[column_name]

    def get_columns_subset(self, column_names: List[str], n: int) -> pd.DataFrame:
        return self.df[column_names][0:n]

    def get_row(self, index: int) -> pd.Series:
        return self.df.iloc[index]

    def get_rows_subset(self, start: int, end: int) -> pd.DataFrame:
        return self.df.iloc[start:end]

    def get_value(self, row_index: int, column_index: int) -> str:
        return self.df.iloc[row_index, column_index]

    def iterate_over_rows(self) -> None:
        for index, row in self.df.iterrows():
            print(index, row[2], row[3], row[-1])

    def loc(self, condition: str) -> pd.DataFrame:
        return self.df.loc[self.df['Type 1'] == condition]

    def describedata(self) -> pd.DataFrame:
        return self.df.describe()

    def sort_values(self, column_names: List[str], ascending: List[bool]) -> pd.DataFrame:
        return self.df.sort_values(column_names, ascending=ascending)

    def add_total_column(self) -> None:
        self.df['Total'] = self.df['HP'] + self.df['Attack'] + self.df['Defense'] + self.df['Sp. Atk'] + self.df[
            'Sp. Def'] + self.df['Speed']

    def compute_totals(self, start: int, end: int) -> pd.Series:
        return self.df.iloc[start:end, 4:10].sum(axis=1)

    def drop_column(self, column_name: str) -> None:
        self.df.drop(columns=[column_name], inplace=True)


if __name__ == '__main__':
    data = PokemonData('pokemon_data.csv')
    data.print_head(4)
    print(data.get_columns())
    print(data.get_column('Defense'))
    print(data.get_columns_subset(['Defense', 'Speed'], 5))
    print(data.get_row(0))
    print(data.get_rows_subset(0, 6))
    print(data.get_value(1, 4))
    data.iterate_over_rows()
    print(data.loc('Fire'))
    print(data.describedata())
    print(data.sort_values(['Name', 'Speed'], [True, False]))
    data.add_total_column()
    print(data.compute_totals(4, 10))
    data.drop_column('Total')

    # Reading Excel file
    df_excel = pd.read_excel('pokemon_data.xlsx')
    print(df_excel.head(4))
    print(df_excel.columns)
