"""
@Desc: www.baidu.com
@Auth: coco-hkk
@Date: 2023-05-22 15:32:09
@pyver: 3.11.3
"""

import urllib.request


def baidu_spider(word: str):
    """ 百度搜索，
        使用 requests 会返回 百度安全验证，可能 requests 容易识别
    """
    url = f'https://www.baidu.com/s?wd={word}'
    headers = {
        'Referer': 'https://www.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36'
    }

    request_struct = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request_struct).read().decode('utf-8')

    print(response)


if __name__ == '__main__':
    baidu_spider('github')
