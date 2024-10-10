import streamlit as st
import section1
import section1_1
import section2

# サイドバーを使ってページを選択
st.sidebar.title("目次")
page = st.sidebar.selectbox("セクションを選んでください：", 
                            ["1章 - 業務と機械学習プロジェクト", 
                             "1.1 本書の目的", 
                             "2章 - データサイエンスの基礎知識"])

# 選択されたページを表示
if page == "1章 - 業務と機械学習プロジェクト":
    section1.show()
elif page == "1.1 本書の目的":
    section1_1.show()
elif page == "2章 - データサイエンスの基礎知識":
    section2.show()
