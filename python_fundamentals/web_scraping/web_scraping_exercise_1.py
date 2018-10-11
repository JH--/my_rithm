from urllib import request
from re import search
import bs4

# Part 1 - Web Scraping
# Write a Python program that uses BeautifulSoup to go to https://news.google.com
# and prints out all of the headlines on the page. Then, write a function called
# find_headline_by_keyword which lets you search through those headlines for
# keywords, and returns to you a list of all of the headlines that match all the
# keywords you provide.


def keyword_search(keywords, headline):
    for keyword in keywords:
        if not search(keyword.lower(), headline.lower()):
            return
    return True


def find_headline_by_keyword(headlines):
    keywords = input("Headline Search - Enter keywords: ").strip().split()
    return [h for h in headlines if keyword_search(keywords, h)]


if __name__ == "__main__":
    url = "https://news.google.com"
    data = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data, "html.parser")
    headlines = [h.span.text for h in soup.select("h3") + soup.select("h4")]

    for line in headlines:
        print(f"{line}\n")

    print("\n\n".join(find_headline_by_keyword(headlines)))


#url = "https://news.google.com"
#data = request.urlopen(url).read()
#soup = bs4.BeautifulSoup(data, "html.parser")
#
#headlines = [h.span.text for h in soup.select("h3") + soup.select("h4")]
#
# for line in headlines:
#    print(f"{line}\n")
#
#
# def keyword_search(keywords, headline):
#    for keyword in keywords:
#        if not search(keyword.lower(), headline.lower()):
#            return
#    return True
#
#
# def find_headline_by_keyword(headlines):
#    keywords = input("Headline Search - Enter keywords: ").strip().split()
#    return [h for h in headlines if keyword_search(keywords, h)]
#
#
# print("\n\n".join(find_headline_by_keyword(headlines)))
