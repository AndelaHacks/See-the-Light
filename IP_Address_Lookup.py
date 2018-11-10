import socket
import requests


# Remove the below line when finally intergrated with main app
link = "https://www.du30newsblog.blogspot.com"

# Split the link and get element 2
get_url = (link.split('/'))[2]

# print(get_url)

# choose from below 3 methods the one that is optimal

# method 1
# answers = dns.resolver.query(get_url)
# for IP_Addresses in answers:
#     print(IP_Addresses)

# method 2
IP_addr = socket.gethostbyname(get_url)
# print(IP_addr)
Token_Charles = '52a90970-cfa0-4536-91e5-f7148bb25c61'
Token_Simon = '6ca9c9de-3b1e-4300-b85b-6501bf44717a'

headers = {
    "Accept": "application/json",
    "X-Auth-Token": Token_Simon,
}
# print (headers)
fullip = requests.get('https://api.apility.net/v2.0/' +
                      IP_addr, headers=headers)
print(fullip)

# This is a mork response since our creds have expired

    fulldict = {"geo": {...},
                "hostname": "abts-tn-static-035.5.165.122.airtelbroadband.in",
                "baddomain": {
                "domain": {
                    "blacklist": [],
                    "blacklist_mx": [],
                    "blacklist_ns": [],
                    "mx": [],
                    "ns": [],
                    "score": 0
                },
                    "ip": {
                        "address": "",
                        "blacklist": "",
                        "is_quarantined": false,
                        "score": 0
                },
                    "source_ip": {
                        "address": "71.152.251.222",
                        "blacklist": [],
                        "is_quarantined": false,
                        "score": 0
                },
                    "score": 0
    },
        "badip": {
        "score": 0,
        "blacklists": []
    },
        "history": {
        "score": -1,
        "activity": [
            {
                "ip": "122.165.5.35",
                "timestamp": 1537000113218,
                "command": "rem",
                "blacklists": "",
                "blacklist_change": "UCEPROTECT-LEVEL1"
            },
            ...
        ],
                    "score_1day": false,
                    "score_7days": false,
                    "score_30days": true,
                    "score_90days": true,
                    "score_180days": true,
                    "score_1year": true
    },
        "score": -1,
        "whois": {...}
    }

