import requests
from bs4 import BeautifulSoup

def main():
  try:
    response = requests.get("https://huggingface.co/papers")
    response.raise_for_status()
    soup = BeautifulSoup(response.text)
    
    articles = soup.find_all('article')
    
    print(articles)

  except requests.exceptions.RequestException as e:
    print(e)

main()