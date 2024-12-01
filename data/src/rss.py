from datetime import datetime

from lxml import etree, html
import requests


class RssParser:
    ENDPOINTS = [
        "https://www.public.fr/feed",
        "https://vsd.fr/actu-people/feed/",
    ]
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
    }

    @classmethod
    def get_articles(cls, feed: str) -> list:
        response = requests.get(feed, headers=cls.HEADERS)
        root = etree.fromstring(response.content, base_url=feed)
        data = []
        for e in root.xpath("channel/item"):
            data.append({
                "source": feed,
                "title": str(e.xpath("title/text()")[0]).strip(),
                "description": str(e.xpath("description/text()")[0]).strip(),
                "article": html.fromstring(e.xpath('content:encoded/text()', namespaces={'content': 'http://purl.org/rss/1.0/modules/content/'})[0]).text_content(),
                "url": str(e.xpath("link/text()")[0]),
                "creator": str(e.xpath("dc:creator/text()", namespaces={'dc': 'http://purl.org/dc/elements/1.1/'})[0]),
                "published_at": datetime.strptime(e.xpath("pubDate/text()")[0], "%a, %d %b %Y %H:%M:%S %z"),
            })
        return data

    @classmethod
    def get_all(cls) -> list:
        result = []
        for endpoint in cls.ENDPOINTS:
            result += cls.get_articles(endpoint)
        return result
