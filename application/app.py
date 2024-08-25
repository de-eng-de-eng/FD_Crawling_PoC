import streamlit as st
import pandas as pd

def load_csv() -> (pd.DataFrame, pd.DataFrame):
    naver = pd.read_csv("./data/result_naver.csv")
    instagram = pd.read_csv("./data/result_instagram.csv")

    return naver, instagram

def main():

    dfNaver, dfInsta = load_csv()
    st.write("Running with Streamlit")
    
    tab1, tab2 = st.tabs(["Naver", "Instagram"])

    tab1.dataframe(
        dfNaver,
        column_config={"URL": st.column_config.LinkColumn("URL to website")},
    )

    tab2.dataframe(dfInsta,
        column_config={"URL": st.column_config.LinkColumn("URL to website")},
    )


if __name__ == "__main__":
    main()