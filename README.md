# 简介

Solr是一个独立的企业级搜索应用服务器，它对外提供类似于Web-service的API接口。用户可以通过http请求，向搜索引擎服务器提交一定格式的XML文件，生成索引；也可以通过Http Get操作提出查找请求，并得到XML格式的返回结果。
Apache-Solr任意文件读取漏洞漏洞，攻击者可以在未授权的情况下读取目标服务器敏感文件和相关内容。

# 影响版本

Apache Solr <= 8.8.1

# 使用方法
python Apache_Solr_Poc.py

脚本会读取ip.txt中的ip进行批量验证,如果读取/etc/passwd成功会记录在vuln.txt文件中。

# 效果
![image](https://user-images.githubusercontent.com/18067503/111721194-5d80df00-889a-11eb-8175-e10c4705cefe.png)
