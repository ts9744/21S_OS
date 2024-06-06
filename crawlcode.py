# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        print(f"요청 URL: {url}")  # 요청 URL 출력
        # HTTP 요청
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킵니다.
        response.encoding = response.apparent_encoding  # 인코딩 설정
        print(f"HTTP 요청 성공, 상태 코드: {response.status_code}")  # HTTP 상태 코드 출력
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        print("HTML 파싱 성공")  # HTML 파싱 성공 메시지 출력
        
        # 전체 HTML 출력
        print(soup.prettify())
        
    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청 중 오류 발생: {e}")
    except Exception as e:
        print(f"기타 오류 발생: {e}")

# 대상 URL
url = 'https://edu.dcinside.com/board/lists/?id=extra_new1'
get_html(url)

def get_links_with_keyword(url, keyword_text):
    try:
        print(f"요청 URL: {url}")  # 요청 URL 출력
        # HTTP 요청
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킵니다.
        response.encoding = response.apparent_encoding  # 인코딩 설정
        print(f"HTTP 요청 성공, 상태 코드: {response.status_code}")  # HTTP 상태 코드 출력
        
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        print("HTML 파싱 성공")  # HTML 파싱 성공 메시지 출력
        
        # 게시물 링크 추출
        links = []
        # 모든 게시물의 <tr> 요소 찾기
        keyword_elements = soup.find_all('tr', class_='ub-content us-post')
        print(f"게시물 수: {len(keyword_elements)}")  # 게시물 수 출력
        
        for keyword in keyword_elements:
            title_span = keyword.find('span', class_='mark')
            if title_span and keyword_text in title_span.text:
                link = keyword.find('a',href=True)['href']
                full_link = requests.compat.urljoin(url, link)
                print(f"키워드 포함된 게시물 링크: {full_link}")  # 키워드 포함된 게시물 링크 출력
                links.append(full_link)

        if not links:
            print("키워드가 포함된 게시물을 찾을 수 없습니다.")
        
        return links
    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청 중 오류 발생: {e}")
        return []
    except Exception as e:
        print(f"기타 오류 발생: {e}")
        return []

# 대상 URL과 검색할 키워드
url = 'https://edu.dcinside.com/board/lists/?id=extra_new1'
keyword_text = '루틴'

print("스크랩 시작")  # 스크랩 시작 메시지 출력
# 링크 스크랩
links = get_links_with_keyword(url, keyword_text)

print(f"스크랩된 링크 수: {len(links)}")  # 스크랩된 링크 수 출력
# 결과 출력
for link in links:
    print(link)
print("스크랩 종료")  # 스크랩 종료 메시지 출력


