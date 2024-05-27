"""
@Desc: 恋听网 https://m.ting55.com/
@Auth: coco-hkk
@Date: 2024-05-22 14:22:09
@pyver: 3.12.2
"""

import requests
import json
import time
import urllib.parse
from pathlib import Path
from urllib.parse import quote
from bs4 import BeautifulSoup


# 谢涛听世界之战国-10345
AUDIO_ID = "10345"
AUDIO_DIR = "E:/workspace/test/audio"
AUDIO_NAME = "战国.txt"


def get_url_list(server):
    """获取所有音频页面 url

    :param server: 音频目录主页
    """
    page_urls = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    }
    html_content = requests.get(url=server, headers=headers).content.decode("utf-8")
    soup = BeautifulSoup(html_content, "html.parser")
    toc = soup.css.select("a.f")
    for _ in toc:
        audio_url = f"{server}-{_.string}"
        page_urls.append(audio_url)
    return page_urls


def get_audio_url_list(page_urls, audio_index, start):
    """获取所有音频 url

    :param page_urls: 音频页面 url
    :param audio_index: 音频索引
    """
    xhr = "https://m.ting55.com/glink"

    for page_url in page_urls[(start - 1) :]:
        # 获取参数
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        }
        html = requests.get(url=page_url, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")
        xt = soup.css.select_one("head meta[name='_c']").attrs["content"]
        book_id = soup.css.select_one("head meta[name='_b']").attrs["content"]
        page = soup.css.select_one("head meta[name='_cp']").attrs["content"]

        # 构造参数
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": page_url,
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Xt": xt,
            "Cookie": "JSESSIONID=7E61F99CE8D199A3CFAB94E15043AB83; __gads=ID=63ac5e16c5a6e5b5:T=1716686525:RT=1716686525:S=ALNI_MY0EIsd9IMz13JbBnxtV3bwoHgg1g; __gpi=UID=00000e2cbd5177f6:T=1716686525:RT=1716686525:S=ALNI_MYBv3iS8bc7x3reiQ5jeA-0BdTW8w; __eoi=ID=90a6cde5457641ef:T=1716686525:RT=1716686525:S=AA-AfjY5J-RKCQctzhXX4KK7kC-k",
        }

        data = f"bookId={book_id}&isPay=0&page={page}"

        time.sleep(5)

        # 获取地址
        resp = requests.post(url=xhr, headers=headers, data=data).text
        try:
            ourl = json.loads(resp)["ourl"]
            if ourl == "":
                print("重新输入 Cookie")
                break
            title = json.loads(resp)["title"]
            title = urllib.parse.unquote(title)
            with open(audio_index, "+a", encoding="utf-8") as fs:
                print(f"{page} {title} {ourl}\n")
                fs.write(f"{page} {title} {ourl}\n")
        except json.decoder.JSONDecodeError:
            with open(f"no_{audio_index}", "+a", encoding="utf-8") as fs:
                print(f"{page} 章节不存在")
                fs.write(f"{page} 章节不存在\n")
            continue

        time.sleep(5)


def download_audio(save_dir, audio_index, start):
    """下载音频

    :param save_dir: 保存目录
    :param audio_index: 音频索引文件
    """
    with open(audio_index, "r", encoding="utf-8") as fs:
        audio_list = fs.readlines()

    for audio in audio_list[(start - 1) :]:
        audio_info = audio.rstrip("\n").split(" ")
        if len(audio_info) != 3:
            continue

        index = audio_info[0]
        title = audio_info[1]
        url = audio_info[2]
        format = url.split(".")[-1]

        response = requests.get(url, stream=True)

        with open(f"{save_dir}/{index}-{title}.{format}", "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        time.sleep(1)


if __name__ == "__main__":
    input_arg = input(
        "1-1. 获取音频地址-起始地址\n"
        "2-1. 下载音频-起始地址\n"
        "请输入："
    )

    save_dir = AUDIO_DIR
    audio_index = f"{AUDIO_DIR}/{AUDIO_NAME}"
    server_url = f"https://m.ting55.com/book/{AUDIO_ID}"

    if not Path(save_dir).exists():
        Path(save_dir).mkdir(parents=True, exist_ok=True)

    choice = input_arg.split("-")[0]
    start = int(input_arg.split("-")[1])

    if choice == "1":
        print("开始获取音频 URL...")
        page_urls = get_url_list(server_url)
        get_audio_url_list(page_urls, audio_index, start)
    else:
        print("开始下载音频...")
        download_audio(save_dir, audio_index, start)

    print("已完成")
