'''
Created on 2017年5月16日

@author: Administrator
'''
from urllib.error import URLError
import urllib.request


def post(url, data):
    
    """
    url：掌厅连接
    data：body内容
    
                返回值：
      response_code = 200
                    返回正常json结果
            
      response_code != 200
                    返回http状态码
            
                    网络异常
                    返回异常原因

    """
    while_time = 0
    while(True):
        try:
            req = urllib.request.Request(url, data)
            datas = data.encode(encoding='utf_8')
        
            headers = {
                "platform":"iPhone",
                "channel":"T_WAP",
                "version":"3.3.2",
                "Content-Type":"application/x-www-form-urlencoded",
                "Cookie":"SmsNoPwdLoginCookie=BEE699D4816A18875C9B7DC808B76B3E"
                }
            
            req = urllib.request.Request(url, headers=headers, data=datas)
            response = urllib.request.urlopen(req)
            
            if (response.status == 200):
                return response.read().decode('UTF-8')

        # 无网络连接，报异常,重试三次...
        except URLError as e:
            try:
                if isinstance(e.code, int):
                    return e.code
            except: 
                if (while_time == 2):
                    print("访问超过3次,退出...")
                    return e.reason
                      
                while_time = while_time + 1
                print("访问超时，第"+ str(while_time) +"次尝试")
    


def get():
    return 



if __name__ == "__main__":
    url = "http://218.205.252.24:18080/scmccClient/action.dox"
    data = "auth=yes&appKey=00011&md5sign=|FOR_PRESSURE_TEST|&internet=WiFi&sys_version=10.3&screen=750*1334&model=iPhone&imei=C243B1B7-B541-427B-957C-B7F8C1E03B1E&deviceid=C243B1B7-B541-427B-957C-B7F8C1E03B1E&version=3.3.2&msgId=5453168626900314811&jsonParam=%5B%7B%22dynamicURI%22:%22/softUpdate%22,%22dynamicParameter%22:%7B%22method%22:%22versionUpgradeInfo%22%7D,%22dynamicDataNodeName%22:%22softUpdate_Node%22%7D%5D"
    
    print(post(url, data))