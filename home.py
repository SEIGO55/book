import streamlit as st
from PIL import Image
import os

# スライド画像を保存するディレクトリを指定
output_dir = "./slides"
# スライド画像をリストとして読み込み
slide_images = [f"{output_dir}/slide_{i+1}.png" for i in range(3)]  # 3はスライドの枚数に応じて変更

# 各画像が存在するかを確認し、Pillowで読み込み
loaded_images = []
for image_path in slide_images:
    if os.path.exists(image_path):
        img = Image.open(image_path)
        loaded_images.append(img)
    else:
        st.write(f"Image not found: {image_path}")

# 読み込んだ画像を表示
if loaded_images:
    st.image(loaded_images[0], use_column_width=True)
else:
    st.write("No images were loaded.")

