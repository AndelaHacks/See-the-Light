from newspaper import Article
# replace with dynamic value once the code is has been integrated on the view.py as its own route
url = 'https://nation.co.ke/bla/bla/some-other-link.html'


# we are going to anaylse a news article URL, scrape the domain name and IP address
# Return Sensational score for the heading
# return reputation score from the domain name/IP address using Alexa
# return keyword analytics from the body text

article = Article(url, language="en")

article.download()
article.parse()
article.nlp()
