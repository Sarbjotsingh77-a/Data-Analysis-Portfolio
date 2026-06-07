import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(data, title, filename):

    plt.figure(figsize=(10,6))
    data.plot(kind="bar")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def pie_chart(data, title, filename):

    plt.figure(figsize=(8,8))
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.title(title)
    plt.ylabel("")
    plt.savefig(filename)
    plt.close()

def heatmap(df, filename):

    plt.figure(figsize=(10,6))
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm"
    )
    plt.savefig(filename)
    plt.close()

def histogram(df, column, filename):

    plt.figure(figsize=(10,6))
    sns.histplot(df[column], kde=True)
    plt.savefig(filename)
    plt.close()
