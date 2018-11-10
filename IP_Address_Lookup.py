import socket
import requests

"""
https://apility.io/apidocs/#get-full-ip-address-reputation-info

From API version 2.0 a new endpoint has been added that allows to obtain a score of an IP address not only studying if it is in a black list. Also the following checks are made:

A reverse DNS lookup is performed and a hostname is obtained. The service checks if the domain is in any blacklist.
Check if the IP address was in any blacklist in the past. The service checks the historical information of the IP address.
These three checks -IP address blacklist, Domain blacklist and IP address historical blacklist- are summarized and returned as a global score for the IP address.

This API call also returns detailed information about the IP address from different sources:

IP Geolocation
AS information
WHOIS informaton
Reverse DNS lookup to obtain the Hostname
Blacklists where the IP address was found (if any).
Blacklists where the Hostname was found (if any).
IP address historical activity: what blacklists did the IP address was found in?
"""
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

# key_pass = 'Mwangi2018'

# GET /badip_batch/IP_addr HTTP/1.1
# Host: api.apility.net
# X-Auth-Token: 52a90970-cfa0-4536-91e5-f7148bb25c61
# Cache-Control: no-cache
# Postman-Token: 77a94897-edff-f7bc-7b48-6874d8a37340


#$ curl -H "Accept: application/json" -H "X-Auth-Token: 52a90970-cfa0-4536-91e5-f7148bb25c61" -X GET "https://api.apility.net/badip_batch/172.217.6.193"
