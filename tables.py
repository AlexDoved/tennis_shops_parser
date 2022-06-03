import os

import pandas as pd


def save_to_table(brand: str, category: str, names: list, links: list,
                  prices: list) -> None:
    """Сохранение результатов в таблицу Excel."""
    df = pd.DataFrame({
        'Name': names,
        'Link': links,
        'Price': prices
    })
    file_path = 'tables'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    writer = pd.ExcelWriter(f'tables/{brand}_{category}.xlsx')
    df.to_excel(writer, sheet_name=brand, index=False, na_rep='NaN')
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets[brand].set_column(col_idx, col_idx, column_width)
    writer.save()
