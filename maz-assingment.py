# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load your data from the CSV file (replace 'your_data.csv' with your actual file path)
file_path = 'C:\\Users\\MAZ YAFAI\\OneDrive\\Desktop\\20110607JSU_Total_VisitorsU.csv'
data = pd.read_csv(file_path)

# Filter the data for specific countries and series
countries = ['Afghanistan', 'India', 'Pakistan']
series = 'EG.ELC.ACCS.UR.ZS'
years = ['2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]', '2006 [YR2006]', '2007 [YR2007]', '2008 [YR2008]']

filtered_data = data[data['Country Name'].isin(countries) & (data['Series Code'] == series)]
filtered_data = filtered_data.set_index('Country Name')

# Transpose the data for plotting
filtered_data = filtered_data[years].transpose()

# Create a line graph
plt.figure(figsize=(10, 6))
for country in countries:
    plt.plot(filtered_data.index, filtered_data[country], label=country)

plt.xlabel('Year')
plt.ylabel('Access to Electricity (%)')
plt.title('Access to Electricity in Urban Areas Over Time')
plt.grid(True)
plt.legend()
plt.show()


# Create a scatter plot
plt.figure(figsize=(10, 6))
for country in countries:
    plt.scatter(filtered_data.index, filtered_data[country], label=country)

plt.xlabel('Year')
plt.ylabel('Access to Electricity (%)')
plt.title('Access to Electricity in Urban Areas Over Time (Scatter Plot)')
plt.grid(True)
plt.legend()
plt.show()





# Read the data from the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\MAZ YAFAI\\OneDrive\\Desktop\\20230816Rolling12MonthsofCashReceiptsBrokenDownbyMonth1.csv')
print(df)
# Check if the required column exists
if 'InvoiceMonth' in df.columns:
    df['InvoiceMonth'] = pd.to_datetime(df['InvoiceMonth'])

# Remove commas and convert columns to numeric
df['MeatIndustryCash'] = df['MeatIndustryCash'].str.replace(',', '').fillna(0).astype(float)
df['MiscAndMilkIndustryCash'] = df['MiscAndMilkIndustryCash'].str.replace(',', '').fillna(0).astype(float)
df['RadiologicalCash'] = df['RadiologicalCash'].str.replace(',', '').fillna(0).astype(float)
df['GovernmentCash'] = df['GovernmentCash'].str.replace(',', '').fillna(0).astype(float)

# Line Plot

# # Set the 'Date' column as the index if it exists
if 'InvoiceMonth' in df.columns:
    df.set_index('InvoiceMonth', inplace=True)

# # Create the line plot if there is data to plot


# Bar Plot

# Create the bar plot if there is data to plot
if len(df) > 0:
    ax = df.plot(kind='bar', stacked=True, figsize=(12, 8))

    # Customize the plot
    ax.set_xlabel('InvoiceMonth')
    ax.set_ylabel('Values')
    ax.set_title('Bar Plot of Your Data')
    ax.legend(title='Columns', loc='upper left')

    # Convert the x-axis labels to years and months by removing the time part (00:00:00)
    x_labels = df.index.strftime('%Y-%m')
    ax.set_xticklabels(x_labels)

    plt.show()




