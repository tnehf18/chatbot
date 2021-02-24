# /home/ubuntu/project/chatbot/api.py
"""
챗봇 API 입니다.
"""

import json
import random
import datetime as dt
from flask import Flask, request, abort
import engine

app = Flask(__name__)


# 최초 웹 루트 접속 경로
@app.route('/', methods=['GET'])
def index():
    return '''<div>
    <h2>chatbot API 서버입니다. 반갑습니다. :)</h2>
    <ul>
      <li>카카오톡: 미구현</li>
      <li>네이버톡톡: 가동중 <a href="http://talk.naver.com/W47XFR">[채팅방 접속하기]</a></li>
    </ul>
    </div>
    '''


# API 연결
@app.route('/talk/<platform>', methods=['POST'])
def talk(platform):

    if platform == "NAVER":
        # 네이버톡톡
        return naver_api()

    elif platform == "KAKAO":
        # 카카오톡
        return kakao_api()

    else:
        # 정의되지 않은 platform 일 경우 404 오류
        abort(404, "알 수 없는 요청입니다.")


# 네이버톡톡 API
def naver_api():

    # NaverHandler 클래스 생성
    from event_handler.naverTalk import NaverHandler

    handler = NaverHandler('FActz2vcTDqHeOLgFkyo')

    body = request.get_json()
    user_key = body['user']
    event = body['event']

    try:

        if event == "open":
            # 채팅방 입장시 이벤트
            print(f"채팅방에 유저가 들어왔습니다. user: {user_key} [{dt.datetime.now()}]")
            print(json.dumps(body, indent=4))

            options = body["options"]

            if options["friend"]:
                msg = "다시 와주셨군요. 반갑습니다. :D"
                content = handler.getTextContent(msg)

                handler.send_msg(user_key, content)

                if options["unreadMessage"]:
                    content = handler.getTextContent("읽지 않은 메시지가 있습니다.")
                    handler.send_msg(user_key, content, delay=1)

            else:
                msg = random.choice(["안녕하세요. 나는 챗봇입니다. :)", "반가습니다~, 무엇을 도와드릴까요?", "어서오세요."])
                text_content = handler.getTextContent(msg)

                info_content = handler.getTextContent('안내를 원하시면 "안내"라고 말하시거나, 아래의 메시지에서 버튼을 클릭해주세요.')

                btns = [
                    {
                        "type": "TEXT",
                        "data": {
                            "title": "안내",
                            "code": "help"
                        }
                    },
                    {
                        "type": "LINK",
                        "data": {
                            "title": "깃허브 링크",
                            "url": "https://github.com/tnehf18/chatbot",
                            "mobileUrl": "https://github.com/tnehf18/chatbot"
                        }
                    }
                ]
                btn_content = handler.getCompositeContent(title="안내", image_url="https://www.memoryrecord.site/static/img/thumb.png", btns=btns)

                handler.send_msg_interval(user_key, text_content, info_content, btn_content, interval=1)

            return json.dumps({}), 200

        elif event == "send":
            # 채팅창 채팅, 버튼 등 입력시 이벤트
            print(f"유저가 메시지를 보내왔습니다. user: {user_key} [{dt.datetime.now()}]")
            print(json.dumps(body, indent=4))

            if "imageContent" in body:
                user_img = body["imageContent"]

                case_1 = (
                    handler.getImageContent("https://memoryrecord.site/static/img/original_2.png"),
                    handler.getTextContent("무슨 사진이죠?")
                )
                case_2 = (
                    handler.getImageContent("https://memoryrecord.site/static/img/original_10.png"),
                    handler.getTextContent("죄송합니다. 아직 이미지 분석 기능은 없습니다.")
                )
                contents = random.choice((case_1, case_2))

                handler.send_msg_interval(user_key, *contents)

            elif "textContent" in body:
                user_msg = body["textContent"]

                # 사용자 채팅 입력시 대응
                # ※ 교재에서는 이 시점에서 챗봇 엔진에 접속해 사용자가 입력한 채팅 내용에 따라, DB에서 조회하여 처리하도록 구현됨.
                answers = engine.getResponse(body["textContent"])
                contents = handler.getContents(*answers)

                handler.send_msg_interval(user_key, *contents, interval=1)

            return json.dumps({}), 200

        elif event == "friend":
            # 친구추가, 소식듣기 관련 이벤트
            print(f"친구추가 관련 이벤트가 발생했습니다. {user_key}")
            print(json.dumps(body, indent=4))

            if body["options"]["set"] == "on":
                contet = handler.getImageContent("https://memoryrecord.site/static/img/original_6.png")
                handler.send_msg(user_key, contet)
            elif body["options"]["set"] == "off":
                content = handler.getTextContent("ㅠㅠ")
                handler.send_msg(user_key, content)

            return json.dumps({}), 200

        elif event == "leave":
            # 채팅방 나갔을 때 이벤트
            print(f"유저가 채팅방을 나갔습니다. user: {user_key} [{dt.datetime.now()}]")
            print(json.dumps(body, indent=4))

            return json.dumps({}), 200

    except Exception as e:
        print(e.args)
        abort(500)
        return json.dumps({}), 500


# 카카오톡 API
def kakao_api():

    # KakaoTemplate 클래스 생성
    from event_handler.kakaoTalk import KakaoTemplate

    skill = KakaoTemplate()

    body = request.get_json()
    req = body['userRequest']

    contents = engine.getResponse(req['utterance'])


    return skill.send_resp(contents)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
