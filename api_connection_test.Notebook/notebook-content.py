# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Prerequisite

%pip install requests

# For Fabric notebook
%pip install yfinance pandas



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#resources
import requests
import pandas as pd





# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=ERW.BK,MINT.BK,CENTEL.BK,DUSIT.BK,^SET.BK"



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

url = "https://api.worldbank.org/v2/country/THA/indicator/SP.POP.TOTL?format=json"

response1 = requests.get(url)

indicator_pop = response1.json()

indicator_pop

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Access JSON DATA COMPLICATE

url = "https://api.worldbank.org/v2/country?format=json&per_page=500"

response = requests.get(url)

main_data = response.json()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

countries_pop = indicator_data[1]

rows = []

for c in countries_pop:
    rows.append({
        "country_code": c["countryiso3code"],
        "date": c["date"],
        "value": c["value"]
    })

df_pop = pd.DataFrame(rows)

spark_df_pop = spark.createDataFrame(df_pop)

spark_df_pop.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

countries = main_data[1]

rows = []

for c in countries:
    rows.append({
        "country_code": c["id"],
        "country_name": c["name"],
        "region": c["id"],
        "income_level": c["incomeLevel"]["value"],
        "capital_city": c["capitalCity"]
    })

df = pd.DataFrame(rows)
df.head()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark_df = spark.createDataFrame(df)

spark_df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
