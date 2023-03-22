from sys import argv
import os
HelpMassage = """webutils URL | MODE | [WORDLIST] | [PARAMETERS] | [COOKIES] | [USERNAME] | [EXTRA] 
MODES:
0: crawl the website and display all sites found
1: Subdomain brute force needs a wordlist as third argument
2: lfi filter bypass and needs a wordlist as third argument and the parameter as fourth argument
3: Bruteforce weblogins and needs wordlist as third argument, the paramteters as fourth and the username as fifth

WORDLIST:
This program got some wordlists included
For subdomains: subdomains.txt or subdomains-small.txt
For lfifilter bypass: lfibypass.txt
For login bruteforce: rockyou.txt

PARAMETERS:
These are the parameters of a get or post requests. If you use more than one argument, seperate them with a ','

Examples:
Mode 0: webutils http://abs.example.com/index.html 0
Mode 1: webutils http://example.com/index.html 1 subdomains.txt
Mode 2: webutils http://example.com/index 2 lfibypass.txt img
Mode 3: webutils http://metapress.htb/wp-login.php 2 rockyou.txt log,pwd wp-settings-time-2=1679422000,wp-settings-2=mfold%3Do%26uploader%3D1,PHPSESSID=lfu71uj85hjuqbop501njep6bq,wordpress_test_cookie=WP%20Cookie%20check manager wp-submit=Log%2BIn,redirect_to=http%253A%252F%252Fmetapress.htb%252Fwp-admin%252F,testcookie=1"""


if "-h" in argv:
    print(HelpMassage)
elif len(argv) < 3:
    print(HelpMassage)
    exit()
elif argv[2] == "0":
    import crawler
    crawler.main()
elif argv[2] == "1" and len(argv) >= 4:
    import subscan
    subscan.main()
elif argv[2] == "2" and len(argv) >= 5:
    import lfifilterbypass
    lfifilterbypass.main()
elif argv[2] == "3" and len(argv) >= 8:
    import loginbruteforce
    loginbruteforce.main()

else:
    print(HelpMassage)
    exit()

