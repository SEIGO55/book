import streamlit as st
import re
from other_script import get_additional_text  # 他のファイルから関数をインポート

# 既存のテキスト
text = '''
3章 機械学習モデルの開発手順 [書式1:  章タイトル]
3章ではいよいよモデルの開発手順について説明していきたいと思います。

3.1 モデルの開発フロー [書式2:  節タイトル]
モデルの開発フローについて説明します。Pythonでモデルを開発するフローは図1の通りです。 [書式4:  文]
(1)データの読み込み[書式5:  文中の項目]
まずはデータの読み込みが必要です。[書式4:  文]
(2)データの確認[書式5:  文中の項目]
次にデータの確認を行います。[書式4:  文]
(3)モデル構築[書式5:  文中の項目]
最後に予測モデルを構築します。[書式4:  文]
'''

# テキストを解析して表示する関数
def parse_and_display_text(text):
    # テキストを改行で分割
    lines = text.strip().split('\n')
    
    for line in lines:
        # 空行をスキップ
        if not line.strip():
            continue
        
        # 書式を検出
        match = re.search(r'\[書式(\d+):.*\]', line)
        if match:
            format_type = int(match.group(1))
            content = re.sub(r'\[書式\d+:.*\]', '', line).strip()
            
            if format_type == 1:
                st.header(content)
            elif format_type == 2:
                st.subheader(content)
            elif format_type == 3:
                st.markdown(f'### {content}')
            elif format_type == 4:
                st.write(content)
            elif format_type == 5:
                st.write(f'**{content}**')
            elif format_type == 6:
                st.code(content, language='python')
            elif format_type == 7:
                st.text(content)
        else:
            # 書式指定がない行はそのまま表示
            st.write(line)

# 既存のテキストを解析して表示
parse_and_display_text(text)

# 他のPythonファイルから追加のテキストを取得
additional_text = get_additional_text()

# 追加のテキストを解析して表示
parse_and_display_text(additional_text)
