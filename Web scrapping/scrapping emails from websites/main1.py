import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
 

CONNECTION_ERROR = "Connectin Error"
# read url from input
 
# to save urls to be scraped
#unscraped = deque([original_url])
# to save scraped urls
#scraped = set()


result_Emails = []
# to save fetched emails
 
#while len(unscraped) > 0:
#    url = unscraped.popleft()
def findEmails(url):
    #scraped.add(url)
    parts = urlsplit(url)

    if '/' in parts.path:
        path = url[:url.rfind('/')+1]
    else:
        path = url
    print("Crawling URL %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        return CONNECTION_ERROR
    
    soup = BeautifulSoup(response.text, 'lxml')
    new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text, re.I)
    return new_emails
    

def appendEmails(emailArray):
    while len(emailArray):
        result_Emails.append(emailArray.pop())


def main(original_url):
    #scraped.add(original_url)
    parts = urlsplit(original_url)

    base_url = "{0.scheme}://{0.netloc}".format(parts)
    if '/' in parts.path:
        path = original_url[:original_url.rfind('/')+1]
    else:
        path = original_url
    print("Crawling URL %s" % original_url)
    try:
        response = requests.get(original_url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        pass
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        original_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text, re.I)

        appendEmails(original_emails)
        print(original_emails)
        #scraped.update(original_emails)
    except:
        pass

def saveEmails():    
    print(result_Emails)
    df = pd.DataFrame(result_Emails, columns=["Email"])
    df.to_csv('email.csv', index=False)


# get data from excel
def getDatafromExcel(path):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.worksheets[0]
    for i, row in enumerate(sheet):
        if i == 0:
            continue
        url = row[2].value
        print(url)
        main(url)

    saveEmails()


if __name__ == "__main__":
    excelPath = input("Enter the Excel File Path: ") 
    getDatafromExcel(excelPath)