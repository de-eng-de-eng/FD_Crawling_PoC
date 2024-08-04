import streamlit as st
import pandas as pd

def load_csv() -> (pd.DataFrame, pd.DataFrame):
    naver = pd.read_csv("./data/result_naver.csv")
    instagram = pd.read_csv("./data/result_instagram.csv")

    return naver, instagram

def main():

    dfNaver, dfInsta = load_csv()
    st.write("Running with Streamlit")

    rows = st.columns(2)

    rows[0].markdown("### Naver")
    rows[0].dataframe(dfNaver)
    
    rows[1].markdown("### Instagram")
    rows[1].dataframe(dfInsta)


if __name__ == "__main__":
    main()