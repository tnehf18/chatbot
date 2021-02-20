# /home/ubuntu/project/chatbot/event_handler/naverTalk.py
"""
네이버톡톡 이벤트 처리
"""

import json
import time
import requests


class NaverHandler:

    # 생성자
    def __init__(self, authorization_key):
        self.authorization_key = authorization_key

    # 문자열 컨텐츠 요소
    def getTextContent(self, text):
        return {
            "textContent": {
                "text": text
            }
        }

    # 이미지 컨텐츠 요소
    def getImageContent(self, image_url):
        return {
            "imageContent": {
                "imageUrl": image_url
            }
        }

    # 컴포지트 컨텐츠 요소
    def getCompositeContent(self, title=None, desc=None, els=None, image_url=None, btns=None):

        contents = dict()

        if title is not None:
            contents.update(title=title)
        if desc is not None:
            contents.update(description=desc)
        if els is not None:
            # 조금 복잡해서 현재는 생략
            contents.update(elementList=els)
        if image_url is not None:
            img = {
                "imageUrl": image_url
            }
            contents.update(image=img)
        if btns is not None:
            contents.update(buttonList=btns)

        return {
            "compositeContent": {
                "compositeList": [
                    contents
                ]
            }
        }

    # 복수 컨텐츠 생성
    def getContents(self, *args):
        contents = []
        for cont_type, arg in args:
            if cont_type == "text":
                contents.append(self.getTextContent(arg))
            elif cont_type == "image":
                contents.append(self.getImageContent(arg))
            elif cont_type == "composite":
                contents.append(self.getCompositeContent(arg))
            elif cont_type == "self":
                contents.append(arg)

        return contents

    # 메시지 전송
    def send_msg(self, user_key, content, delay=0):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': self.authorization_key
        }

        data = {
            "event": "send",
            "user": user_key
        }
        data.update(content)

        msg = json.dumps(data)
        time.sleep(delay)
        requests.post(
            'https://gw.talk.naver.com/chatbot/v1/event',
            headers=headers,
            data=msg
        )

    # 메시지 연속 전송
    def send_msg_interval(self, user_key, *contents, interval=0):
        for i, content in enumerate(contents):
            if i is not 0:
                time.sleep(interval)
            self.send_msg(user_key, content)
