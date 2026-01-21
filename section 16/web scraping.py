import threading #helps to do multiple task concurrently
import requests #sends http request
from bs4 import BeautifulSoup  #parse html so we can extract data

urls = [
    'https://docs.langchain.com/oss/python/langchain/overview',
    'https://docs.langchain.com/oss/python/langchain/models',
    'https://docs.langchain.com/oss/python/langchain/tools'
]

def fetch_content(url):
    response = requests.get(url) #this sends the request to server to get 
    soup = BeautifulSoup(response.content, 'html.parser') #response.content is raw html data bytes
    print(f"total no of text {len(soup.text)} characters from {url}") #soup.text Extracts all visible text from the HTML

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages fetched")


output:
PS C:\Users\asus\Documents\python\multithreading> python webscrap.py
total no of text 3700 characters from https://docs.langchain.com/oss/python/langchain/overview       
total no of text 43083 characters from https://docs.langchain.com/oss/python/langchain/models        
total no of text 11802 characters from https://docs.langchain.com/oss/python/langchain/tools
all web pages fetched
