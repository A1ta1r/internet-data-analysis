import requests
import re
from bs4 import BeautifulSoup as bs

url = r"https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaMIBiAEBmAExuAEXyAEU2AEB6AEB-AECiAIBqAID&lang=en-us&sid=d7625d75c19329190f2fe671a4dc3809&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaMIBiAEBmAExuAEXyAEU2AEB6AEB-AECiAIBqAID%3Bsid%3Dd7625d75c19329190f2fe671a4dc3809%3Bcheckin_month%3D12%3Bcheckin_monthday%3D27%3Bcheckin_year%3D2018%3Bcheckout_month%3D12%3Bcheckout_monthday%3D28%3Bcheckout_year%3D2018%3Bcity%3D-2980155%3Bclass_interval%3D1%3Bdest_id%3D-2980155%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3Daebb808f6f900186%3Bss%3DPerm%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DPerm%3Bssne_untouched%3DPerm%26%3B&ss=Perm&is_ski_area=0&ssne=Perm&ssne_untouched=Perm&city=-2980155&checkin_month=12&checkin_monthday=30&checkin_year=2018&checkout_month=12&checkout_monthday=31&checkout_year=2018&group_adults=4&group_children=0&no_rooms=1&from_sf=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}

p = re.compile(r'RUB\s\d*(,\d\d\d)*')
canParsePage = True
i = 1
while canParsePage:
    request = requests.get(url, headers=headers)
    soup = bs(request.content, 'html.parser')

    for item in soup.find_all('div', class_='sr_item_content'):
        hotel = item.find(
            'span', class_='sr-hotel__name').get_text().strip()
        price = item.find('div', class_='totalPrice')
        record = str(i) + " [Hotel: " + hotel + "]"
        if price:
            record = record + \
                " [Price: " + p.search(price.get_text()).group() + "]"
        print(record)
        i += 1
    nextPage = soup.find('a', class_='paging-next')
    if nextPage:
        url = "https://www.booking.com" + nextPage['href']
    else:
        canParsePage = False
