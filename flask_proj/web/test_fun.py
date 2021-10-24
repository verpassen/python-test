#-*- encoding: utf-8 -*-

test_inputmsg=['你好','你是誰','聯絡方式']
test_sentance = ['您好 我想問一下關於AH725','有型錄嗎?','電話多少','','']

#-----------------------------------------------------------------------------

basic_info = {"CompanyName":"台灣泰珂洛","Tel":"02-85219986","Fax":"02-85218935",
"WebSite":"https://subs.tungaloy.com/tw/","Facebook":"https://www.facebook.com/Tungaloy-Taiwan-281690456087000",
"Contact":"https://subs.tungaloy.com/tw/contact/","Address":"新北市新莊區中央路293號9樓",
"Youtube":"https://www.youtube.com/user/TungaloyCorporation"}
'''
def aboutTungaloy():
	print('您好 我們是%s\n' % (basic_info['CompanyName']))
	print('公司電話:%s' % (basic_info['Tel']))
	print('傳真電話:%s' % (basic_info['Fax']))
	print('公司位於:%s\n' % (basic_info['Address']))
	print('若對於公司產品有任何問題，都可在我們官網找到相關的資訊')
	print('官網連結:%s\n' % (basic_info['WebSite']))
	print('也歡迎您關注我們臉書粉絲團:%s' % basic_info['Facebook'])
	print('或是追蹤我們的youtube頻道:%s' % basic_info['Youtube'])
	print('都可以讓您在第一時間得到我們最新的產品資訊喔!')
'''
def aboutTungaloy():
	reply = []
	reply.append('您好 我們是%s\n' % (basic_info['CompanyName']))
	reply.append('公司電話:%s' % (basic_info['Tel']))
	reply.append('傳真電話:%s' % (basic_info['Fax']))
	reply.append('公司位於:%s\n' % (basic_info['Address']))
	reply.append('若對於公司產品有任何問題，都可在我們官網找到相關的資訊')
	reply.append('官網連結:%s\n' % (basic_info['WebSite']))
	reply.append('也歡迎您關注我們臉書粉絲團:%s' % basic_info['Facebook'])
	reply.append('或是追蹤我們的youtube頻道:%s' % basic_info['Youtube'])
	reply.append('都可以讓您在第一時間得到我們最新的產品資訊喔!')
	return reply
#-----------------------------------------------------------------------------
def handle_message(input_txt):
    # message = TextSendMessage(text=input_txt)
	df = load_data('insert.json') 
	aboutTungaloy() 
	greeting(input_txt)
	# aboutTungaloy()
    # reply_msg
    # return reply_msg

def greeting(input_txt):
	gener_speaking = ['您好','你好','請問','妳好']
	good_byes_pharse = ['Goodebye','再見','感謝','bye','掰']
	if input_txt in gener_speaking:
		return ('您好，有什麼需要為您服務的嗎?')
	elif input_txt in good_byes_pharse:
		return ('感謝您的詢問，歡迎有任何問題\n 隨時與我們聯絡，謝謝')


def load_data(file):
	import json
	import os
	filepath = os.getcwd()
	FileName = (os.getcwd()+ "\\" + file)

	with open(FileName,'r') as f:
		data = f.read()
	obj_insert = json.loads(data)['chipbreaker']
	obj_grades = json.loads(data)['Grade']
	return [obj_insert,obj_grades]	 






