from newspaper import Article, Config
from summa import summarizer
config = Config()
config.keep_article_html = True
def extract(url):
    article = Article(url=url, config=config)
    article.download()
    article.parse()
    article.nlp()

    return dict(
        title=article.title,
        description=article.text,
        html_content=article.html,
        image=article.top_image,
        authors=article.authors,
        tags=article.keywords,
        publish_date=article.publish_date,
        summary=summarizer.summarize(article.text),

    )