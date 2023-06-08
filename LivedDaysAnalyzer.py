import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.table import Table
from datetime import datetime

if __name__ == '__main__':
    file_path = 'U.S. Presidents Birth and Death Information - Sheet1.csv'
    df = pd.read_csv(file_path)
    
    ## cleaning the data, removing entries with no death date
    df['DEATH DATE'].fillna(pd.Timestamp.today().strftime('%Y-%m-%d'), inplace=True)
    
    ## changing format of birth date and death date
    df['BIRTH DATE'] = pd.to_datetime(df['BIRTH DATE'])
    df['DEATH DATE'] = pd.to_datetime(df['DEATH DATE'])
    
    ## creating variables
    df['lived_days'] = (df['DEATH DATE'] - df['BIRTH DATE']).dt.days
    df['lived_years'] = (df['DEATH DATE'] - df['BIRTH DATE']).dt.days // 365
    df['lived_months'] = (df['DEATH DATE'] - df['BIRTH DATE']).dt.days // 30
    df['year_of_birth'] = df['BIRTH DATE'].dt.year
    
    print(df)
    
    ## top 10 president from shortest lived to longest lived
    df_temp=df.sort_values(by='lived_days')
    df_temp.drop('BIRTH DATE', axis=1, inplace=True)
    df_temp.drop('DEATH DATE', axis=1, inplace=True)
    
    print("\n\n\n Following are the details of the top 10 president from shortest lived to longest lived\n")
    print(df_temp.head(10))
    
    ## top 10 president from longest lived to shortest lived
    df_temp=df_temp.sort_values(by='lived_days', ascending=False)
    print("\n\n\n Following are the details of the top 10 president from longest lived to shortest lived\n")
    print(df_temp.head(10))
    
    # Calculate the metrics
    mean = df['lived_days'].mean()
    median = df['lived_days'].median()
    mode = df['lived_days'].mode().values
    max_value = df['lived_days'].max()
    min_value = df['lived_days'].min()
    std_deviation = df['lived_days'].std()
    
    ## metrics dataframe created
    metrics_df = pd.DataFrame({'Metric': ['Mean', 'Median', 'Mode', 'Maximum Value', 'Minimum Value', 'Standard Deviation'], 'Value': [mean, median, mode, max_value, min_value, std_deviation]})

    print("\n\n\n Metrics of number of days for the president have lived\n")
    print(metrics_df)
    
    print("======================================================")
    print(df['lived_days'])
    print("======================================================")
    # Plot a histogram of the 'DAYS LIVED' column
    plt.figure(figsize=(8, 6))
    sns.histplot(df['lived_days'], kde=True)
    plt.title('Distribution of Days Lived')
    plt.xlabel('Days Lived')
    plt.ylabel('Frequency')
    plt.show()
    # Plot a boxplot of the 'DAYS LIVED' column
    plt.figure(figsize=(8, 6))
    sns.boxplot(df['lived_days'])
    plt.title('Boxplot of Days Lived')
    plt.xlabel('Days Lived')
    plt.show()
    
    