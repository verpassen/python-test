import requests
import re 
 

book_url='https://www.hetubook.com/book/4750/'
response_1 = requests.get(book_url)
response_1.encoding = 'utf8'
 
print(response_1.text)
# part of the results
'''
第一章
https://www.hetubook.com/book/4750/3524210.html
第二章
https://www.hetubook.com/book/4750/3524211.html
第三章
https://www.hetubook.com/book/4750/3524212.html
114章
https://www.hetubook.com/book/4750/3524323.html
'''
# <dd><a href="/book/4750/3524210.html" title="第1章 停雲榭">
# <dd><a href="/book/4750/3524211.html" title="第2章 飛寇兒">
# <dd><a href="/book/4750/3524212.html" title="第3章 風華貌">

regx = '<h2 class=.*>(.*)<'
chapter_href_list = re.findall(regx,response_1.text)
chapter_url_list,filename_list = [],[]

print(chapter_href_list)
#--------------
base_url = 'https://www.hetubook.com/' 
for id in chapter_href_list:
	url = base_url + id
	# print(url)
	chapter_url_list.append(url)
	
# print(chapter_url_list)
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
	