# /home/ubuntu/project/chatbot/event_handler/engine.py
"""
챗봇 엔진 모듈입니다.
(※ 원래는 얘도 단독으로 서버로서 실행되어, 챗봇 API 와 소켓 통신을 주고받아야 하나, 임시로 모듈로 사용합니다.)
"""

import datetime
import requests
import random
from bs4 import BeautifulSoup

greeting = ["안녕", "안녕?", "안녕하세요", "안녕하세요?", "반가워", "반가워요.", "반갑습니다.", "ㅎㅇ", "ㅎㅇ?", "hello", "hi"]
req_info = ["안내", "소개", "자기소개", "도움말", "help", "도와줘", "기능"]
req_word = ["할 줄 아는 게 뭐니?", "뭘 할 수 있니?", "가능한 단어", "입력 가능한 단어"]
req_time = ["현재 시간", "현재 시각", "지금", "몇 시?", "몇 시니?", "시계"]
req_weather = ["날씨", "비"]
req_resv = ["예약", "step1", "step2"]
thx_word = ["ㄳ", "감사", "감사합니다", "고마워", "고맙습니다."]
bad_word = ["나쁜놈", "ㅅㅂ"]


def getResponse(textContent):
    if textContent["inputType"] == "typing":
        user_text = textContent["text"].strip()

        result = []
        if user_text in greeting:
            result = [
                ("text", random.choice(greeting))
            ]
        elif user_text in req_info:
            result = [
                ("text", " ".join('''저는 파이썬으로 구현된 간단한 대화형 챗봇입니다.
                이름은 아직 없구요. 현재까지는 "날씨", "예약" 등의 간단한 기능만 존재합니다. 
                '''.split()))
                , ("text", "아쉽지만, 인공지능은 챗봇 아니에요. ㅋ")
                , ("image", "http://memoryrecord.site/static/img/original_5.png")
                , ("text", "입력하신 정보에 따라 정해진 답변만 하도록 되어 있습니다.")
                , ("text", "아직은 말이죠")
            ]
        elif user_text in req_time:
            result = [
                ("text", "현재 시각은")
                , ("self", {
                    "text": datetime.datetime.today().strftime("%H:%M:%S"),
                    "code": "current_time",
                    "inputType": "time"
                })
                , ("text", "입니다.")
            ]
        elif user_text in req_weather:
            soup = BeautifulSoup(requests.get("https://weather.naver.com/today/").text, "html.parser")
            summary = soup.select_one(".summary")

            result = [
                ("text", "오늘 날씨를 검색합니다. ※ 현재는 서울만 가능합니다.")
                , ("text", f"{soup.select_one('.current').text} / {soup.select_one('.before_slash').text}")
                , ("text", summary.find(text=True).strip() + summary.select_one('.temperature').text if summary.select_one('.temperature') else "")
            ]

            today_chart_list = soup.select_one(".today_chart_list")
            for i, today_chart in enumerate(today_chart_list.select(".ttl")):
                result.append(("text", f"{today_chart.text} {today_chart_list.select('.level_text')[i].text}입니다."))

        elif user_text in req_resv:
            result = [
                ("image", "http://memoryrecord.site/static/img/original_10.png")
                , ("text", "아직 우리 채널은 만들어진 지 얼마 안되서 파트너가 없어요.")
                , ("text", "하지만 나중을 위해서 예제를 준비했답니다.")
                , ("text", "한번 해 보아요.")
                , ("image", "http://memoryrecord.site/static/img/original_14.png")
                , ("self", {
                    "compositeContent": {
                        "compositeList": [
                            {
                                "title": "톡톡 레스토랑",
                                "description": "파스타가 맛있는집",
                                "image": {
                                    "imageUrl": "http://ldb.phinf.naver.net/20171212_39/1513070642332Sre4X_JPEG/lLWrszsMNIW4RLx5R_or39IB.JPG.jpg"
                                },
                                "buttonList": [
                                    {
                                        "type": "CALENDAR",
                                        "data": {
                                            "title": "방문 날짜 선택하기",
                                            "code": "step1",
                                            "options": {
                                                "calendar": {
                                                    "placeholder": "방문 날짜를 선택해주세요.",
                                                    "start": datetime.datetime.today().strftime("%Y%m%d"),
                                                    "end": "20210430",
                                                    "disables": "20210309,20210315-20210316"
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                })
            ]
        elif user_text in thx_word:
            result = [
                ("text", "저두요 ♡")
            ]
        elif user_text in bad_word:
            result = [
                ("image", "http://memoryrecord.site/static/img/police.jpg")
                , ("text", "경찰 아저씨 여기예요!")
            ]
        else:
            result = [
                ("image", "http://memoryrecord.site/static/img/original_10.png")
                , ("text", "죄송합니다. 알 수 없는 요청입니다.")
            ]

        return result

    elif textContent["inputType"] == "button":
        user_code = textContent["code"].strip()

        result = []
        if user_code in req_info:
            result = [
                ("text", " ".join('''저는 파이썬으로 구현된 간단한 대화형 챗봇입니다.
                이름은 아직 없구요. 현재까지는 "날씨", "예약" 등의 간단한 기능만 존재합니다. 
                '''.split()))
                , ("text", "아쉽지만, 인공지능은 챗봇 아니에요. ㅋ")
                , ("image", "http://memoryrecord.site/static/img/original_5.png")
                , ("text", "입력하신 정보에 따라 정해진 답변만 하도록 되어 있습니다.")
                , ("text", "아직은 말이죠")
            ]
        elif user_code == "confirm":
            result = [
                ("image", "http://memoryrecord.site/static/img/original_10.png")
                , ("text", "죄송합니다. 아직 예약정보를 불러오는 기능은 구현되지 않았습니다.")
            ]
        else:
            result = [
                ("image", "http://memoryrecord.site/static/img/original_10.png")
                , ("text", "죄송합니다. 알 수 없는 요청입니다.")
            ]

        return result

    elif textContent["inputType"] == "sticker":
        user_text = textContent["text"]

        # 유저가 보낸 이모티콘 그대로 이모티콘으로 응답 가능한지 테스트
        content_1 = {
            "textContent": {
                "text": user_text,
                "inputType": "sticker"
            }
        }
        content_2 = {
            "textContent": {
                "text": "사용자가 보낸 이모티콘 ID: " + user_text,
                "inputType": "typing"
            }
        }
        # 테스트 결과, 이모티콘으로 보내는 응답하는 것은 불가능한 것으로 파악됨.
        # ("스티커를 전송했습니다." 라는 메시지만 출력됨. 심지어 앞에 텍스트를 붙여도 Id 값을 인식함.)
        #
        # 챗봇에서 사용자에게 기존에 네이버에 있는 이모티콘을 사용하는 것을 불가능해 보이며,
        # 이미지를 미리 업로드 해놓고, 이를 텍스트 만큼 빠르게 전송하는 방법을 권하고 있음.
        # ※ 챗봇과 사용자가 보유한 이모티콘이 다르며, 또한 서로 다르게 암호화되기 때문인 것으로 추측됨.

        return [
            ("self", content_1)
            , ("self", content_2)
            , ("image", "http://memoryrecord.site/static/img/original_2.png")
            , ("text", "이모티콘이 없나봐요, 데헷")
        ]

    elif textContent["inputType"] == "calendar":
        user_code = textContent["code"].strip()

        result = []
        if user_code == "step1":
            result = [
                ("text", "시간을 선택해주세요."),
                ("self", {
                    "compositeContent": {
                        "compositeList": [
                            {
                                "title": "톡톡 레스토랑",
                                "description": "파스타가 맛있는집",
                                "image": {
                                    "imageUrl": "http://ldb.phinf.naver.net/20171212_39/1513070642332Sre4X_JPEG/lLWrszsMNIW4RLx5R_or39IB.JPG.jpg"
                                },
                                "buttonList": [
                                    {
                                        "type": "TIME",
                                        "data": {
                                            "title": "방문 시간 선택",
                                            "code": "step2"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                })
            ]

        return result

    elif textContent["inputType"] == "time":
        user_code = textContent["code"].strip()

        result = []
        if user_code == "step2":
            result = [
                ("text", "예약이 완료되었습니다."),
                ("image", "http://memoryrecord.site/static/img/original_6.png"),
                ("self", {
                    "compositeContent": {
                        "compositeList": [
                            {
                                "title": "톡톡 레스토랑",
                                "description": "파스타가 맛있는집",
                                "image": {
                                    "imageUrl": "http://ldb.phinf.naver.net/20171212_39/1513070642332Sre4X_JPEG/lLWrszsMNIW4RLx5R_or39IB.JPG.jpg"
                                },
                                "elementList": {
                                    "type": "LIST",
                                    "data": [
                                        {
                                            "title": "예약 완료",
                                            "description": "날짜",
                                            "image": {
                                                "imageUrl": "http://ldb.phinf.naver.net/20171212_39/1513070642332Sre4X_JPEG/lLWrszsMNIW4RLx5R_or39IB.JPG.jpg"
                                            },
                                            "button": {
                                                "type": "TEXT",
                                                "data": {
                                                    "title": "확인",
                                                    "code": "confirm"
                                                }
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                })
            ]

        return result

    elif textContent["inputType"] == "vphone":
        result = [
            ("image", "http://memoryrecord.site/static/img/original_10.png")
            , ("text", "죄송합니다. 아직 구현되지 않았습니다.")
        ]

        return result
    else:
        result = [
            ("image", "http://memoryrecord.site/static/img/original_2.png")
            , ("text", "죄송합니다. 알 수 없는 요청입니다.")
        ]

        return result
