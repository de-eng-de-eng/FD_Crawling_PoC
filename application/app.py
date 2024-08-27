import streamlit as st
import pandas as pd

def load_csv() -> (pd.DataFrame, pd.DataFrame, pd.DataFrame):
#    naver = pd.read_csv("./data/result_naver.csv")
    naver_bizinfo = pd.read_excel("./Naver/Results/FD_Crawling_Business_Info_System_20240826.xlsx")
    naver_blog = pd.read_excel("./Naver/Results/FD_Crawling_Naver_Blog_20240826.xlsx")
#    instagram = pd.read_csv("./data/result_instagram.csv")
    instagram_feed = pd.read_csv("./Instagram/Final/Results/instagram_post_data.csv")


    return naver_bizinfo, naver_blog, instagram_feed

def main():

    dfNaverBizInfo, dfNaverBlog, dfInstaFeed = load_csv()
    st.write("(가칭) FD인벤토리 정보마당")
    #st.write("@Running with Streamlit")
    
    n_biz, n_blog, i_feed = st.tabs(["정보공개서", "네이버", "인스타그램"])

    n_biz.dataframe(
        dfNaverBizInfo,
        column_config={"URL": st.column_config.LinkColumn("URL to website")},
    )

    n_blog.dataframe(
        dfNaverBlog,
        column_config={"URL": st.column_config.LinkColumn("URL to website")},
    )

    i_feed.dataframe(
        dfInstaFeed,
        column_config={"post_url": st.column_config.LinkColumn("URL to website")},
    )


if __name__ == "__main__":
    main()
