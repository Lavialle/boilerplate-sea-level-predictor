import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize=(12,5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(1880, 2051)
    plt.plot(x, slope * x + intercept)
    # Create second line of best fit
    df_after_2000 = df[df['Year'] >=2000]
    slope, intercept, r, p, se = linregress(df_after_2000['Year'], df_after_2000['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    plt.plot(x2, slope * x2 + intercept)
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.xlim(1850, 2076)
    plt.xticks(range(1850, 2076, 25))
    plt.ylabel('Sea Level (inches)')
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
