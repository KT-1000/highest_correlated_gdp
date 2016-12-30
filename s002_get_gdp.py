# Identify the country in Sub-Saharan Africa
# with an annual GDP most strongly correlated
# with the largest number of other sub Saharan countries.
# In other words, for each country in sub Saharan Africa,
# find which other country has the highest correlation.
# Once you have identified this list of country pairs,
# tell us which country occurs most frequently.
import pandas as pd
from collections import Counter


def find_correlation(csv_path):
    # create DataFrame
    df = pd.read_csv(csv_path, sep=',', index_col=0)
    # transpose to get correct axes
    t_df = df.transpose()
    # find the correlation of each country's GDP to each other country's GDP
    correlation = t_df.corr()
    # store the country pairs with strong correlations
    row_corr = []
    # rows are in format: Pandas(Index='AGO', AGO=1.0, BDI=0.94752851658272008, BEN=0.96412797510248038, ....)
    for row in correlation.itertuples():
        skip_keys = ['Index', row.Index]
        # track the highest correlation for each country pair
        high_corr = -1.0
        # track the country with the highest correlation to the index country
        high_corr_ctry = ""

        for key_val in row.__dict__:

            if key_val not in skip_keys:
                country_code = key_val
                corr_val = row.__dict__[key_val]

                if float(corr_val) > high_corr:
                    high_corr = corr_val
                    high_corr_ctry = country_code

        # when finished with each correlation value in the row, append the tuple (row_index, high_corr_ctry) to row_corr
        row_corr.append((row.Index, high_corr_ctry))

    return Counter(item[1] for item in row_corr).most_common(1)[0][0]

if __name__ == "__main__":
    tidy_csv = "./data_files/tidy_gdp.csv"
    print(find_correlation(tidy_csv))
