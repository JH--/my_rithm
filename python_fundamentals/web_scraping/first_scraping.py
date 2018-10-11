import urllib.request as request
import bs4
import csv

url = "https://news.ycombinator.com/"
data = request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")

links = soup.select("a.storylink")

with open("articles.tsv", "w") as tsvfile:
    writer = csv.writer(tsvfile, delimiter="\t")
    writer.writerow(("Title", "Link"))
    for link in links:
        writer.writerow((link.text, link["href"]))

with open("articles.tsv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in list(reader):
        print (" ---- ".join(row))
        print (" ")




# for link in links:
#    print(f"{link['href']} {link.text}")
