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


