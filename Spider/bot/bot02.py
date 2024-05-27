"""
@Desc: 网易新闻页面链接采集
       http://news.163.com/
       beautiful soup4
@Auth: coco-hkk
@Date: 2023-05-23 09:42:57
@pyver: 3.11.3
"""

import re
import time
import urllib.request

from bs4 import BeautifulSoup


def scan_url(url):
    """ 网易新闻 """
    html = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, "lxml")

    link_list = soup.find_all("a", href=True)

    page_urls = []
    for link in link_list:
        url = link.get("href")
        if not url.startswith("http"):
            continue
        page_urls.append(link.get('href'))

    print(page_urls)


if __name__ == '__main__':
    base_url = "http://news.163.com/"
    scan_url(base_url)
