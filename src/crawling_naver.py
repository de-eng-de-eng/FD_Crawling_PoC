from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.common.by import By
import datetime
import time
import pandas as pd


class crawling_nvaer():
    
    def __init__(self):
        self.base_url = "https://section.blog.naver.com/ThemePost.naver?directoryNo=29&activeDirectorySeq=3&currentPage=1"
        try:
            self.chrome_driver = webdriver.Chrome()
            #크롬 드라이버 설치 링크 : https:storage.googleapis.com/chrome-for-testing-public/127.0.6533.72/win64/chromedriver-win64.zip
            #압축 해제 후, driver.exe는 실행파일과 같은 위치 혹은 하위에 존재해야 함
            #사내망에선 드라이버의 물리적 위치 괄호 안에 지정해줘야 함
        except SessionNotCreatedException as e:
            print("SessionNotCreatedExceptions이 발생했습니다:", str(e))

    def run_crawler(self) -> pd.DataFrame:
        self.chrome_driver.get(self.base_url)
        time.sleep(3)

        post_titles = self.chrome_driver.find_elements(By.CLASS_NAME,'title_post')

        crawler_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        crawler_date = datetime.datetime.now().strftime('%Y%m%d')

        App = "Naver Blog"
        data = []

        print("-----네이버 블로그 - 맛집 포스트-----")
        for page in range(1,3): ##1~2페이지까지
            self.chrome_driver.find_element(By.XPATH, '/html/body/ui-view/div/main/div[1]/div/section/div[2]/div[11]/span[{}]/a'.format(page)).click()
            time.sleep(2)

            #포스트 제목
            post_titles = self.chrome_driver.find_elements(By.CLASS_NAME,'title_post')

            #포스트 url
            post_urls = self.chrome_driver.find_elements(By.CLASS_NAME,'desc_inner')
            urls = []
            for i in post_urls :
                href = i.get_attribute('href')
                print(href)
                urls.append(href)

            for idx, post_title in enumerate(post_titles[9:]): ## Top 3 제거(제목너무 짧음), 공백 행 제거
                title = post_title.text
                line_data = []
                line_data.append(App)
                line_data.append(title)
                line_data.append(urls[idx])
                line_data.append(crawler_time)
                data.append(line_data)
        self.chrome_driver.close()

        df = pd.DataFrame(data, columns= ['App', 'Post Title', 'URL', 'Crawler Time'])
        
        return df