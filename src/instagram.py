from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd


class crawler():

    def __init__(self):
        self.base_url = "https://www.instagram.com/accounts/login/"
        try:
            self.chrome_driver = webdriver.Chrome()
        except SessionNotCreatedException as e:
            print("SessionNotCreatedExceptions이 발생했습니다:", str(e))


    def run(self) -> pd.DataFrame:
        
        # 인스타그램 로그인 페이지 접속
        self.chrome_driver.get(self.base_url)
        time.sleep(3)

        # 로그인 정보 입력 및 제출
        try:
            # 사용자 이름과 비밀번호 입력 요소를 대기
            username = WebDriverWait(self.chrome_driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password = self.chrome_driver.find_element(By.NAME, 'password')

            # 사용자 이름과 비밀번호 입력
            username.send_keys('wel_data')
            password.send_keys('WelstoryDATA@13')

            # 로그인 버튼 클릭
            login_button = self.chrome_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            login_button.click()
        except Exception as e:
            print(f"Error during login: {e}")
            self.chrome_driver.quit()

        # 로그인 완료 대기 및 팝업 무시
        try:
            # 비밀번호 저장 팝업 처리
            WebDriverWait(self.chrome_driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now') or contains(text(), '나중에 하기')]"))
            ).click()

            # 알림 설정 팝업 처리
            WebDriverWait(self.chrome_driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now') or contains(text(), '나중에 하기')]"))
            ).click()
        except Exception as e:
            print(f"Error handling popups: {e}")

        # 특정 해시태그 페이지로 이동
        hashtag = '건대맛집'
        self.chrome_driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

        # 동적 콘텐츠 로드 대기
        time.sleep(5)

        # 스크롤을 통해 추가 콘텐츠 로드 (예: 3번 스크롤)
        for _ in range(3):
            self.chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        # 페이지 소스 가져오기
        page_source = self.chrome_driver.page_source

        # BeautifulSoup으로 페이지 파싱
        soup = BeautifulSoup(page_source, 'html.parser')

        data = []

        # 게시물 데이터 추출 (예: 게시물 링크)
        posts = soup.find_all('a', href=True)
        for post in posts:
            link = post['href']
            if '/p/' in link:  # 게시물 링크 필터링
                url = f'https://www.instagram.com{link}'
                data.append(url)

        # 브라우저 종료
        self.chrome_driver.quit()
        
        df = pd.DataFrame(data, columns= ['URL'])

        return df