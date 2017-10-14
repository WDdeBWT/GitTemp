# coding = utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import re
import operator

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.coding = r.apparent_encoding
		return r.text
	except:
		print("---error0---")

def parsePageTao(ilt, html):
	#try:
	plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
	tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
	slt = re.findall(r'\"view_sales\"\:\"\d*?人付款\"',html)
	for i in range(len(plt)):
		price = eval(plt[i].split(':')[1])
		title = eval(tlt[i].split(':')[1])
		temp = eval(slt[i].split(':')[1])
		match = re.search(r'\d*', temp)
		if match:
			sales = int(match.group(0))
		else:
			print("---error1---")
		ilt.append([price , title, sales])
	ilt.sort(key = operator.itemgetter(2), reverse = True) #根据销量排序
	if (ilt[0][1] == ilt[1][1]):
		ilt.pop(0)
	for li in ilt:
		print(li)
		print("---error2---")
	#except:
	#	print("---error2---")

def parsePageJD(ilt, html):
	pass

def printList(ilt):
	pass

def main():
	url1 = "https://s.taobao.com/search?q=尊尼获加黑牌"
	url2 = "https://search.jd.com/Search?keyword=%E5%B0%8A%E5%B0%BC%E8%8E%B7%E5%8A%A0%E9%BB%91%E7%89%8C&enc=utf-8&wq=%E5%B0%8A%E5%B0%BC%E8%8E%B7%E5%8A%A0%E9%BB%91%E7%89%8C&pvid=9f4cd6c2c1974ab0a97806854a11e538"
	infolist = []
	html = getHTMLText(url1)
	parsePageTao(infolist, html)
	tplt = "{:4}\t{:8}\t{:16}\t{:8}"
	print(tplt.format("序号", "价格", "商品名称", "销量"))
	count = 0
	for g in range(3):
		print(tplt.format(count, infolist[g][0], infolist[g][1]), infolist[g][2])
	print("----------")

main()