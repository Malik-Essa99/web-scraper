from  bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    all_anchors = soup.find_all('a',href="/wiki/Wikipedia:Citation_needed")
    citations_needed = []
    for anchor in all_anchors:
        citations_needed.append(anchor.find('span',text="citation needed").text.strip())
    return(len(citations_needed))


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all_paragraphs =[]
    report = ''
    all_anchors = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")

    for anchor in all_anchors:
        all_paragraphs.append(anchor.parent.parent.parent.text.strip())
    for paragraph in all_paragraphs:
        report += paragraph +"\n" +"\n"
    return report

if __name__=="__main__":

    with open("article.txt","w") as file:
        file.write(str(get_citations_needed_report(URL))+"\n")
        file.write("The unmber of citations needed is: " + str(get_citations_needed_count(URL)))
        
    print(get_citations_needed_report(URL))
    print("the number of citations needed is:", get_citations_needed_count(URL))