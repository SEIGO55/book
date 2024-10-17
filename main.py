import streamlit as st
import plotly.graph_objects as go

# PIE理論の円グラフを描画する関数
def plot_pie_chart():
    # PIE理論のデータ
    labels = ['パフォーマンス (10%)', 'イメージ (30%)', '露出 (60%)']
    sizes = [10, 30, 60]

    # Plotlyを使った円グラフ
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
    fig.update_layout(title_text="ハーヴィー・コールマンのPIE理論")
    return fig

# Streamlitレイアウト: 1列目に円グラフ、2列目に説明を追加
st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px;'>ハーヴィー・コールマンのPIE理論</h1>
""", unsafe_allow_html=True)

# 折りたたみセクションで詳細を表示
with st.expander("詳細を表示"):
    # 2カラムレイアウトを作成
    col1, col2 = st.columns(2)
    
    # 左側に円グラフを表示
    with col1:
        st.plotly_chart(plot_pie_chart())
    
    # 右側に説明を表示
    with col2:
        st.subheader("説明")
        st.markdown("""
        <p style="font-size:12px;">
        <strong>パフォーマンス: 成功の基盤 (10%)</strong><br>
        - パフォーマンスはキャリアの進展において重要であり、全体の10%を占めています。<br>
        - 仕事をうまくこなすことは必要ですが、それだけでは成長の限界があります。<br>
        <strong>イメージ: 認識が力 (30%)</strong><br>
        - 他者からの認識がキャリアの成長に30%影響します。<br>
        - ポジティブでプロフェッショナルなイメージを築くことが大切です。<br>
        <strong>露出: 能力の発揮 (60%)</strong><br>
        - 露出はキャリア進展の60%を占めています。<br>
        - 自分の能力を示し、適切な人々に見てもらうことが成功の鍵です。
        </p>
        """, unsafe_allow_html=True)
    # Custom styled info box using st.markdown
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px; border-left: 5px solid #2196f3;">
        <div style="font-size:18px;">
            【構築・運用計画改定による変更点】<br>
            ● <span style="color:red;">指導項目の修正</span>（「課題の把握」「外部及び内部の課題を特定すること」）<br>
            ⇒指針の項目No.10の表現に合わせたもので、実務内容に変更はない
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

