# -*- coding: utf-8 -*-
__author__ = 'nanguoyu'
import urllib.request

url = 'https://api.heweather.com/x3/weather?cityid=CN101110103&key=xxxxxxxxxxxxxxx'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read()
print(content.decode("utf8"))
