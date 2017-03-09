#coding:utf8
from bs4 import BeautifulSoup

import urllib2

#访问链接

def get_html_cont(root_url):

	html_cont=urllib2.urlopen(root_url).read()

	return html_cont

#获取文章列表


def get_article_list(html_cont):


	data=BeautifulSoup(html_cont,'lxml',from_encoding='utf-8')

	data_list=data.find("div",class_="grid-8").find_all("a",class_="archive-title")

	for artic in data_list:
		print artic.get_text(),artic['href'],"\n"

#爬去固定页面数

def get_all_page(start,end):

	base_url="http://python.jobbole.com/all-posts/page/"
	for i in range(start,end):
		root_url="%s%d"%(base_url,i)
		print "======开始爬取第%d页内容======\n"%(i)
		html_cont = get_html_cont(root_url)
		get_article_list(html_cont)
		print "======第%d页爬取完成======\n"%(i)

if __name__ == "__main__":
	get_all_page(1,31)