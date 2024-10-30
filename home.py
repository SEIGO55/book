import streamlit as st
import fitz  # PyMuPDF
from gtts import gTTS
import os

# PDFファイルのパス
pdf_path = "./DX-9.pdf"

# 音声ファイルとスクリプトファイルの保存ディレクトリ
audio_dir = "./audio"
script_dir = "./scripts"
os.makedirs(audio_dir, exist_ok=True)
os.makedirs(script_dir, exist_ok=True)

# セッション状態で現在のページ番号を保持
if 'page_number' not in st.session_state:
    st.session_state.page_number = 0

# 現在のページに対応するスクリプトファイルのパス
script_file = f"{script_dir}/script_{st.session_state.page_number + 1}.txt"

# スクリプトファイルが存在するか確認し、内容を読み込む
if os.path.exists(script_file):
    with open(script_file, "r", encoding="utf-8") as file:
        page_script = file.read()
else:
    page_script = "音声はありません。"

# PDFのページ数を取得
with fitz.open(pdf_path) as pdf_document:
    num_pages = pdf_document.page_count

# 現在のページを画像に変換して表示
with fitz.open(pdf_path) as pdf_document:
    page = pdf_document[st.session_state.page_number]
    pix = page.get_pixmap()
    image = pix.tobytes("png")
    st.image(image, caption=f"Page {st.session_state.page_number + 1} / {num_pages}")

# 音声ファイルのパス
audio_file = f"{audio_dir}/page_{st.session_state.page_number + 1}.mp3"

# 音声ファイルが存在しない場合、gTTSで生成
if not os.path.exists(audio_file):
    tts = gTTS(text=page_script, lang='ja')
    tts.save(audio_file)

# 音声の自動再生
st.audio(audio_file, autoplay=True)

# ページ遷移ボタン
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("前のページ") and st.session_state.page_number > 0:
        st.session_state.page_number -= 1

with col3:
    if st.button("次のスライド") and st.session_state.page_number < num_pages - 1:
        st.session_state.page_number += 1

st.write(f"現在のページ: {st.session_state.page_number + 1} / {num_pages}")


