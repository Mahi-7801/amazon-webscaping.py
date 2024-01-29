from bs4 import BeautifulSoup
import csv

# Read index.html file
with open('filpkat2.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all div elements with class="_1AtVbE col-12-12"
divs = soup.find_all('div', class_='_1AtVbE col-12-12')

# Open data.csv in write mode
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer
    csvwriter = csv.writer(csvfile)

    # Write header to CSV file
    csvwriter.writerow(['link', 'title', 'ratings', 'reviews', 'prices'])

    # Iterate through each div element
    for div in divs:
        # Try to find img with loading="eager" and get img.src
        img = div.find('img', {'loading': 'eager'})
        link = img['src'] if img else ''

        # Try to find div with class="_4rR01T" and get div.text as title
        title_div = div.find('div', class_='_4rR01T')
        title = title_div.text.strip() if title_div else ''

        # Try to find div with class="_3LWZlK" and get div.text as ratings
        ratings_div = div.find('div', class_='_3LWZlK')
        ratings = ratings_div.text.strip() if ratings_div else ''

        # Try to find div with class="fMghEO" and get div.text as reviews
        reviews_div = div.find('div', class_='fMghEO')
        reviews = reviews_div.text.strip() if reviews_div else ''

        # Try to find div with class="_30jeq3 _1_WHN1" and get div.text as prices
        prices_div = div.find('div', class_='_30jeq3 _1_WHN1')
        prices = prices_div.text.strip() if prices_div else ''

        # Write the data to CSV file
        csvwriter.writerow([link, title, ratings, reviews, prices])

print("Data has been written to data.csv.")
