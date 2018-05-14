import requests
import re
import random
import time
from bs4 import BeautifulSoup
import urllib

class download:
    
    def __init__(self):
        self.iplist=[]
        User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        header = {}
        header['User-Agent'] = User_Agent
        b=requests.get('http://www.xicidaili.com/wt/',headers=header)
        html=urllib.parse.unquote_plus(b.text)
        b_1=BeautifulSoup(html,'lxml').find_all('tr',class_='odd')
        for b_x in b_1:
            ip_add=b_x.find_all('td')[1].get_text()
            duankou=b_x.find_all('td')[2].get_text()
            tou=b_x.find_all('td')[5].get_text()
            IP=tou.lower()+'://'+ip_add+':'+duankou
            self.iplist.append(IP)
        
        #self.iplist = ['http://218.56.132.154:8080','http://125.89.54.43:9797']  ##初始化一个list用来存放我们获取到的IP
 #       html = requests.get('http://www.xicidaili.com/nt') ##获取代理网站
#http://www.xicidaili.com/nt/
       # iplistn = re.findall(r'r/>(.*?)<b', html.text,re.S) ##
     #   
      #  iplistn=BeautifulSoup(html,'lxml').fiand_all(class_='odd')
                            
   #     for ip in iplistn:
       #     ip=iplistn.contents[1]
       #     i = re.sub('\n','',ip)
       #     print(i)
        #    self.iplist.append(i.strip())
            
        self.user_agent_list =[
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"                               
                               ]
    def get(self,url,host,refere,timeout,proxy=None,num_retries=6):
        UA = random.choice(self.user_agent_list)
 #       headers={'user-Agent': UA}
        header = {
               'Accept':'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding' : 'gzip, deflate, sdch',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'Connection':'keep-alive',
               'Cookie':'AJSTAT_ok_pages=1; AJSTAT_ok_times=29',
               'Host':host,
               'Referer':refere,
               'User-Agent':UA,
               'X-Requested-With':'XMLHttpRequest'
               }

        if proxy==None:
            try:
                
                return requests.get(url,headers=header,timeout=timeout) ##这样服务器就会以为我们是真的浏览器了
            except: ##如过上面的代码执行报错则执行下面的代码
                if num_retries>0:
                    time.sleep(10)
                    print(u'获取网页错误，10S后将获取倒数第：',num_retries, u"次")
                    return self.get(url,host,refere,timeout,num_retries-1)
                else:
                    print('开始代理')
                    time.sleep(10)
                    IP=''.join(str(random.choice(self.iplist)).strip())
                    print(IP)
                    proxy = {'http':IP}
                    return self.get(url,host,refere,timeout,proxy)
            
        else:
            try:
                IP=''.join(str(random.choice(self.iplist)).strip())
                
                proxy = {'http':IP}
                print(proxy)
                return requests.get(url,headers=header,proxies=proxy,timeout=timeout)
            except:
                
                if num_retries >0:
                    time.sleep(10)
                    IP=''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http':IP}
                    print('正在更换代理，10S后将重新获取倒数第',num_retries,'次')
                    print('当前代理是:',proxy)
                    return self.get(url,host,refere,timeout,proxy,num_retries-1)
                else:
                    print('代理也不好用了 取消代理')
                    return self.get(url,host,refere,3)
        
    
request = download()
