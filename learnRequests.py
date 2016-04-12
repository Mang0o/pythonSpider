#coding:utf-8
import requests
data = {
	'form_email':'956310246@qq.com',
	'form_password':'123456zz',
	'captcha-solution':'cloud',
	'captcha-id':'bcoESdpucJdXBRFdycopGIyR:en'
}
r = requests.get("http://www.qiushibaike.com")#,data=data)

print r.text.encode('gb18030')

# from bs4 import BeautifulSoup
# import re

# doc = ['<html><head><title>Page title</title></head>',
#        '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
#        '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
#        '</html>']
# soup = BeautifulSoup(''.join(doc))

# print soup.prettify()


