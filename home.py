import streamlit as st
from gtts import gTTS
import os

import streamlit as st
from PIL import Image

# スライド画像を保存するディレクトリを指定
output_dir = "./slides"
# スライド画像を読み込むパスを指定（例: slides フォルダ内に画像が保存されている前提）
slide_images = [f"{output_dir}/slide_{i+1}.png" for i in range(3)]  # スライドの数に合わせて調整

# 各画像が存在するか確認
for image_path in slide_images:
    st.write("Image path exists:", image_path)  # デバッグ用にファイルパスを表示

# スライドのインデックスに基づいて画像を表示
if slide_images:
    st.image(slide_images[0], use_column_width=True)
else:
    st.write("No slide images found.")

# 各スライドに対応するテキスト
slide_texts = ["スライド1の内容です", "スライド2の内容です", "最後のスライドです"]

# スライドごとに音声ファイルを生成（既に生成済みの場合はスキップ）
for i, text in enumerate(slide_texts):
    audio_path = f"audio_{i+1}.mp3"
    if not os.path.exists(audio_path):  # 音声ファイルが存在しない場合に生成
        tts = gTTS(text=text, lang='ja')
        tts.save(audio_path)

# スライド画像と音声ファイルをリストに格納
slide_images = [f"{output_dir}/slide_{i+1}.png" for i in range(len(slide_texts))]
audio_files = [f"audio_{i+1}.mp3" for i in range(len(slide_texts))]

# セッション状態でスライドのインデックスを管理
if 'slide_index' not in st.session_state:
    st.session_state['slide_index'] = 0

# スライドのインデックスに基づいて画像と音声を表示
slide_index = st.session_state['slide_index']
st.image(slide_images[slide_index], use_column_width=True)

# 音声の再生ボタン
if st.button("音声再生"):
    st.audio(audio_files[slide_index])

# 次のスライドへ進むボタン
if st.button("次のスライド"):
    if slide_index < len(slide_images) - 1:
        st.session_state['slide_index'] += 1

