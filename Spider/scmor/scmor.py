"""
@Desc: 思谋学术
        1. pip install pyexecjs
        2. pip install lxml

        访问链接通过 js 触发，分析触发代码，获取链接 url
@Auth: coco-hkk
@Date: 2023-05-22 21:51:41
@pyver: 3.11.3
"""

import execjs
import requests
from lxml import etree
import re

with open('scmor.js', 'r', encoding='utf-8') as f:
    js = f.read()
    ctx = execjs.compile(js)


def parse_content(html):
    """ 解析 base64 编码的 URL """
    tree = etree.HTML(html)
    script_text = tree.xpath('//script/text()')[0]
    base64_url = re.findall(r'U3kwBQ[a-zA-Z0-9]+=*', script_text)
    return base64_url


def decode(string):
    """ 解码 URL """
    # base64 解码 string 参数, string 参数的值就是上面代码中的那段 base64 编码后的内容
    string = ctx.call('base64decode', string)
    key = "21b5del6oIO57e01aac.scmor.com"
    length = len(key)
    code = ''
    for i in range(0, len(string)):
        k = i % length
        n = ord(str(string[i])) ^ ord(str(key[k]))
        code += chr(n)
    return ctx.call('base64decode', code)


if __name__ == '__main__':
    html_content = requests.get("https://ac.scmor.com").text
    encoded_url_list = parse_content(html_content)
    for encoded_url in encoded_url_list:
        print(decode(encoded_url))
