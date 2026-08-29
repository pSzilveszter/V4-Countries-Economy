import pandas as pd
import numpy as np

print("1. Data loading in progress")
# Loading the main database
df_main = pd.read_excel("P_Data_Extract_From_World_Development_Indicators.xlsx", sheet_name='Data')
df_main = df_main.dropna(subset=['Country Code'])

# Melt (Converting to long format)
id_vars = ['Country Name', 'Country Code', 'Series Name', 'Series Code']
df_melted = pd.melt(df_main, id_vars=id_vars, var_name='Year', value_name='Value')
df_melted['Year'] = df_melted['Year'].str[:4].astype(int)
df_melted['Value'] = pd.to_numeric(df_melted['Value'].replace('..', np.nan))
df_clean = df_melted.dropna(subset=['Value'])

print("2. Loading the custom indicator list...")
# Loading indicators from Excel (from the first sheet)
df_ind = pd.read_excel("indikators.xlsx", sheet_name='Munka1')

# Extracting and cleaning WDI codes (removing spaces)
wdi_codes = df_ind['WDI-kód'].dropna().astype(str).str.strip().tolist()
df_clean['Series Code'] = df_clean['Series Code'].astype(str).str.strip()

print("3. Filtering and Pivoting (Building the Analytical Dataset)...")
# Filtering for the selected indicators
df_filtered = df_clean[df_clean['Series Code'].isin(wdi_codes)]

# Pivoting: Country and Year as rows, Indicators as columns
df_analysis = df_filtered.pivot_table(
    index=['Country Name', 'Year'],
    columns='Series Name',
    values='Value'
).reset_index()

# Cleaning column names (removing index names)
df_analysis.columns.name = None

print("\n--- THE ANALYTICAL DATABASE HAS BEEN CREATED ---")
print(df_analysis.head())

# Lementés Excelbe
output_filename = "v4_analytical_database.xlsx"
df_analysis.to_excel(output_filename, index=False)
print(f"\nSuccess! The cleaned database has been saved to: {output_filename}")
