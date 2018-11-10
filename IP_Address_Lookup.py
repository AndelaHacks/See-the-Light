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


headers = {
    "Accept": "application/json",
    "X-Auth-Token": "52a90970-cfa0-4536-91e5-f7148bb25c61",
}
# print (headers)
fullip = requests.get('https://api.apility.net/v2.0/' + IP_addr, headers=headers)
print(fullip)
# key_pass = 'Mwangi2018'

# GET /badip_batch/IP_addr HTTP/1.1
# Host: api.apility.net
# X-Auth-Token: 52a90970-cfa0-4536-91e5-f7148bb25c61
# Cache-Control: no-cache
# Postman-Token: 77a94897-edff-f7bc-7b48-6874d8a37340


#$ curl -H "Accept: application/json" -H "X-Auth-Token: 52a90970-cfa0-4536-91e5-f7148bb25c61" -X GET "https://api.apility.net/badip_batch/172.217.6.193"