from newspaper import Article, Config
from summa import summarizer
config = Config()
config.keep_article_html = True
def extract(url):
    article = Article(url=url, config=config)
    article.download()
    article.parse()
    article.nlp()

    try:
        text_rank_summary = summarizer.summarize(article.text)
    except:
        text_rank_summary = ''

    return dict(
        title=article.title,
        image=article.top_image,
        authors=article.authors,
        tags=article.keywords,
        text_rank_summary=text_rank_summary,
        summary=article.summary,
        description=article.text,
        publish_date=article.publish_date,
        meta_img=article.meta_img,
        meta_description=article.meta_description,
        meta_keywords=article.meta_keywords,

        

    )