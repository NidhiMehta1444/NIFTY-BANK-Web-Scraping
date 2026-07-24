import requests
import pandas as pd
import json
from datetime import datetime

start_date = "22-Jul-2021"
end_date = datetime.today().strftime("%d-%b-%Y")

url = "https://www.niftyindices.com/BackPage/getHistoricaldatatabletoString"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.niftyindices.com/reports/historical-data",
    "Origin": "https://www.niftyindices.com",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

payload = {
    "cinfo": (
        "{'name':'NIFTY BANK',"
        f"'startDate':'{start_date}',"
        f"'endDate':'{end_date}',"
        "'indexName':'NIFTY BANK'}"
    )
}

session = requests.Session()

session.get(
    "https://www.niftyindices.com/reports/historical-data",
    headers=headers
)

response = session.post(
    url,
    json=payload,
    headers=headers
)

# Get the response
result = response.json()
data = result
 # If this gives an error, let me know.

# Convert to DataFrame
df = pd.DataFrame(data)

# Optional: Keep only required columns
df = df[[
    "HistoricalDate",
    "INDEX_NAME",
    "OPEN",
    "HIGH",
    "LOW",
    "CLOSE"
]]

# Save to CSV
df.to_csv("NIFTY_BANK_5Y.csv", index=False)

print(df.head())
print("CSV file saved successfully!")