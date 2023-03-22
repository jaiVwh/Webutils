import requests
import sys
from urllib.parse import urljoin, urlparse
import threading

allowedRes = [200,204,302,307,401,403,405,500]
url = sys.argv[1]
wordlist = sys.argv[3]
words = open(wordlist).readlines()
toTest = len(words)
tested = 0
parsed = urlparse(url)
domain = None
nl = parsed.netloc
snl = nl.split(".")
if len(snl) == 2:
    domain = snl[0] + "." + snl[1]
elif len(snl) == 3:
    domain = snl[1] + "." + snl[2]


def TestSub(subdomain, url):
    h = {"Host" : subdomain.strip("\n") + "." + domain}
    res = requests.get(url, headers=h, allow_redirects=False)
    if res.status_code in allowedRes:
        print(h["Host"] + "                       ")



def main():
    tested = 0
    print("Tested (0/" + str(toTest) + ")", end="\r")
    for s in words:
        t = threading.Thread(target=TestSub, args=(s, url))
        t.run()
        tested += 1
        print("Tested (" + str(tested) + "/" + str(toTest) + ")", end="\r")
