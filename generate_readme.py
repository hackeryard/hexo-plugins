#coding:utf-8  
from lxml import etree
import requests
import codecs
import sys

if len(sys.argv) == 1:
    print('''
    Usage: python generate_readme.py [my_site_url]
    The default site is https://hackeryard.github.io, use the arg [my_site_url] to replace it
    使用命令行参数设置生成的Readme中博客地址, 如 https://hackeryard.github.io
    ''')
    my_site = "https://hackeryard.github.io"

elif len(sys.argv) == 2:
    my_site = sys.argv[1]

else:
    print('''
    Usage: python generate_readme.py [my_site_url]
    The default site is https://hackeryard.github.io, use the arg [my_site_url] to replace it
    使用命令行参数设置生成Readme中的博客地址, 如 https://hackeryard.github.io
    ''')
    sys.exit(1)

with codecs.open("./public/archives/index.html", "r", "utf-8") as f:
    text = f.read()
html = etree.HTML(text)
script = html.xpath("//a[@class='category-list-link']/text()")
script2 = html.xpath("//a[@class='category-list-link']/@href")

script3 = html.xpath("//a[@class='tag-list-link']/text()")
script4 = html.xpath("//a[@class='tag-list-link']/@href")

script5 = html.xpath("//a[@class='archive-list-link']/text()")
script6 = html.xpath("//a[@class='archive-list-link']/@href")


with open("./source/README.MDOWN", "w") as file:
    file.write("# 欢迎大家访问我的博客站点\n\n")
    file.write("## 分类:\n\n")
    for i in range(len(script)):
        catas = "[{0}]({1})".format(script[i], my_site + script2[i])
        file.write("- " + catas + "\n\n")
        print(catas)

    file.write("## Tags:\n\n")
    for i in range(len(script3)):
        tags = "[{0}]({1})".format(script3[i], my_site + script4[i])
        file.write("- " + tags + "\n\n")        
        print(tags)

    file.write("## 归档:\n\n")
    for i in range(len(script5)):
        archives = "[{0}]({1})".format(script5[i], my_site + script6[i])
        file.write("- " + archives + "\n\n")                
        print(archives)


    