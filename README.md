# Python 기초(+ ~~카카오톡~~ 네이버톡톡 챗봇 만들기) 스터디

## < 개요 >

#### 1주차) 1/17
  - [자료형](https://github.com/tnehf18/chatbot/blob/master/ch01_datatype/%EC%9E%90%EB%A3%8C%ED%98%95.md "자료형")
  - [제어문](https://github.com/tnehf18/chatbot/blob/master/ch02_control/%EC%A0%9C%EC%96%B4%EB%AC%B8.md "제어문")

#### 2주차) 1/24
  - [함수](https://github.com/tnehf18/chatbot/blob/master/ch03_function/%ED%95%A8%EC%88%98.md "함수")
  - [클래스](https://github.com/tnehf18/chatbot/blob/master/ch04_class/%ED%81%B4%EB%9E%98%EC%8A%A4.md "클래스")

#### 3주차) 1/31
  - [모듈](https://github.com/tnehf18/chatbot/blob/master/ch05_module/%EB%AA%A8%EB%93%88.md "모듈")
  - [예외처리](https://github.com/tnehf18/chatbot/blob/master/ch06_exception/%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC.md "예외처리")

#### 4주차) 2/7 
  - [엑셀 파일을 읽고 쓰는 방법](https://github.com/tnehf18/chatbot/blob/master/ch07_file/%ED%8C%8C%EC%9D%BC%EC%B2%98%EB%A6%AC.md "파일 처리")

#### 번외
  - [데이터베이스 제어](https://github.com/tnehf18/chatbot/blob/master/ch08_database/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4.md "데이터베이스")

#### 5주차, 6주차) 2/14, 2/21
  - 챗봇 만들기 프로젝트


### 프로젝트

> 챗봇 API 서버: <https://www.memoryrecord.site/>

> 카카오톡 채널: 구현중
 
> 네이버톡톡 채널: <https://talk.naver.com/W47XFR>


- 운영 환경

```
서버 OS: 우분투 18.04 LTS (AWS EC2)
웹 서버: NGINX 1.14
```


- 프로젝트 소스 구성

```
프로젝트 ROOT
┝─── static             # css, js, 이미지 파일 등 정적 리소스
┝─── template           # html 등 웹 페이지 화면  ※ 현재는 없음.
┝─── event_handler      # 이벤트 처리 모듈
│       │
│       ┝─── kakaoTalk.py       # 카카오톡 이벤트 처리 모듈
│       └─── naverTalk.py       # 네이버톡톡 이벤트 처리 모듈
┝─── api.py             # 챗봇 API 모듈
└─── engine.py          # 챗봇 엔진 모듈
```

※ 참고:

[네이버톡톡 챗봇 API 문서](https://github.com/navertalk/chatbot-api "네이버톡톡 챗봇 API 문서")

[네이버 톡톡 파이썬 모듈](https://github.com/hwonyo/naver_talk_sdk "네이버 톡톡 파이썬 모듈") by hwonyo

[카카오 i 오픈빌더 문서](https://i.kakao.com/docs/key-concepts-block "카카오 i 오픈빌더 문서")
```
※ 기본적으로 네이버톡톡 API 문서는 node.js, 스프링, php 를 예제를 설명하고, 파이썬용은 따로 없는데,
  다른 분이 비즈니스 로직에 집중할 수 있도록 만든 파이썬용 오픈 소스 모듈입니다.
  
  굉장히 훌륭한 모듈이지만, 기초를 학습하고자 하는 목적에서 본 프로젝트에는 사용되지 않았습니다. 
```

 
## < 교재 >

Python Tutorial: <https://www.w3schools.com/python/default.asp> [w3school]

점프 투 파이썬!: <https://wikidocs.net/book/1> [위키독스]

파이썬 - 기본을 갈고 닦자!: <https://wikidocs.net/book/1553> [위키독스]

처음 배우는 딥러닝 챗봇: <https://www.hanbit.co.kr/store/books/look.php?p_code=B7030488815> [한빛미디어]


> ※ 본 자료는 위 자료들을 참고하여 작성되었음을 알립니다.
