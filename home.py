import streamlit as st

# サイドバーに選択ボックスを表示
page = st.sidebar.selectbox("ページを選択", ["home", "page2", "page3"])

# ページに応じてファイルをインポート
if page == "home":
    st.title("Home Page")
    st.write("これはホームページです。")

elif page == "page2":
    # page2.pyの内容を読み込む
    import page2

elif page == "page3":
    # page3.pyの内容を読み込む
    import page3
