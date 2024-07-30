import os
from datetime import datetime
import feedparser 


LAST_FETCH_FILE = 'last_fetch.txt'


def read_last_fetch_datetime():
    if not os.path.exists(LAST_FETCH_FILE):
        return None
    with open(LAST_FETCH_FILE, 'r') as file:
        datetime_str = file.read().strip()
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def write_last_fetch_datetime(dt):
    with open(LAST_FETCH_FILE, 'w') as file:
        file.write(dt.strftime('%Y-%m-%d %H:%M:%S'))



news_feed = feedparser.parse('https://www.cert.ssi.gouv.fr/feed')    
last_fetch_datetime = read_last_fetch_datetime()
new_last_fetch_datetime = datetime.utcnow()

if last_fetch_datetime is None:
        last_fetch_datetime = datetime.min
#today = datetime.utcnow().date()


for entry in news_feed.entries:
    entry_published = datetime(*entry.published_parsed[:6])
    if entry_published > last_fetch_datetime:
            print(entry.title)
            print(entry.link)

write_last_fetch_datetime(new_last_fetch_datetime)


