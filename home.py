import streamlit as st

st.title("Home Page")
st.write("これはホームページです。")

import os
from pdf2image import convert_from_path

# 保存用のディレクトリを作成
output_dir = "./slides"
os.makedirs(output_dir, exist_ok=True)

# PDFファイルのパスを指定
pdf_path = "./DX-9.pdf"

# PDFを画像に変換して、スライドごとに指定したフォルダに保存
slides = convert_from_path(pdf_path)
for i, slide in enumerate(slides):
    slide.save(f"{output_dir}/slide_{i+1}.png", "PNG")  # 各ページを指定フォルダに保存

from gtts import gTTS

# 各スライドに対応するテキスト
slide_texts = ["スライド1の内容です", "スライド2の内容です", "最後のスライドです"]

# スライドごとに音声ファイルを生成
for i, text in enumerate(slide_texts):
    tts = gTTS(text=text, lang='ja')
    tts.save(f"audio_{i+1}.mp3")

import streamlit as st
import simpleaudio as sa

# スライド画像と音声ファイルをリストに格納
slide_images = [f"slide_{i+1}.png" for i in range(len(slides))]
audio_files = [f"audio_{i+1}.mp3" for i in range(len(slides))]

# セッション状態でスライドのインデックスを管理
if 'slide_index' not in st.session_state:
    st.session_state['slide_index'] = 0

# スライドのインデックスに基づいて画像と音声を表示
slide_index = st.session_state['slide_index']
st.image(slide_images[slide_index], use_column_width=True)

# 音声の再生ボタン
if st.button("音声再生"):
    wave_obj = sa.WaveObject.from_wave_file(audio_files[slide_index])
    play_obj = wave_obj.play()
    play_obj.wait_done()

# 次のスライドへ進むボタン
if st.button("次のスライド"):
    if slide_index < len(slide_images) - 1:
        st.session_state['slide_index'] += 1

