import streamlit as st
import fitz  # PyMuPDF
from gtts import gTTS
import os

# PDFファイルのパス
pdf_path = "./DX-9.pdf"

# 音声ファイルの保存ディレクトリ
audio_dir = "./audio"
os.makedirs(audio_dir, exist_ok=True)

# セッション状態で現在のページ番号を保持
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

    # ページのテキストを取得
    page_text = page.get_text()

# 音声ファイルのパス
audio_file = f"{audio_dir}/page_{st.session_state.page_number + 1}.mp3"

# 音声ファイルが存在しない場合、gTTSで生成
if not os.path.exists(audio_file):
    tts = gTTS(text=page_text, lang='ja')
    tts.save(audio_file)

# 音声の再生ボタン
if st.button("音声再生"):
    st.audio(audio_file)

# ページ遷移ボタン
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("前のページ") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("次のページ") and st.session_state.page_number < num_pages - 1:
        st.session_state.page_number += 1

st.write(f"現在のページ: {st.session_state.page_number + 1} / {num_pages}")

