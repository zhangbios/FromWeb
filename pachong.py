"""
    作者： KsBIOS
    日期：2018.1.3
    功能：网络爬虫
    版本：1.0
"""
import requests
from bs4 import BeautifulSoup


def get_global_city():
    """
        获取全国城市
    """
    url = 'http://pm25.in'
    city_list = []
    req = requests.get(url, timeout = 30)
    soup = BeautifulSoup(req.text, 'lxml')

    all_city_name = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = all_city_name.find_all('a')
    for cache_name in city_link_list:
        cityname = cache_name.text
        city_link = cache_name['href'][1:]
        city_list.append((cityname,city_link))
    return city_list


def get_city_AQI(cityname):
    """
        获取城市aqi
    """
    city_url = 'http://pm25.in/' + cityname
    req = requests.get(city_url, timeout = 30)
    # print(req.status_code)
    soup = BeautifulSoup(req.text,'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})
    # print(div_list)
    cityAQI = []
    for i in range(8):
        caption = div_list[i].find('div', {'class': 'caption'}).text.strip()
        # print(caption)
        value = div_list[i].find('div', {'class': 'value'}).text.strip()
        # print(value)
        cityAQI.append((caption,value))
    # print(cityAQI)
    return cityAQI


def main():
    """
        主函数
    """
    city_list = get_global_city()
    # print(city_list)
    for city in city_list:
        city_name = city[0]
        city_pinyin = city[1]
        city_aqi = get_city_AQI(city_pinyin)
        print(city_name, city_aqi)


if __name__ == "__main__":
    main()