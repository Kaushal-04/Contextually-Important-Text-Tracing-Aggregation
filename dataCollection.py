import requests
from bs4 import BeautifulSoup

def dataCollect():
    '''
    url = 'https://en.wikipedia.org/wiki/News'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')  
    texts = [paragraph.text for paragraph in paragraphs]
    '''
    texts = """
    Apple Inc. is looking at buying U.K. startup for $1 billion. 
    The deal would mark the company's first acquisition in Europe. 
    Tim Cook, CEO of Apple, stated that this acquisition is part of the company's strategy to expand its presence in the region.
    """
    return texts