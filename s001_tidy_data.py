SKIP_LINES = ("Country Name", "ï»¿", "\n")
REGION_FILTER = ["Sub-Saharan Africa"]

# HEADER = "Country Name, Country Code, Region, Income Group, Special Notes, Indicator Name, Indicator Code," \
# HEADER = "country_code,income_group," \
HEADER = "country_code," \
         "1960,1961,1962,1963,1964,1965,1966,1967,1968,1969," \
         "1970,1971,1972,1973,1974,1975,1976,1977,1978,1979," \
         "1980,1981,1982,1983,1984,1985,1986,1987,1988,1989," \
         "1990,1991,1992,1993,1994,1995,1996,1997,1998,1999," \
         "2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010," \
         "2011,2012,2013,2014,\n"


def parse_meta(metadata):
    """
    Parse the country metadata file to return a dictionary containing:
    {(country_code, country_name): region, income_group, special_notes}
    for ONLY the regions in the region_filter
    :param metadata: filepath to CSV containing metadata country data
    :return meta_dict: {(country_code, country_name): region, income_group, special_notes} key allows lookup in gdp file
    """
    meta_dict = {}

    with open(metadata, "r") as in_file:
        for line in in_file:
            # skip any non-data lines
            if not line.startswith(SKIP_LINES):
                # metadata is in format: "Country Name","Country Code","Region","IncomeGroup","SpecialNotes",
                split_line = line.split(",")
                try:
                    country_name = split_line[0].strip(' ""')
                    country_code = split_line[1].strip(' ""')
                    region = split_line[2].strip(' ""')
                    income_group = split_line[3].strip(' ""')
                    special_notes = split_line[4].strip(' ""')

                    if region in REGION_FILTER:
                        comp_key = (country_code, country_name)

                        if comp_key not in meta_dict:
                            # meta_dict[comp_key] = ["%s,%s,%s" % (region, income_group, special_notes)]
                            # meta_dict[comp_key] = ["%s,%s" % (region, income_group)]
                            meta_dict[comp_key] = ["'%s'" % income_group]
                        else:
                            print("ERROR: key exists for line: " + line)

                except IndexError:
                    print("ERROR: can't parse line: " + line)

    return meta_dict


def parse_gdp(gdp, tidy, meta_dict):
    """
    Given the name of an input file, output file and the dictionary returned by the parse_metadata function,
    use keys in the dictionary to get only the information for those countries from the input file, and
    write the complete information from both the dictionary and the input file to the output file in the format:
    {('country_code", "country_name"): ["region",
                                        "income_group",
                                        "special_notes",
                                        "indicator_name",
                                        "indicator_code",
                                        "1960": "", ... "2014": "XXXX.XXXX"]}
    Note that data in the input file is in the following format:
        "Country Name","Country Code","Indicator Name","Indicator Code","1960",[...]"2014",
    :param gdp:
    :param tidy:
    :param meta_dict:
    :return None:
    """
    with open(gdp, 'r') as in_file, open(tidy, 'w+') as out_file:
        # write the header to output file only once
        out_file.write(HEADER)
        for line in in_file:
            # skip any non-data lines
            if not line.startswith(SKIP_LINES):
                try:
                    split_line = line.split(",")
                    country_name = split_line[0].strip(' ""')
                    country_code = split_line[1].strip(' ""')
                    indicator_name = split_line[2].strip(' ""')
                    indicator_code = split_line[3].strip(' ""')
                    gdp_by_year = split_line[4:]

                    # this key should have a counterpart in the meta_dict if it's a country in Sub-Saharan Africa
                    comp_key = (country_code, country_name)
                    if comp_key in meta_dict:
                        # create the line to write to the tidy CSV
                        # out_line = "%s,%s,%s,%s,%s,%s" % (country_name,
                        #                                   country_code,
                        #                                   meta_dict[comp_key][0],
                        #                                   indicator_name,
                        #                                   indicator_code,
                        #                                   ''.join(gdp.strip(' ""\n') + "," for gdp in gdp_by_year))

                        # out_line = "%s,%s,%s" % (country_code,  meta_dict[comp_key][0], ''.join(gdp.strip(' ""\n') + "," for gdp in gdp_by_year))

                        out_line = "%s,%s" % (country_code, ''.join(gdp.strip(' ""\n') + "," for gdp in gdp_by_year))
                        out_file.write(out_line + "\n")

                except IndexError:
                    print("ERROR: can't parse line: " + line)


if __name__ == "__main__":
    metadata_file = "./data_files/Metadata_Country.csv"
    gdp_file = "./data_files/GDP.csv"
    tidy_file = "./data_files/tidy_gdp.csv"

    # import pprint
    # pp = pprint.PrettyPrinter(indent=4, width=300, compact=True)
    # pp.pprint(parse_meta(metadata_file))
    meta = parse_meta(metadata_file)
    parse_gdp(gdp_file, tidy_file, meta)
