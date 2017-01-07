import pandas as pd


def find_highest_correlated_gdp(gdp_file, country_file):
    """
    Given GDP.csv and Metadata_Country.csv (taken from The World Bank http://data.worldbank.org),
    identify the country in Sub-Saharan Africa with an annual GDP
    most strongly correlated with the largest number of other sub Saharan countries.
    In other words, for each country in sub Saharan Africa, find which other country has the highest correlation.
    :param gdp_file: CSV containing GDP data
    :param country_file: CSV containing country metadata
    :return hcgdp_ctry: country with highest correlated GDP
    """
    hcgdp_ctry = None

    # create data frames from each csv
    gdp_frame = pd.read_csv(gdp_file,
                            sep=",",
                            index_col=0,
                            skiprows=2,
                            skipinitialspace=True,
                            encoding="utf-8")

    for gdp_col in gdp_frame.columns:
        gdp_col.replace("\n", "").replace(" ", "").replace("\\", "")

    ctry_frame = pd.read_csv(country_file,
                             index_col=0,
                             skipinitialspace=True,
                             encoding="utf-8")
    # clean 'em up
    # combine into one data frame on country name
    # get the correlation of this combined data frame (using .corr)

    print(gdp_frame.head())

    return hcgdp_ctry


if __name__ == "__main__":
    print(find_highest_correlated_gdp('data_files/GDP.csv', 'data_files/Metadata_Country.csv'))
