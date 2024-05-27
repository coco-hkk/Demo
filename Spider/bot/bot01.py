"""
@Desc: 豆瓣短评
       页面分析，获取评论及其作者
       pip install beautifulsoup4
@Auth: coco-hkk
@Date: 2023-05-22 22:28:27
@pyver: 3.11.3
"""

import requests
import time
from bs4 import BeautifulSoup


def comment_info(douban_url, start_index):
    """  获取豆瓣读书 《利用Python进行数据分析》 短评 """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36'
    }

    r = requests.get(douban_url, headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')
    comment_list = bs.find_all('li', 'comment-item')

    for index, item in enumerate(comment_list):
        comment = item.find_all('p', 'comment-content')
        author = item.find_all('span', 'comment-info')[0].find_all('a')[0].string
        print(f"{index + start_index}. {comment[0].find_all('span')[0].string} -- {author}")


if __name__ == '__main__':
    for i in range(0, 16):
        time.sleep(2)
        start = i * 20
        url = f'https://book.douban.com/subject/25779298/comments/?start={start}&limit=20&status=P&sort=score'
        comment_info(url, start)
