import requests
import re 

book_url='https://www.wfxs.org/html/11591/'
response_1 = requests.get(book_url)
response_1.encoding = 'big5'
 
#print(response_1.text)
# part of the results
# <dd><a href="/html/11591/9181171.html">第113章 冰凍三尺</a></dd>
# <dd><a href="/html/11591/9232049.html">第114章 歸宿</a></dd>
# <dd><a href="/html/11591/9334310.html">第115章 船僧</a></dd>
# <dd><a href="/html/11591/9356796.html">第116章 蓬萊</a></dd>
# <dd><a href="/html/11591/9384079.html">第117章 復仇</a></dd>
# <dd><a href="/html/11591/9504533.html">第118章 蠱毒</a></dd>
# <dd><a href="/html/11591/9616530.html">第119章 何懼</a></dd>
# <dd><a href="/html/11591/9702621.html">第120章 碎遮</a></dd>
# <dd><a href="/html/11591/9734455.html">第121章 濟南</a></dd>

regx = '<dd><a href="(.*)"'

chapter_href_list = re.findall(regx,response_1.text)
chapter_url_list,filename_list = [],[]
 
#--------------
base_url = 'https://www.wfxs.org' 
for id in chapter_href_list:
	url = base_url + id
	print(url)
	chapter_url_list.append(url)
	

#--------------
#capture the content 
content_regx = '&nbsp;&nbsp;&nbsp;&nbsp;(.*)<br \/>'
title_regx = '<title>(.*)<\/title>'

 
#-------------
#檢查名稱 是不是有特殊字符
# 
def check_escape_id(words):
#input
	for id in range(len(words)):		
		if re.findall('[^0-9a-zA-Z *]',words[id]) != []:
			words[id]=re.sub('[^0-9a-zA-Z *]','',words[id])
	return words
	
test_words = ['h/e\llo <wor=ld> ?　','hello /|@daf','hweir!@']

#print(check_escape_id(test_words))
#---------
#將內容儲存成txt file 

count = 0
#print(filename_list)
#print(save_path)
save_path = 'D:/tmp/test.txt'

'''
for x in chapter_url_list:
	response_2 = requests.get(x)
	response_2.encoding = 'big5'	
	title = re.findall('<title>(.*)\(.*\)',response_2.text)) 
 	#file_name = re.sub('\/',' ',filename,3)
	#save_path = 'D:/tmp/{}.txt'.format(file_name)
	with open (save_path,'a+',encoding='big5',errors='ignore') as f:
		title = re.findall(title_regx,response_2.text)
		content = re.findall(content_regx,response_2.text)
		
		for k in title:
			f.write(k+'\n')
		for e in content:
			f.write(e+'\n')
 
		count += 1
		print('第{}章抓取完畢'.format(count))
'''
	