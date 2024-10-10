import streamlit as st
import re

# サンプルテキスト
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

3.2 例題データ・目的の説明[書式2:  節タイトル]
次に本書で取り上げる例題データと分析の目的の説明をしたいと思います。[書式4:  文]

3.2.1   例題データの説明[書式3:  項タイトル]
まずは例題データの説明です。[書式4:  文]

3.2.2   モデルの目的[書式3:  項タイトル]
次にモデルの目的です。[書式4:  文]

3.2.3   [書式3:  項タイトル]
次にモデルの目的です。[書式4:  文]
実行コードは以下の通りです。[書式4:  文]

import pandas as pd  [書式6:  コード入力]
print(df)  [書式6:  コード入力]

xxxxxxxxxxxxxxx  [書式7:  出力結果]
'''

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


