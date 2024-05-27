"""
@Desc: 房天下新房信息
@Auth: coco-hkk
@Date: 2023-05-27 22:31:50
@pyver: 3.11.3
"""

import re

import numpy as np
import requests
from bs4 import BeautifulSoup


def get_house_info(url):
    """ 获取房子信息 """
    # 指定城市新房房价第一页信息
    html_content = requests.get(url).content.decode('utf-8')

    soup = BeautifulSoup(html_content, 'lxml')

    # 计算网页页数
    element_last_page = soup.select('.last')
    page_number = int(element_last_page[0].get('href').split('/')[3].split('9')[1])

    # 构造网页网址 demo
    url_demo = url + '/b9{}/'

    # 房价列表
    house_price_list = []
    for i in range(1, (page_number + 1)):
        new_url = url_demo.format(i)
        sub_html_content = requests.get(new_url).content.decode('utf-8')
        soup = BeautifulSoup(sub_html_content, 'lxml')

        name_list = soup.select('.nlcd_name a')
        address_list = soup.select('.address a')

        type_list = soup.findAll(name="span", attrs={"class": re.compile(r"forSale|inSale|outSale|zusale|zushou")})  # 出售
        price_list = soup.findAll(name="div", attrs={"class": re.compile(r"nhouse_price|kanesf")})  # 价格

        for index, name in enumerate(name_list):
            num = index + 1
            house_name = name.text.strip()
            house_address = address_list[index].get('title')
            house_status = type_list[index].text.strip()
            house_price_with_unit = price_list[index].text.replace('\n', '')
            house_price = re.findall(r'\d+', house_price_with_unit)
            house_price_list.append(house_price)

            print(f"编号 {num}\n"
                  f"name: {house_name}\n"
                  f"address: {house_address}\n"
                  f"status: {house_status}\n"
                  f"house_price: {house_price_with_unit}\n")

        break

    house_price_list = [int(i[0]) for i in house_price_list if i]

    print('*' * 80)
    print('* ' + ' 房价均价: ' + str(np.mean(house_price_list)))
    print('* ' + ' 房价最高价: ' + str(np.max(house_price_list)))
    print('* ' + ' 房价最低价: ' + str(np.min(house_price_list)))
    print('*' * 80)


if __name__ == '__main__':
    city_name = input("城市名（拼音）：")
    base_url = f'http://{city_name}.newhouse.fang.com/house/s'

    get_house_info(base_url)
