
import requests
import json

from doc import WorkDoc


def get_links_yandex(link: str) -> str:
    url = 'https://cloud-api.yandex.net/v1/disk/public/resources'
    links_str = ''
    params = {
        'public_key': link,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        dict_link = json.loads(response.text)
        if '_embedded' in dict_link.keys():
            for item in dict_link['_embedded']['items']:
                if links_str == '':
                    links_str += item['file']
                else:
                    links_str += f"\n{item['file']}"
        elif 'file' in dict_link.keys():
            links_str = dict_link['file']

    return links_str


def get_links_google(link: str) -> str:
    url = ''
    links_str = ''
    params = {
        'public_key': link,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        for item in response.json()['_embedded']['items']:
            if links_str == '':
                links_str += item['file']
            else:
                links_str += item['file']

    return links_str


def get_photos_links(photos_link: str) -> str:
    if 'drive.google' in photos_link:
        return get_links_google(photos_link)
    elif 'disk.yandex' in photos_link:
        return get_links_yandex(photos_link)
    else:
        return ''


def get_links_per_file(filepath: str):
    work_doc = WorkDoc()
    work_doc.open_file(filepath)
    work_doc.set_sheet(0)
    link_columns = work_doc.find_column_with_link()
    for row in range(2, work_doc.get_row_count() + 1):
    # for row in range(2, 3):
        for itemLink in link_columns:
            direct_links = get_photos_links(work_doc.read_sell_value(row, itemLink['source']))
            if direct_links != '':
                work_doc.write_links_sell(row, itemLink['destination'], direct_links)

    work_doc.save_doc()




