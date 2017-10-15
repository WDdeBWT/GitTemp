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
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print("---error0---")

def parsePageTao(ilt, html):
	try:
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
			ilt.append([price, title, sales])
		ilt.sort(key = operator.itemgetter(2), reverse = True) #根据销量排序
		if (ilt[0][2] == ilt[1][2]):
			ilt.pop(0)
	except:
		print("---error2---")

def parsePageJD(ilt, html):
	popli = []
	soup = BeautifulSoup(html, "html.parser")
	htl = soup.find_all('li', class_ = "gl-item")
	for i in range(len(htl)):
		if len(htl[i].get("data-sku")) > 7:
			continue
		alla = htl[i].find_all("a")
		price = htl[i].find('div', class_='p-price').i.string
		for a in alla:
			if a.em != None:
				title = a.em.text
				ilt.append([price, title])

def printList(infolistTao, infolistJD):
	tpltTao = "{:4}\t{:8}\t{:32}\t{:8}\t"
	print("\n---淘宝数据：序号，价格，品名，销量---\n")
	for g in range(5):
		print(tpltTao.format(g+1, infolistTao[g][0], infolistTao[g][1], infolistTao[g][2]))
	tpltJD = "{:4}\t{:8}\t{:32}\t"
	print("\n---京东数据：序号，价格，品名---\n")
	for g in range(len(infolistJD)):
		print(tpltJD.format(g+1, infolistJD[g][0], infolistJD[g][1]))
	print("\n--------------------------------------------------\n")

def main():
	goods = "鼠标"
	urlTao = "https://s.taobao.com/search?q=" + goods
	urlJD = "https://search.jd.com/Search?keyword=" + goods + "&enc=utf-8"
	infolistTao = []
	infolistJD = []
	htmlTao = getHTMLText(urlTao)
	parsePageTao(infolistTao, htmlTao)
	htmlJD = getHTMLText(urlJD)
	parsePageJD(infolistJD, htmlJD)
	printList(infolistTao, infolistJD)

main()