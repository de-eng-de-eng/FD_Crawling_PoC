from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import datetime
import time
import pandas as pd


class crawler():
    
    def __init__(self):
        self.base_url = "https://section.blog.naver.com/ThemePost.naver?directoryNo=29&activeDirectorySeq=3&currentPage=1"
        try:
            self.chrome_driver = webdriver.Chrome()
        except SessionNotCreatedException as e:
            print("SessionNotCreatedExceptions이 발생했습니다:", str(e))

    def GetAddress(self, addr_url):
        print(addr_url)
        try:
            driver = webdriver.Chrome()
            #크롬 드라이버 설치 링크 : https:storage.googleapis.com/chrome-for-testing-public/127.0.6533.72/win64/chromedriver-win64.zip
            #압축 해제 후, driver.exe는 실행파일과 같은 위치 혹은 하위에 존재해야 함
            #사내망에선 드라이버의 물리적 위치 괄호 안에 지정해줘야 함
        except SessionNotCreatedException as e:
            print("SessionNotCreatedExceptions이 발생했습니다:", str(e))
            
        #블로그 링크 하나씩 불러서 크롤링
        contents = []
        restaurant_name = []
        restaurant_address = []
        
        #블로그 링크 하나씩 불러오기
        driver.get(addr_url)
        time.sleep(1)
        #블로그 안 본문이 있는 iframe에 접근하기
        driver.switch_to.frame("mainFrame")
        #본문 내용 크롤링하기
        #본문 내용 크롤링하기
        try:
            a = driver.find_element(By.CSS_SELECTOR,'div.se-main-container').text
            contents.append(a)
        # NoSuchElement 오류시 예외처리(구버전 블로그에 적용)
        except NoSuchElementException:
            a = driver.find_element(By.CSS_SELECTOR,'div#content-area').text
            contents.append(a)
        #print(본문: \n', a)

        # driver.quit() #창닫기
        print("<<본문 크롤링이 완료되었습니다.>>")
        # print(contents)

        print("<<본문의 장소 정보입니다.>>")
        text = contents[0]
        contents_list = text.split("\n")
        print(contents_list)
        try:
            found = contents_list.index('© NAVER Corp.') ## 네이버 지도 전체가 위젯으로 넣어진 경우
            restaurant_name.append(contents_list[found+1])
            restaurant_address.append(contents_list[found+2])
            print(restaurant_name)
            print(restaurant_address)
        except ValueError:
            try : 
                found = contents_list.index('예약')
                restaurant_name.append(contents_list[found-2])
                restaurant_address.append(contents_list[found-1])
                print(restaurant_name)
                print(restaurant_address)
            except ValueError:
                try : 
                    found = contents_list.index('주소')
                    restaurant_name.append(contents_list[found-1])
                    restaurant_address.append(contents_list[found+1])
                    print(restaurant_name)
                    print(restaurant_address)
                except ValueError:
                    print("장소 정보를 찾을 수 없습니다.") ## 네이버 지도 일부가 위젯으로 넣어지거나, 지도가 본문에 첨부되지 않은 경우
                    restaurant_name.append(" ")
                    restaurant_address.append(" ")
                    print(restaurant_name)
                    print(restaurant_address)
        driver.quit() #창닫기

        return restaurant_name[0], restaurant_address[0]
        

    def GetNaverBlog(self, crawler_time):
        App = "Naver Blog"
        data = []
        
        # post_titles = driver.find_elements(By.CLASS_NAME,'title_post')

        #크롤링 시작
        print("-----네이버 블로그 - 맛집 포스트-----")
        for page in range(1,3): ##1~2페이지까지. 5분 소요
            self.chrome_driver.find_element(By.XPATH, '/html/body/ui-view/div/main/div[1]/div/section/div[2]/div[11]/span[{}]/a'.format(page)).click()
            time.sleep(2)

            #포스트 제목
            post_titles = self.chrome_driver.find_elements(By.CLASS_NAME,'title_post')

            #포스트 url, 식당명, 식당주소
            post_urls = self.chrome_driver.find_elements(By.CLASS_NAME,'desc_inner')
            urls = []
            name = []
            address = []

            for i in post_urls :
                href = i.get_attribute('href')
                # print(href)
                urls.append(href)

            for url in urls :
                res_name, res_address = self.GetAddress(url)
                name.append(res_name)
                address.append(res_address)

            for idx1, post_title in enumerate(post_titles[9:]): ## Top 3 제거(제목너무 짧음), 공백 행 제거
                title = post_title.text
                line_data = []
                line_data.append(App)
                line_data.append(title)
                line_data.append(urls[idx1])
                line_data.append(name[idx1])
                line_data.append(address[idx1])
                line_data.append(crawler_time)
                data.append(line_data)
        
        self.chrome_driver.close()

        #데이터 프레임 생성
        df = pd.DataFrame(data, columns= ['App', 'Post Title', 'URL', 'Restaurant Name', 'Restaurant Address', 'Crawler Time'])
        df.index = df.index+1
        return df

    

    def run(self) -> pd.DataFrame:
        self.chrome_driver.get(self.base_url)
        time.sleep(3)

        crawler_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        result = self.GetNaverBlog(crawler_time)

        return result