# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def get_links_with_keyword(url, keyword):
    try:
        # HTTP 요청
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킵니다.
        print("HTTP 요청 성공, 상태 코드:", response.status_code)
        
        # HTML 파싱
        soup = BeautifulSoup(response.content, 'html.parser')
        print("HTML 파싱 성공")
        
        # 게시물 목록 찾기
        posts = soup.find_all('a', class_='subject')
        print(f"게시물 수: {len(posts)}")
        
        # 게시물 링크 추출
        links = []
        for post in posts:
            if keyword in post.text:
                print(f"키워드 포함된 게시물: {post.text}")
                links.append(post['href'])

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
keyword = '루틴'

# 링크 스크랩
links = get_links_with_keyword(url, keyword)

# 결과 출력
print(f"스크랩된 링크 수: {len(links)}")
for link in links:
    print(link)
