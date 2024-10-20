import streamlit as st

def show():
    st.header("1.1　本書の目的")
    st.write("""
    本書は、データサイエンスと機械学習を業務に効果的に活用する方法を解説することを目的としています。
    特に、**Streamlit**を使用してデータサイエンスの成果物をインタラクティブなウェブアプリケーションとして
    共有する手法に焦点を当てています。

    現代のビジネス環境では、データから価値を引き出す能力が競争力の源泉となっています。しかし、
    データサイエンスや機械学習の専門知識を持たない方にとって、その成果を理解し活用することは容易ではありません。
    そこで、本書では以下の点を目指します。
    """)
    
    st.markdown("""
    - **業務課題とデータサイエンスの橋渡し**：ビジネス上の問題をデータサイエンスで解決するためのアプローチを紹介します。
    - **機械学習プロジェクトの実践的な進め方**：プロジェクトの立ち上げからモデルの構築、評価、展開までのステップを具体的に解説します。
    - **Streamlitによる成果の共有**：プログラミングの専門知識がなくても、簡単にデータサイエンスの結果を可視化し、関係者と共有できる方法を提供します。
    """)
    
    st.write("""
    本書を通じて、データサイエンスと機械学習の知識を深めるだけでなく、実際の業務でその力を発揮できるようになることを期待しています。
    """)
