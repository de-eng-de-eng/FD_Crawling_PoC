import src.naver
import src.instagram


def main():
    get_naver_crawler = src.naver.crawler()
    result_naver = get_naver_crawler.run()

    get_instagram_crawler = src.instagram.crawler()
    result_instagram = get_instagram_crawler.run()
    
    print("### 네이버 크롤링")
    print(result_naver)

    print("### 인스타그램 크롤링")
    print(result_instagram)



if __name__ == "__main__":
    main()