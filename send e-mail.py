import requests
import yagmail
from parsel import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
jssf_url = 'http://yz.ujs.edu.cn/index/sszs.htm'
jssf_response = requests.get(url=jssf_url, headers=headers)
jssf_response.encoding = 'utf-8'
# print(jsdx_response.text)
html = jssf_response.text
sel = Selector(text=html)
all_titles = sel.css('tr:nth-child(1) > td > a ::text').getall()
title = all_titles[0]
# print(all_titles)
# print(title)
str = '初试'
if str in title:
    # print(1)
    content = [
        '貌似可以查看初试成绩了-------',
        'http://yz.ujs.edu.cn/index/sszs.htm'
    ]
    sender = '***@qq.com'
    password = '***'
    res = '***@qq.com'
    yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', smtp_ssl=True)
    yag.send(to=res, subject='今日初试通知', contents=content)
else:
    # print(2)
    content = '今日还不能查看初试成绩-------'
    sender = '***@qq.com'
    password = '***'
    res = '***@qq.com'
    yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', smtp_ssl=True)
    yag.send(to=res, subject='今日初试通知', contents=content)
