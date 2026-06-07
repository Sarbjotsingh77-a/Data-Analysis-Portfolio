def calculate_statistics(df):

    numeric_df = df.select_dtypes(include=['number'])

    stats = {
        "Mean": numeric_df.mean(),
        "Median": numeric_df.median(),
        "Minimum": numeric_df.min(),
        "Maximum": numeric_df.max(),
        "Correlation": numeric_df.corr()
    }

    return stats
