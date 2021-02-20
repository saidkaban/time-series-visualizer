import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=True)

# Clean data
df = df[(df["value"] <= df["value"].quantile(0.975)) & (df["value"] >= df["value"].quantile(0.025))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(25, 8))
    plt.plot(df, color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar["month"] = df_bar["value"].index.month.to_list()
    df_bar["month"] = [months[num - 1] for num in df_bar["month"]]
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months)

    df_pivot = pd.pivot_table(
    df_bar,
    values="value",
    index="year",
    columns="month",
    aggfunc=np.mean)

    # Draw bar plot

    ax = df_pivot.plot(kind="bar")

    fig = ax.get_figure()
    fig.set_size_inches(10, 10)

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box["month"] = pd.Categorical(df_box["month"], categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box["year"], y =df_box["value"])
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")

    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box["month"] , y =df_box["value"])
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig