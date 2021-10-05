# -*- coding: utf-8 -*-
#載入LineBot所需要的套件
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
# import test_fun

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('2LhA8MJ4slIH6qMURWRlGGNiuDwMJr9qJ5qcEiF2M9+K8X1aS4RQZcjlxfGC7X322/Jte+lx5uA1LmFWhxY6lI6g32FJYn8sQTWLMPCacJG7POpPs7fUULm8YlyV+zf+GP1lLUtWkG14kYp4yMuGoAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret

handler = WebhookHandler('059810822c07be59f4794448fce49d1a')
your_ID = 'U62a78d3a1ec5b920108d2e18040c64dd'
line_bot_api.push_message(your_ID, TextSendMessage(text='the robot wakes up'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['x-line-signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

 
#處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token,TextSendMessage(text='I am ready!'))
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))

    
    
 
#主程式

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
