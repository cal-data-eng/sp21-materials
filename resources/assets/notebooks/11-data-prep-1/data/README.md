This directory includes a few odds and ends:

**Jeopardy Data**
- `jc1.txt` is a dataset of Jeopardy Contestants crawled from j-archive.com and [posted on Reddit](https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/).
- `jq2.txt` is a dataset Jeopardy Questions also crawled from j-archive.com

**California/Nevada Precipitation Data**
- `simple_scrape.py` is a Python script to crawl data from the [NOAA Website for the California-Nevada River Forecast Center](https://www.cnrfc.noaa.gov), e.g. pages like https://www.cnrfc.noaa.gov/monthly_precip_2020.php). If you run it, it will create a subdirectory called `output` and store each year's data there.
- `monthly_precip_full.csv` is the concatenation of the outputs of `simple_scrape.py`
- `flow_CalDataEngExample.zip` is a Trifacta flow export file. It contains all the recipes to take the `monthly_precip_full.csv` file and generate the remaining files: `mm.txt`, `mmp.txt`, `mmr.txt` and `mpf.txt`. This is not a human-readable format---to make use of it, you need to go to Flows->Import Flow in Trifacta [as described here](https://docs.trifacta.com/display/AWS/Import+Flow).
- `mm.txt` is a pivot table (matrix) of `Year` x `Month`.
- `mmp.txt` is a pivot table of `(Year,ID,Location,Station)` x `Month`
- `mmr.txt` is a un-pivoted (relational) version of `mpf.txt`
- `mpf.txt` is a cleaned-up version of `monthly_precip_full.csv` with all the display junk from the web stripped out and the relevant fields replicated into each row.
