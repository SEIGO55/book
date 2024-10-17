import streamlit as st
import matplotlib.pyplot as plt

# PIE理論の円グラフを描画する関数
def plot_pie_chart():
    # PIE理論のデータ
    labels = ['パフォーマンス (10%)', 'イメージ (30%)', '露出 (60%)']
    sizes = [10, 30, 60]
    colors = ['#ff9999','#66b3ff','#99ff99']

    # 円グラフを作成
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.set_title("ハーヴィー・コールマンのPIE理論")
    return fig

# Streamlitレイアウト: 1列目に円グラフ、2列目に説明を追加
st.title("ハーヴィー・コールマンのPIE理論")

# 2カラムレイアウトを作成
col1, col2 = st.columns(2)

# 左側に円グラフを表示
with col1:
    st.pyplot(plot_pie_chart())

# 右側に説明を表示
with col2:
    st.subheader("説明")
    st.write("""
    **パフォーマンス: 成功の基盤 (10%)**
    - パフォーマンスはキャリアの進展において重要であり、全体の10%を占めています。
    - 仕事をうまくこなすことは必要ですが、それだけでは成長の限界があります。

    **イメージ: 認識が力 (30%)**
    - 他者からの認識がキャリアの成長に30%影響します。
    - ポジティブでプロフェッショナルなイメージを築くことが大切です。

    **露出: 能力の発揮 (60%)**
    - 露出はキャリア進展の60%を占めています。
    - 自分の能力を示し、適切な人々に見てもらうことが成功の鍵です。
    """)

