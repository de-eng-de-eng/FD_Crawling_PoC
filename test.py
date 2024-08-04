import src.naver
import src.instagram


def main():
    get_naver_crawler = src.naver.crawler()
    result_naver = get_naver_crawler.run()
    result_naver.to_csv("./data/result_naver.csv", index=False)

    get_instagram_crawler = src.instagram.crawler()
    result_instagram = get_instagram_crawler.run()
    result_instagram.to_csv("./data/result_instagram.csv", index=False)

if __name__ == "__main__":
    main()