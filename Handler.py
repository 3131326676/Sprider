import urllib.request
import http.cookiejar

# 使用IP代理
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://112.87.69.220:9999',
    'https': 'https://218.91.112.139:9999'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())

# 请求携带cookie
cookie = http.cookiejar.CookieJar()
hanlder = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hanlder)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)
