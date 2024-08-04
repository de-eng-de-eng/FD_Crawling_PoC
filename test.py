from src.crawling_naver import crawling_nvaer


def main():
    get_naver_post = crawling_nvaer()

    result = get_naver_post.run_crawler()

    print(result)


if __name__ == "__main__":
    main()