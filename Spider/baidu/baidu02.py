"""
@Desc: 获取百度贴吧内容
@Auth: coco-hkk
@Date: 2023-05-25 09:55:59
@pyver: 3.11.3
"""

import time
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup, Comment
from lxml import html


def get_html(base_url):
    """ 获取网页内容 """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/113.0.0.0 Safari/537.36'
        }
        request = urllib.request.Request(base_url, headers=headers)
        response = urllib.request.urlopen(request).read().decode('utf-8')
        return response
    except:
        return "ERROR"


def get_content(base_url):
    """ 分析贴吧的网页文件，整理信息，保存在列表变量中 """
    # 帖子列表
    comments = []
    html_0 = get_html(base_url)
    html_ = html.fromstring(html_0).xpath('//comment()')[-3].text.strip()
    soup = BeautifulSoup(html_, 'lxml')
    div_list = soup.find_all('div', attrs={'class': 't_con cleafix'})

    # 循环遍历帖子
    for li in div_list:
        comment = {}
        try:
            comment['title'] = li.find('a', attrs={'class': 'j_th_tit'}).text.strip()
            comment['link'] = "http://tieba.baidu.com" + li.find('a', attrs={'class': 'j_th_tit'})['href']
            comment['name'] = li.find('span', attrs={'class': 'tb_icon_author'}).text.strip()
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题')

    return comments


def main(base_url, begin, end):
    """ 获取贴吧评论内容 """
    url_list = []
    for i in range(begin - 1, end):
        url_list.append(base_url + '&pn=' + str(50 * i))

    for _ in url_list:
        content = get_content(_)
        for comment in content:
            print('标题： {}\n'
                  '链接： {}\n'
                  '发帖人： {}\n'
                  '发帖时间： {}\n'
                  '回复数量： {}\n'.format(comment['title'], comment['link'], comment['name'], comment['time'],
                                          comment['replyNum']))

    print("信息采集结束...")


if __name__ == '__main__':
    kw = input('贴吧名：')
    begin_index = int(input('起始页：'))
    end_index = int(input('结束页：'))
    url = f"https://tieba.baidu.com/f?kw={urllib.parse.quote(kw)}&ie=utf-8"
    main(url, begin_index, end_index)
