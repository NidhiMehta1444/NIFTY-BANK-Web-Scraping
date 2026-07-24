import requests
import pandas as pd
from datetime import datetime, timedelta

# -----------------------------------
# Calculate 5 years date range
# -----------------------------------

end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

from_date = start_date.strftime("%d-%m-%Y")
to_date = end_date.strftime("%d-%m-%Y")

print(from_date)
print(to_date)

# -----------------------------------
# Create Session
# -----------------------------------

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.niftyindices.com/reports/historical-data",
    "Origin": "https://www.niftyindices.com"
}

# Visit homepage first
session.get(
    "https://www.niftyindices.com/reports/historical-data",
    headers=headers
)

# -----------------------------------
# Payload
# -----------------------------------

payload = {

    "indexType": "Equity",

    "subIndexType": "Sectoral Indices",

    "indexName": "NIFTY BANK",

    "fromDate": from_date,

    "toDate": to_date

}

# -----------------------------------
# Download data
# -----------------------------------

url = "https://www.niftyindices.com/Backpage.aspx/getHistoricaldatatabletoString"

response = session.post(
    url,
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)