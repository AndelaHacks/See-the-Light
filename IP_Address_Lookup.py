import socket
import dns.resolver

# Remove the below line when finally intergrated with main app
link = 'https://nation.co.ke/bla/bla/some-other-link.html'

# Split the link and get element 2
get_url = (link.split('/'))[2]

# print(get_url)

# choose from below 3 methods the one that is optimal

# method 1
answers = dns.resolver.query(get_url)
for IP_Addresses in answers:
    print(IP_Addresses)

# method 2
addr = socket.gethostbyname(get_url)
print(addr)

# method 3


def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain:
    :return:
    """
    ids = [
        'A',
        'NS',
        'CNAME',
        'SOA',
        'MX',
        'TXT',
    ]

    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                print(a, ':', rdata.to_text())

        except Exception as e:
            print(e)  # or pass


if __name__ == '__main__':
    get_records(get_url)
