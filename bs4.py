#!/usr/bin/python
# coding:utf-8

from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
import os


def get_all_page_link():
    """
    获取所有的首页所有网页链接
    :return: 
    """
    html = urlopen('http://www.meizitu.com/')
    bsObj = BeautifulSoup(html, "html.parser")
    page_links = bsObj.find_all("a", {'href': re.compile('^http:.*?\.html$')})
    print page_links

    return page_links


def get_pages(page_links):
    """
    获取多个页面的图片
    :return: 
    """
    os.chdir('/data/DA/pachong/pic')
    for link in page_links:
        html = urlopen(link['href'])
        bsObj = BeautifulSoup(html, "html.parser")
        images = bsObj.find_all("img", {'src': re.compile('^http:.*?\.jpg$')})
        all_file_len = len(os.listdir('.'))
        k = all_file_len
        print "start downing ....."
        for image in images:
            print image['src']
            urlretrieve(image['src'], "%s.jpg" % k)
            k += 1
    print "end....."


def get_page():
    """
    获取单个页面的图片
    :return: 
    """
    os.chdir('/data/DA/pachong/pic')
    html = urlopen('http://www.meizitu.com/a/4119.html')
    bsObj = BeautifulSoup(html, "html.parser")
    images = bsObj.find_all("img", {'src': re.compile('^http:.*?\.jpg$')})
    all_file_len = len(os.listdir('.'))
    k = all_file_len
    print "start downing ....."
    for image in images:
        print image['src']
        urlretrieve(image['src'], "%s.jpg" % k)
        k += 1
    print "end....."

if __name__ == "__main__":

    all_link = get_all_page_link()
    for link in all_link:
         print link['href']
    get_page()

