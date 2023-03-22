import sys, requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from threading import Thread

links = set()
browsed = set()

url = sys.argv[1]
parsed = urlparse(url)
base = parsed.scheme + '://' + parsed.netloc

links.add(url)

def run_spider(url):
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        browsed.add(url)
        for a in soup.findAll("a"):
            href = urljoin(base, a.get("href"))

            if parsed.netloc in href:
                links.add(href)
                print("Found " + str(len(links)) + " links", end="\r")
        for a in soup.findAll("script"):
            href = urljoin(base, a.get("src"))

            if parsed.netloc in href:
                links.add(href)
                print("Found " + str(len(links)) + " links", end="\r")
        for a in soup.findAll("link"):
            href = urljoin(base, a.get("href"))

            if parsed.netloc in href:
                links.add(href)
                print("Found " + str(len(links)) + " links", end="\r")
        for a in soup.findAll("img"):
            href = urljoin(base, a.get("src"))

            if parsed.netloc in href:
                links.add(href)
                print("Found " + str(len(links)) + " links", end="\r")
        if "Nonce" in html or "nonce" in html:
            print(html)
            print(url)
            exit()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    except:
        pass

def main():



    while len(links) != len(browsed):
        for u in links:
            if not u in browsed:
                run_spider(u)
                break

    for l in links:
        print(l.split("?")[0])
