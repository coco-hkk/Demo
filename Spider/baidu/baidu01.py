"""
@Desc: 百度贴吧图片下载
       百度安全验证绕过是个难点
@Auth: coco-hkk
@Date: 2023-05-23 09:42:57
@pyver: 3.11.3
"""

import time
import urllib
import urllib.request
from lxml import etree, html
from lxml.etree import HTMLParser


def load_page(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36'
    }

    # 中文编码错误解决
    # encoded_url = urllib.parse.quote(url, safe=':/')
    request_struct = urllib.request.Request(url=url, headers=headers)
    html_content = urllib.request.urlopen(request_struct).read().decode('utf-8')

    # 解析HTML文档为HTML DOM模型
    # content = etree.parse("file.html", etree.HTMLParser(encoding="utf-8"))
    # content = etree.HTML(html_content, etree.HTMLParser(encoding="utf-8"))
    # content = etree.HTML(html_content)
    content = html.fromstring(html_content)

    # 分析网页源码，抽取注释并解析，获取链接地址列表
    comment_code = content.xpath('//comment()')[49].text.strip()
    content = etree.HTML(comment_code)
    link_list = content.xpath('//div[@class="t_con cleafix"]/div[2]/div[1]/div[1]/a//@href')[1:]

    for link in link_list:
        thread_link = "https://tieba.baidu.com" + link
        load_image(thread_link)


# 取出每个帖子里的每个图片连接
def load_image(link):
    """ 获取图片链接 """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'Referer': 'https://tieba.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36'
    }

    request_struct = urllib.request.Request(url=link, headers=headers)
    html_content = urllib.request.urlopen(request_struct).read().decode('utf-8')
    content = etree.HTML(html_content)

    # 采集图片地址并下载
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        write_image(link)
        time.sleep(1)


def write_image(link):
    """ 将图片保存到本地
        link：图片连接
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36'
    }

    request_struct = urllib.request.Request(url=link, headers=headers)
    image = urllib.request.urlopen(request_struct).read()

    # 取出连接后10位做为文件名
    filename = link[-10:] + '.png'

    # 写入到本地磁盘文件内
    with open(filename, "wb") as f:
        f.write(image)

    print(f"已下载 {filename}")


def tieba_spider(url, begin_page, end_page):
    """ 调度器，负责组合处理每个页面的 url
        url : 贴吧 url 的前部分
        begin_page : 起始页
        end_page : 结束页
    """
    for page in range(begin_page, end_page + 1):
        pn = (page - 1) * 50
        url = url + f"&pn={pn}"

        print(url)
        load_page(url)


if __name__ == "__main__":
    kw = input("贴吧名:")
    begin_index = int(input("起始页："))
    end_index = int(input("结束页："))

    base_url = f"https://tieba.baidu.com/f?ie=utf-8&kw={urllib.parse.quote(kw)}"

    tieba_spider(base_url, begin_index, end_index)
