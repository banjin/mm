#!/usr/bin/python
#-*-coding:utf-8-*-

""",url=www.mzitu.com """

import re
import time
import urllib
import urllib2
import os
import sys


class PageList:
    def __init__(self,url):
        self.url=url
	        
    def getpageListhtml(self,url):
      
        """获取首页的html"""
				            
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	page_html=response.read()
	return page_html
									        
    def getpageList(self,html):
	"""获取图库的连接"""
											            
	pat=r'href="http://baliang616.blog.163.com/blog/(h+.*?\d\d\d\d)" title'
	patten=re.compile(pat)
	pagelist=re.findall(patten,html)
	print pagelist
																            
	for list in pagelist:
																		                
	    request=urllib2.Request(list)
	    res=urllib2.urlopen(request)
	    html=res.read()																									                
																								            p=r'src="http://baliang616.blog.163.com/blog/(.*?\.jpg)" '														
																									    pa=re.compile(p)																				
	    page=re.findall(pa,html)
  																							                    print page																															            
																									    path='/home/hand1234/图片/piaoliang/'+ time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
																									    if not os.path.exists(path):
																									        os.makedirs(path)
																									    else:
																									        pass
																									    os.chdir(path)
																									    k=0
																								            for i in page:													  																															                        urllib.urlretrieve(i,"%s.jpg" % k)                                                                                                                                                              
		k+=1					 																																								                        time.sleep(1)
	 																																										        
																																																def main():    
													                      									  	  																							    url=raw_input("please input a url:")   	 																																										    p=PageList(url)
																																																								                                                      
																																																    html=p.getpageListhtml(url)
																																															
																								    pagelist=p.getpageList(html)
																																																									        
																																																										       
																																																										          
																																																											          

											 																																				        if __name__=="__main__":
																																																    main()
