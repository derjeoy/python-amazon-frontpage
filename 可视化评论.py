import requests
from lxml import etree
import re
import matplotlib.pylab as plt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Cookie': 'x-wl-uid=1DVw4k4T/jAduWIfwW2jvf029Ha4Bgv/AJGjP/yRfJTdq26dr7oDdeEBdb6zOPUl0ByfsaKJ3GUY=; session-id-time=2082729601l; session-id=457-7649276-4174543; csm-hit=tb:DAHATSQRZZBWHWD4ZXYP+s-T61YJHRDEC6Y6S2VMTVZ|1573355007668&t:1573355007668&adb:adblk_no; ubid-acbcn=459-2457809-1906210; session-token="4sZGQQPKw9CJUOzJFLsTdS3FtlpqIyp0hyvhXL6RMOchbDf7p7YLDEL90YFps2Hl80fBT6uPmzQ00meCLYxsrjuoabX3+kz7OB+CLw8GaAYZB8J9oBBcJLBUsGs6LLm/EHQht5Tm0IpOKR0hz0GGtATgcpJXDfRoEdvNol+CUc3mXOMA5KmEfFWstdV+KwyzSGrGW+DdrAftisgZMl2stffIdhcOLh53B4tJwsR5awKqPrOqZF8uJg=="; lc-acbcn=zh_CN; i18n-prefs=CNY'
} #添加headers模拟浏览器防止被发现
hao = []
zhong = []
cha = [] #获取到的评论数存入里面
def parge_page(url):
    response = requests.get(url=url,headers=headers)
    #print(response) #测试一下看看也没有请求到网页
    text = response.text
    html = etree.HTML(text)
    
    file=open("2.html","w",encoding='utf-8')  
    file.write(text)
    file.close()
    
    quan = html.xpath('//div[@id="cm_cr-review_list"]/div') #获取到每个人的评论
    for i in quan:
        pinfen1 = i.xpath('.//span[@class="a-icon-alt"]/text()') #获取到每个人的评分几颗星
        pinlun = i.xpath('.//a[@data-hook="review-title"]/span/text()') #获取到每个人评论的字
        #print(pinlun)
        for pinfen in pinfen1:
            #print(pinlun)
            a = re.sub('颗星，最多 5 颗星','',pinfen) #使用正则把后面不用的字符串替换为空，显得好看
            #print(a)
            list = {'评论':pinlun,'评分': a}
            print(list)
            if a < str(2.0): #判断，小于3颗星就存入差评
                cha.append(a)
            elif a < str(4.0): #小于4颗星就存入中评
                zhong.append(a)
            else:
                hao.append(a) #否则都是好评

def main():
    # url = 'https://www.amazon.cn/product-reviews/B074MFRPWL'
    # parge_page(url)
    for x in range(10): #获取100条评论，一页10条
        url = 'https://www.amazon.cn/product-reviews/B074MFRPWL/?pageNumber='+ str(x) #网站：TIGER 虎牌 水壶 直饮水杯 迷你不锈钢水杯
        #url = 'https://www.amazon.cn/product-reviews/B01N5WPXA7/?pageNumber=' +str(x) #网站：Tiger 600 毫升水瓶带直饮水杯，2 WAY 不锈钢水壶配袋
        parge_page(url)
    print({'好评数':len(hao),'中评数':len(zhong),'差评数':len(cha)}) #输出好中差评各有多少
    x = ['hao','zhong','cha']   #进行可视化输出
    y = [len(hao),len(zhong),len(cha)]
    plt.ylim(0, 100)
    plt.plot(x, y, 'o') #x是x轴，y是y轴,o是展现形式（散点图）
    plt.show() #
if __name__ == '__main__':
    main()  #调用main方法
