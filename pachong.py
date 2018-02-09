"""
    作者：KsBios
    功能：
    版本：
    日期：
"""
import requests
from bs4 import BeautifulSoup


def get_aqi_text_method(city_name):
    """
        获取城市AQI
    """
    url_path = 'http://pm25.in/' + city_name
    r = requests.get(url_path, timeout = 30)
    # print(r.status_code)
    # return r.text
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})
    # return div_list

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption,value))
    return city_aqi


def main():
    """
        主函数
    """
    city_name = input("please input city:")
    aqi_text = get_aqi_text_method(city_name)
    print(aqi_text)


if __name__ == "__main__":
    main()