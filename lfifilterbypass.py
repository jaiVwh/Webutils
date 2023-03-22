import requests
import sys
import urllib3

urllib3.disable_warnings()

url = sys.argv[1]
wordlist = sys.argv[3]
param = sys.argv[4].split(",")[0]

w = open(wordlist, "r")
words = w.readlines()


def main():
    count = 0
    max = len(words)
    print(f"Tested {count}/{max}", end="\r")
    for p in words:
        params = {param : p.strip("\n")}
        #print(params)
        req = requests.get(url, params=params, verify=False)
        #print(params)

        #print(req.text)
        if "root" in req.text:
            print(f"Found bypass: {p}")
            exit()
        count += 1
        print(f"Tested {count}/{max}", end="\r")
