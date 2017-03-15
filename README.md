# jobbole_python_spider
简单的爬虫爬取伯乐在线python版文章

# 环境依赖
1.Mac OS X EI Capitan 10.11.6

2.python 2.7.10

3.需要安装  bs4,lxml
```
sudo pip install bs4
sudo pip install lxml
```

# 使用方式
假设要爬取1-32页数据，则修改最后一行为

get_all_page(1,32)
