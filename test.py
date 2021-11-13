import urllib3
from urllib import request
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup

import lxml.html
import requests

from lxml import etree
import re
import matplotlib.pylab as plt
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Cookie': 'x-wl-uid=1DVw4k4T/jAduWIfwW2jvf029Ha4Bgv/AJGjP/yRfJTdq26dr7oDdeEBdb6zOPUl0ByfsaKJ3GUY=; session-id-time=2082729601l; session-id=457-7649276-4174543; csm-hit=tb:DAHATSQRZZBWHWD4ZXYP+s-T61YJHRDEC6Y6S2VMTVZ|1573355007668&t:1573355007668&adb:adblk_no; ubid-acbcn=459-2457809-1906210; session-token="4sZGQQPKw9CJUOzJFLsTdS3FtlpqIyp0hyvhXL6RMOchbDf7p7YLDEL90YFps2Hl80fBT6uPmzQ00meCLYxsrjuoabX3+kz7OB+CLw8GaAYZB8J9oBBcJLBUsGs6LLm/EHQht5Tm0IpOKR0hz0GGtATgcpJXDfRoEdvNol+CUc3mXOMA5KmEfFWstdV+KwyzSGrGW+DdrAftisgZMl2stffIdhcOLh53B4tJwsR5awKqPrOqZF8uJg=="; lc-acbcn=zh_CN; i18n-prefs=CNY'
} #添加headers模拟浏览器防止被发现

def parge_page(url):
    response = requests.get(url=url,headers=headers)
    #print(response) #测试一下看看也没有请求到网页
    text = response.text
    html = etree.HTML(text)
    quan = html.xpath('//div[@id="cm_cr-review_list"]/div') #获取到每个人的评论
    for i in quan:
        pinfen1 = i.xpath('.//span[@class="a-icon-alt"]/text()') #获取到每个人的评分几颗星
        pinlun = i.xpath('.//a[@data-hook="review-title"]/span/text()') #获取到每个人评论的字
        #print(pinlun)

def main():
    # url = 'https://www.amazon.cn/product-reviews/B074MFRPWL'
    # parge_page(url)
    for x in range(10): #获取100条评论，一页10条
        url = 'https://www.amazon.cn/product-reviews/B074MFRPWL/?pageNumber='+ str(x) #网站：TIGER 虎牌 水壶 直饮水杯 迷你不锈钢水杯
        #url = 'https://www.amazon.cn/product-reviews/B01N5WPXA7/?pageNumber=' +str(x) #网站：Tiger 600 毫升水瓶带直饮水杯，2 WAY 不锈钢水壶配袋
        parge_page(url)
 
    
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"

def amazon_price(r):    
    r.encoding = r.apparent_encoding
    tree = lxml.html.fromstring(r.text.encode("utf-8"))
    print(tree)
    #print(tree.cssselect("span#priceblock_ourprice"))
    #price = tree.cssselect("span#priceblock_ourprice")[1]
    return 1;price.text_content().encode("gbk").strip("￥")
 
if __name__ == "__main__":
    kv = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    
    url = "https://www.amazon.es/dp/B08QZQKXW2"
    req = request.Request(url,headers = kv)
    sleep(10)
    try:
        web = request.urlopen(req)
    except HTTPError as e:
                rank_want = "网页找不到，下架？拼写正确？服务器？UPC？"
                print(e.code)
    except URLError as e:
                rank_want = "网络连接失败"
                sleep(150)
    else:
            soup = BeautifulSoup(web.read(),"html.parser")
            try:
                price = soup.findAll("span",class_="priceblock_ourprice")
                print(price)
            except :
                print("expection")
    finally:
        print("expection111")
                
    
    #print(response.status_code)  #打印结果为：503，说明访问出现错误。
    #print(response.encoding)     #查看它的编码，打印结果：ISO-8859-1,
    #print(response.request.headers)
    #text = web.text
    #print(text)

    #tree = etree.HTML(text)
    #price = tree.cssselect("span#priceblock_ourprice")[0]
    

    file=open("1.html","w",encoding='utf-8')  
    file.write(price)
    file.close()



    
    #print(getHTMLText(url))
    #print(amazon_price(r))
    
    #r.encoding = r.apparent_encoding  #把编码改成它可执行的编码
    #r.text          #查看返回的文本


    #print(r.status_code)
    #r.encoding = "utf-8"
    #print(r.text)
    #print(getHTMLText(url))
