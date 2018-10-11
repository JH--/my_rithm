from urllib import request
from collections import defaultdict
import csv
import bs4


# Part 2 - Web Scraping + File IO
#
# This Wikipedia page has a table with data on all of the US Presidential
# elections. Our goal is to use Beautiful Soup to scrape some of this data
# into a CSV file. The columns of the CSV should be: order, year, winner,
# winner electoral votes, runner-up, and runner-up electoral votes. Use commas
# as the delimiter. For instance, after the header row, the first row of data
# should look like this:
#
# 1st,1788,George Washington,69,John Adams,34
#


def add_suffix(number):
    number = str(number)
    if len(number) == 2 and number[-2:] == '11':
        return number + 'th'
    elif len(number) == 2 and number[-2:] == '12':
        return number + 'th'
    elif len(number) == 2 and number[-2:] == '13':
        return number + 'th'
    elif number[-1] == '1':
        return number + 'st'
    elif number[-1] == '2':
        return number + 'nd'
    elif number[-1] == '3':
        return number + 'rd'
    else:
        return number + 'th'


def extract_info(row):
    if '(' in row and ')' in row and row.index(')') - row.index('(') == 2:
        del row[row.index('('): row.index(')') + 1]
    row = list(filter(lambda r: r[0] != '[' and r[0] != '(', row))
    votes = int(row[-1].split(' / ')[0])
    if row[0].isdigit():
        row = row[1:]
    if len(row) == 2:
        name = row[0]
    elif '/' in row:
        name = row[3]
    else:
        name = row[1]
    return name, votes


def get_data(rows):
    year = ''
    elections = defaultdict(list)
    for row in rows:
        if row[0].isdigit():
            year = row[0]
        elections[year].append(extract_info(row))
    return elections


def make_csv(elections):
    with open("US_presidential_elections.csv", "w") as csvfile:
        columns = 'Order, Year, Winner, Winner Electoral Votes, Runner-up, Runner-up Electoral Votes'.split(
            ', ')
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(columns)
        order = 1
        for year in elections:
            one, two = sorted(
                elections[year], key=lambda c: c[1], reverse=True)[:2]
            one_name, one_votes = one
            two_name, two_votes = two
            writer.writerow([add_suffix(order), year, one_name,
                             one_votes, two_name, two_votes])
            order += 1
    print("US_presidential_elections.csv has been created")


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/United_States_presidential_election"
    data = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data, "html.parser")
    table = soup.find("table", class_="wikitable sortable")
    rows = list(map(lambda row: list(row.stripped_strings), table('tr')))[1:]
    elections = get_data(rows)
    make_csv(elections)
