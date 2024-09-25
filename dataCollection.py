import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/News'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
paragraphs = soup.find_all('p')  
texts = [paragraph.text for paragraph in paragraphs]
print(texts)
