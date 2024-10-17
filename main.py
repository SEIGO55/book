import streamlit as st
import plotly.graph_objects as go

# PIE理論の円グラフを描画する関数
def plot_pie_chart():
    # PIE理論のデータ
    labels = ['パフォーマンス (10%)', 'イメージ (30%)', '露出 (60%)']
    sizes = [10, 30, 60]

    # Plotlyを使った円グラフ
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
    fig.update_layout(title_text="ハーヴィー・コールマンのPIE理論", margin=dict(t=0, b=0, l=0, r=0))
    return fig

# Streamlitレイアウト: 1列目に円グラフ、2列目に説明を追加
st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 10px;'>ハーヴィー・コールマンのPIE理論</h1>
""", unsafe_allow_html=True)

# 折りたたみセクションで詳細を表示
with st.expander("詳細を表示"):
    # 2カラムレイアウトを作成
    col1, col2 = st.columns([1, 1])  # カラム幅を均等に調整
    
    # 左側に円グラフを表示
    with col1:
        st.plotly_chart(plot_pie_chart(), use_container_width=True)  # グラフの幅をカラムいっぱいに
    
    # 右側に説明を表示
    with col2:
        st.subheader("説明")
        st.markdown("""
        <p style="font-size:12px; line-height:1.5; margin-top: 5px; margin-bottom: 5px;">
        <strong>パフォーマンス: 成功の基盤 (10%)</strong><br>
        - パフォーマンスはキャリアの進展において重要であり、全体の10%を占めています。<br>
        - 仕事をうまくこなすことは必要ですが、それだけでは成長の限界があります。<br><br>
        <strong>イメージ: 認識が力 (30%)</strong><br>
        - 他者からの認識がキャリアの成長に30%影響します。<br>
        - ポジティブでプロフェッショナルなイメージを築くことが大切です。<br><br>
        <strong>露出: 能力の発揮 (60%)</strong><br>
        - 露出はキャリア進展の60%を占めています。<br>
        - 自分の能力を示し、適切な人々に見てもらうことが成功の鍵です。
        </p>
        """, unsafe_allow_html=True)

    # カスタムスタイルの情報ボックス
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 10px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        「PIEの法則」は、キャリアを成功させるために重要な3つの要素を表すフレームワークで、
        特に外資系企業やビジネス界での出世や成功において強調されることがあります。
        この法則は以下の3つの要素から成り立っています：<br><br>
        <strong>P</strong> (Performance) - 業績、パフォーマンス
        自分の仕事の成果や、仕事での達成度を意味します。どれだけ良い結果を出し、貢献しているかが重要視されますが、これは出世においては全体の一部に過ぎません。<br><br>
        <strong>I</strong> (Image) - イメージ、印象
        自分が周りからどう見られているか、どのような印象を与えているかがポイントです。プロフェッショナリズム、リーダーシップ、信頼性、自己ブランドの確立が含まれます。<br><br>
        <strong>E</strong> (Exposure) - 露出、知名度
        どれだけ多くの人に自分の存在を知ってもらっているか、また自分の業績やスキルがどれだけ広く認識されているかを示します。適切な人々とのネットワーク作りや、
        重要なプロジェクトに関与することなどがこれに含まれます。<br><br>
        このPIEの法則において、最も重視されるのは「Exposure（露出）」です。どれだけ優れたパフォーマンスを発揮しても、
        それが周りに認知されなければ、出世や昇進に繋がらないことが多いためです。
        PIEの法則は、自己ブランディングとネットワーキングの重要性を説いており、特に外資系企業では単に仕事をこなすだけではなく、
        自分の存在を効果的に周囲にアピールし、適切な人脈を築くことが求められます。
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")


