import requests
from bs4 import BeautifulSoup
import subprocess

# Make a request to the website
url = 'https://www.reddit.com/'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the post titles
post_titles = soup.find_all('a', {'class': 'title'})

# Open a new LibreOffice Calc file
subprocess.call(['libreoffice','--calc','reddit_posts.ods'])

# Get the active sheet
sheet = x.get_active_sheet()

# Write the headers to the sheet
sheet.write(0, 0, 'Post Title')

# Write the post titles to the sheet
for i, title in enumerate(post_titles):
    sheet.write(i + 1, 0, title.text)

# Save the file
x.save('reddit_posts.ods')