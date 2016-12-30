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
    gdp_frame = pd.read_csv(gdp_file, index_col=0, skiprows=2)
    ctry_frame = pd.read_csv(country_file, index_col=0)

    return hcgdp_ctry


if __name__ == "__main__":
    find_highest_correlated_gdp('data_files/GDP.csv', 'Metadata_Country')
