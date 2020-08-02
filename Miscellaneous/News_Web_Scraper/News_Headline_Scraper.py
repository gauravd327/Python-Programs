from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("https://www.bbc.com/news")
soup = BeautifulSoup(page.content, "lxml")
headline_list, link_list = [], []
with open("Headlines.csv", "w") as bbc_headlines:
    writer = csv.writer(bbc_headlines)
    writer.writerow(["Headline", "Link"])
    for x in soup.find_all("a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"):
        link = x.get("href")
        if str(link).startswith("/"):
            link = "https://www.bbc.com" + link

        writer.writerow([x.text, link])