"""
@Desc: www.kfc.com.cn
@Auth: coco-hkk
@Date: 2023-05-22 18:16:09
@pyver: 3.11.3
"""

import requests


def kfc_spider(city: str):
    """ KFC 餐厅信息查询 """
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0 Safari/537.36'
    }

    for i in range(1, 8):
        data = {
            "cname": city,
            "pid": "",
            "pageIndex": i,
            "pageSize": '10'
        }
        response = requests.post(url, headers=headers, data=data).json()

        print(f'第{i}页'.center(30, '='))
        for info in response.get('Table1'):
            print(f"{info['storeName']}餐厅 ： {info['addressDetail']}")


if __name__ == '__main__':
    kfc_spider('西安')
