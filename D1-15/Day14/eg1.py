from time import time
from threading import Thread

import requests


#继承Thread类创建自定义的线程类
class DownloadHandler(Thread):

    def __init__(self,url):
        super().__init__()
        self.url=url

    def run(self):
        filename=self.url[self.url.rfind('/')+1:]
        resp=requests.get(self.url)
        with open('/Ysers/Hao/*'+filename,'wb') as f:
            f.write(resp.content)


def main():
    '''
    通过requests模块中的get函数获取网路资源
    下面的代码中使用了天行数据接口提供的网络API
    要使用该数据接口血药再天行网站注册
    然后使用自己的key替换掉下面的APIkey即可
    :return:
    '''
    resp=requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
    #将服务器返回的JSON格式的数据解析为字典
    data_model=resp.json()
    for mm_dict in data_model['newlist']:
        url=mm_dict['picUtl']
        #通过多线程的方式实现图片下载
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()