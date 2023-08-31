import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

CONNECTION_ERROR = "Connectin Error"

result_Emails = []
 
def findEmails(url):
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
   
    # get current website html
    soup = BeautifulSoup(response.text, 'lxml')
    
    # search those new htmls for any emails
    new_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text, re.I)
    return new_emails
    

def appendEmails(emailArray):
    while len(emailArray):
        result_Emails.append(emailArray.pop())


def main(original_url):

    # get website html
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

    # search html for any emails
    soup = BeautifulSoup(response.text, 'lxml')
    original_emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text, re.I)

    appendEmails(original_emails)

    # find all <a> tags 
    for anchor in soup.find_all("a"):
        if "href" in anchor.attrs:
            link = anchor.attrs["href"]
        else:
            link = ''
            if link.startswith('/'):
                link = base_url + link
            
            elif not link.startswith('http'):
                link = path + link
        # get request all of the hrefs of those tags and get the html
        found_Emails = findEmails(link)

        if(found_Emails == CONNECTION_ERROR):
            print(CONNECTION_ERROR)
            break
        
        appendEmails(found_Emails)

    # get all scripts in each html, get request them, and search for emails in their code
    for anchor in soup.find_all("script"):
        if "href" in anchor.attrs:
            link = anchor.attrs["src"]
        else:
            link = ''
            if link.startswith('/'):
                link = base_url + link
            
            elif not link.startswith('http'):
                link = path + link

        found_Emails = findEmails(link)

        if(found_Emails == CONNECTION_ERROR):
            print(CONNECTION_ERROR)
            break
        
        appendEmails(found_Emails)

    # output csv file
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
        main(url)


if __name__ == "__main__":
    excelPath = input("Enter the Excel File Path: ") 
    getDatafromExcel(excelPath)