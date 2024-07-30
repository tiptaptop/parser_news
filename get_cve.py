from datetime import datetime
import feedparser 


news_feed = feedparser.parse('https://www.cert.ssi.gouv.fr/avis/feed')    
today = datetime.utcnow().date()


for entry in news_feed.entries:
    if datetime(*entry.published_parsed[:6]).date() == today:
        print(entry.title)
        print(entry.link)
