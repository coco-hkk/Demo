"""
@Desc: 17K小说网小说下载
@Auth: coco-hkk
@Date: 2023-05-27 13:33:21
@pyver: 3.11.3
"""


import requests
from urllib.parse import quote
from bs4 import BeautifulSoup


def search_novel(name: str, search: str) -> str:
    """ 搜索小说，返回链接 """
    local_url = f'{search}?c.st=0&c.q={quote(name)}'
    html_content = requests.get(url=local_url).content.decode('utf-8')

    soup = BeautifulSoup(html_content, 'lxml')
    search_list = soup.find_all('div', class_='search-list')
    textlist = search_list[0].find_all('div', class_='textlist')

    for item in textlist[1:]:
        _novel_name = item.find_all('dt')[0].get_text().strip()
        if _novel_name != name:
            continue

        href = item.find_all('li')[2].find_all('a')[0].get('href')
        _full_url = f"https:{href}"
        return _full_url


def get_chapter_url_list(server, target):
    """ 获取小说各章节的 url 链接 """
    urls = []
    html_content = requests.get(url=target).content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'lxml')
    volume = soup.find_all('dl', attrs=('class', 'Volume'))
    for _ in volume:
        soup = BeautifulSoup(str(_), 'lxml')
        links = soup.find_all('a')
        for link in links[1:]:
            urls.append(server + link.get('href'))

    return urls


def get_chapter_contents(target):
    """ 获取小说正文内容 """
    html_content = requests.get(url=target).content.decode('utf-8')
    soup = BeautifulSoup(html_content, 'lxml')

    html_chapter = soup.find_all('div', attrs={'class', 'readAreaBox content'})

    chapter_title = html_chapter[0].find_all('h1')[0].string
    html_chapter_content = html_chapter[0].find_all('div', attrs={'class', 'p'})
    chapter_content_string = html_chapter_content[0].find_all('p')

    chapter_content = ""
    for _ in chapter_content_string[:-1]:
        chapter_content += str(_.string)
        chapter_content += '\n'

    return chapter_title, chapter_content


def write_text(name, path, text):
    """ 将小说写入文件 """
    with open(path, 'a', encoding='utf-8') as stream:
        stream.write(name + '\n')
        stream.writelines(text)
        stream.write('\n')


if __name__ == '__main__':
    server_url = 'http://www.17k.com'
    search_url = 'https://search.17k.com/search.xhtml'

    print("17K 小说网")
    novel_name = input('小说名：')
    book_name = f"{novel_name}.txt"

    full_url = search_novel(novel_name, search_url)
    url_list = get_chapter_url_list(server_url, full_url)

    for url in url_list[:10]:
        title, content = get_chapter_contents(url)
        write_text(title, book_name, content)

    print("已下载完成")
