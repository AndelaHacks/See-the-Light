import requests
import time
from newspaper import Article
from bs4 import BeautifulSoup

start_time = time.time()
url2 = 'https://www.wsj.com/articles/lawmakers-to-resume-stalled-border-security-talks-11549901117'
url = 'https://www.nation.co.ke/news/Waititu-mum-on-alleged-family-hand-in-Kiambu-graft-probe/1056-5129468-ntcmyb/index.html'
url3 = 'https://www.nation.co.ke/news/Wangechi-murder-suspect-held-for-14-days/1056-5072538-d2i6ntz/index.html'

a = Article(url)
a.download()
a.parse()
a.nlp()
# splitted_text = a.text.split("\n", 2)
# r = requests.get(url)
# page = r.text
# soup = BeautifulSoup(page, 'lxml')

# paras = soup.find_all('p')
# print (paras)
print('========================')
print("Keywords", a.keywords)
print("Published Date", a.publish_date)
print (a.text)
print("***** Summary of the above story ************")
print(a.summary)
print("This script took:", round(time.time() - start_time, 2), "seconds to execute")
# for i, para in enumerate(paras):
#     print ('Paragraph', i)
#     print (para)