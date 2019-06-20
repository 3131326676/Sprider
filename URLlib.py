import urllib.request
import urllib.parse
import urllib.error
import socket

# 基本请求的发送
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# 请求时带上数据
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# 获取响应内容
print(response.read())

# response = urllib.request.urlopen('http://httpbin.org/post',timeout=3)
# print(response.read())


# 捕获请求时的异常
try:
    response = urllib.request.urlopen('http://httpbin.org/post', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

response = urllib.request.urlopen('https://www.python.org')
# 响应类型
print(type(response))
# 响应的状态码
print(response.status)
# 响应的头部信息
print(response.getheaders())
# 响应头中的server信息
print(response.getheader('Server'))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germay'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))

print('h')