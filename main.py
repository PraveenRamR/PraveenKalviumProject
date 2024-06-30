import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://results.eci.gov.in/PcResultGenJune2024/candidateswise-S227.htm"

# Fetch the page content
response = requests.get(url)
page_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

print(soup.prettify())

# Initialize lists to store the scraped data
names = []
parties = []
statuses = []
votes = []

cand_boxes = soup.find_all('div', class_='cand-box')

for box in cand_boxes:
    name = box.find('h5').text.strip()
    party = box.find('h6').text.strip()
    status = box.find('div', class_='status').find('div').text.strip()
    vote = box.find('div', class_='status').find_all('div')[1].text.split()[0].strip()
    
    names.append(name)
    parties.append(party)
    statuses.append(status)
    votes.append(vote)

# Create a DataFrame
data = {
    'Name': names,
    'Party': parties,
    'Status': statuses,
    'Votes': votes
}

df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
csv_path = "Lok_Sabha_Election_Results_2024.csv"
df.to_csv(csv_path, index=False )

df.head()