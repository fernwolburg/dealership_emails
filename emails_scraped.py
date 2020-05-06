from bs4 import BeautifulSoup as bs 
import requests
import csv

# specify website and download into 'soup' variable
website = 'PLACE YOUR URL HERE'
source = requests.get(website).text
soup = bs(source, 'lxml')

# create a csv file to store the emails
csv_file = open('emails_scraped.csv', 'a')
csv_writer = csv.writer(csv_file)

# loop through all the emails and store them onto csv
for link in soup.find_all('a', class_='btn btn-main btn-sm email'):
    link = link.get('href')
    email = link[7:]
    print(email)
    csv_writer.writerow([email])
    
csv_file.close()