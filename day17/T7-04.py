
# 동적페이지 크롤링2

import asyncio
from playwright.async_api import async_playwright
import pandas as pd

# 1. 크롤링 웹페이지

# 2. 동기화 함수선언: 동적페이지는 대기상태가 존재 -> `await`
# `async def 함수명():`
async def joongnaRun():
    async with async_playwright() as p:
        browser = await p.chromium.launch( headless=False )
        page = await browser.new_page()
        
        # 4. 크롤링할 페이지로 이동
        await page.goto( 'https://web.joongna.com/search/젤다?page=1' )
        
        # 5-1. 해당 페이지가 모두 열릴 때까지 대기: 시스템 상태(인터넷속도) 알 수 없을 때
        # `await page.wait_for_timeout( 밀리초 )`
        # `await page.wait_for_load_state( '특정상태' )`. `networkidle`: 통신이 모두 종료 상태.
        await page.wait_for_load_state( 'networkidle' )

        # 5-2. 특정한 검색창 활용
        await page.get_by_placeholder('최소 가격').fill('10000')  # '최소 가격' 입력상자에 10000 대입
        await page.wait_for_timeout( 1000 )
        await page.get_by_placeholder('최대 가격').fill('20000')  # '최대 가격' 입력상자에 20000 대입
        await page.wait_for_timeout( 1000 )
        # 가격 입력 후 버튼 클릭: 특정한 식별자가 없는 경우, 버튼에 보이는 이름을 `name=`가져올 수 있다.
        apply_button = page.get_by_role( 'button' , name='적용' )
        await apply_button.click()
        await page.wait_for_timeout(3000)
        
        # 6. 특정한 요소 가져오기 (참고: 식별자가 불명확할 경우 자식/자손 선택자 활용)
        items = await page.query_selector_all( 'div.group > div > a[href^="/product/"]')
        
        # 7. 제품명과 가격 추출
        # 선택자: `a[href=^"/링크/"]`: 해당 링크로 시작하는 링크
        for item in items:
            title_tag = await item.query_selector('span.text-14')
            title = await title_tag.inner_text() if title_tag else '제목없음'

            price_tag = await item.query_selector('span.text-18')
            price = await price_tag.inner_html() if price_tag else 0

            item = {'제목명': title, '가격': price}
            print( item )
            

9
# 동기 함수 실행: `asyncio.run( 동기함수() )`
asyncio.run( joongnaRun() )