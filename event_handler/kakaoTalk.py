# /home/ubuntu/project/chatbot/event_handler/kakaoTalk.py
"""
카카오톡 템플릿
"""


class KakaoTemplate:

    # 생성자
    def __init__(self):
        self.version = "1.0"

    # 단순 텍스트
    def textComponent(self, text):
        return {
            "simpleText": {
                "text": text
            }
        }

    # 단순 이미지
    def imageComponent(self, image_url, alt_text=''):
        return {
            "simpleImage": {
                "imageUrl": image_url,
                "altText": alt_text
            }
        }

    # 응답 메시지 전송
    def send_resp(self, bot_resp):
        responseBody = {
            "version": self.version,
            "template": {
                "outputs": []
            }
        }

        if bot_resp['AnswerImageUrl'] is not None:
            responseBody['template']['outputs'].append(
                self.imageComponent(bot_resp['AnswerImageUrl'])
            )

        if bot_resp['Answer'] is not None:
            responseBody['template']['outputs'].append(
                self.imageComponent(bot_resp['Answer'])
            )

        return responseBody
