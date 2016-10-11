
virtualenv -p python3 diffbotapp
. ./diffbotapp/bin/activate
#https://github.com/codelucas/newspaper
#https://github.com/summanlp/textrank
#https://github.com/miso-belica/sumy

pip3 install newspaper3k
pip install https://github.com/ptmono/textrank/archive/master.zip
pip3 install networkx
pip3 install scipy
pip3 install Flask

- After fetching tags from then use this api for validate

http://lookup.dbpedia.org/api/search/KeywordSearch?QueryClass=place&QueryString=internally

- We need og_image and respective image after that

from newspaper import Article
from summa import summarizer
url = "http://patshaughnessy.net/2012/7/26/objects-classes-and-modules"
article = Article(url)
article.download()
article.parse()
text = article.text
article.top_image
article.nlp()
article.summary
summarizer.summarize(text)