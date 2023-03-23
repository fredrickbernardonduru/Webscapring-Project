import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage to scrape
url = 'https://jiji.co.ke/'

# Make a GET request to the webpage
response = requests.get(url)

# Use BeautifulSoup to parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a')

# Create an empty list to store the names and contacts
name_and_contact_list = []



# Loop through the links and extract the name and contact information
for link in links:
    try:
        if 'item-info' in link['class']:
            # Extract the name and contact information from the link
            name = link.find('h3').text.strip()
            contact = link.find('div', {'class': 'item__line-bottom'}).find_all('span')[1].text.strip()
            
            # Add the name and contact information to the list
            name_and_contact_list.append((name, contact))
            
            # Break out of the loop if we have collected 50K names and contacts
            if len(name_and_contact_list) >= 50000:
                break
    except:
        pass


# Print the list of names and contacts
print(name_and_contact_list)
