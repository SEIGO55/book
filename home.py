import streamlit as st
import fitz  # PyMuPDF

# PDFファイルのパス
pdf_path = "./DX-9.pdf"

# ストリームリットセッションで現在のページ番号を保持
if 'page_number' not in st.session_state:
    st.session_state.page_number = 0

# PDFのページ数を取得
with fitz.open(pdf_path) as pdf_document:
    num_pages = pdf_document.page_count

# 現在のページを画像に変換して表示
with fitz.open(pdf_path) as pdf_document:
    page = pdf_document[st.session_state.page_number]
    # ページをピクセル画像としてレンダリング
    pix = page.get_pixmap()
    image = pix.tobytes("png")

    st.image(image, caption=f"Page {st.session_state.page_number + 1} / {num_pages}")

# ページ遷移のためのボタンを設置
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("前のページ") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("次のページ") and st.session_state.page_number < num_pages - 1:
        st.session_state.page_number += 1

st.write(f"現在のページ: {st.session_state.page_number + 1} / {num_pages}")
