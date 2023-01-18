import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = 'date', parse_dates=True)

# Clean data to filter out top 2.5% of the dataset or bottom 2.5% of the dataset. 
df2 = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (12, 6))
    plt.plot(df2, "g")
    plt.ticklabel_format(style="plain", axis="y")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df2.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month_name()

    # Draw bar plot
    fig = plt.figure(figsize = (12, 6))
    sns.barplot(x=df_bar['year'], y=df_bar['value'], hue=df_bar['month'], hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.legend(title="month", loc="upper left")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df2.copy()
    df_box['year'] = pd.DatetimeIndex(df_box.index).year
    df_box['month'] = pd.DatetimeIndex(df_box.index).month_name()
    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize = (12, 6))

    fig.add_subplot(1,2,1)
    sns.boxplot(x=df_box["year"], y=df_box["value"], palette='Set2')
    plt.ticklabel_format(style="plain", axis="y")
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.ylim(0,250000)

    fig.add_subplot(1,2,2)
    sns.boxplot(x=df_box["month"], y=df_box["value"], palette='Set2', order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.ticklabel_format(style="plain", axis="y")
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    plt.tick_params(axis='x', labelrotation = 45)
    plt.ylim(0,250000)
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
