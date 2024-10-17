import streamlit as st
import plotly.graph_objects as go

# PIE理論の円グラフを描画する関数
def plot_pie_chart():
    # PIE理論のデータ
    labels = ['パフォーマンス (10%)', 'イメージ (30%)', '露出 (60%)']
    sizes = [10, 30, 60]

    # Plotlyを使った円グラフ
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
    
    # グラフのラベルやサイズ、マージンを調整
    fig.update_traces(textposition='outside', textinfo='label+percent', pull=[0, 0, 0.1])  # ラベルを外側に配置
    fig.update_layout(title_text="ハーヴィー・コールマンのPIE理論", margin=dict(t=20, b=20, l=10, r=10), height=350, showlegend=False)  # グラフの高さと余白を調整
    
    return fig

# Streamlitレイアウト
st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>ハーヴィー・コールマンのPIE理論</h1>
""", unsafe_allow_html=True)

# 折りたたみセクションで詳細を表示
with st.expander("詳細を表示"):
    # 上部2カラムレイアウトを作成
    col1, col2 = st.columns([1, 1])  # カラム幅を均等に調整
    
    # 左側に円グラフを表示
    with col1:
        st.plotly_chart(plot_pie_chart(), use_container_width=True)  # グラフの幅をカラムいっぱいに
    
    # 右側に説明を表示
    with col2:
        st.subheader("説明")
        st.markdown("""
        <p style="font-size:12px; line-height:1.5; margin-top: -10px; margin-bottom: 5px;">
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

    # 下部に1カラムレイアウトで情報ボックスを表示
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
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

    st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>参考サイト</h1>
""", unsafe_allow_html=True)
    st.markdown("""
1. [The Networking Institute]
(https://thenetworkinginstitute.com/media/networking/the-pie-theory-performance-image-and-exposure-in-career-progression/) （更新日：
July 21, 2023）
""")
    
    st.markdown("---")


import streamlit as st
import pandas as pd

# Streamlitレイアウト
st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>今までのAIとAGI、ASIとの違い</h1>
""", unsafe_allow_html=True)

with st.expander("詳細を表示"):
    # 説明文
    st.write("""
    従来のAIは、特定のタスクや問題に特化したものであり、一つのプログラムやアルゴリズムで動作しており、限定的な範囲での活動が主でした。
    一方、AGIは汎用的な知能を持つことで複数のタスクに対応できる、人間のような柔軟性を持っています。
    さらにASIは人間の知能をはるかに超えるため、未知のタスクも解決できるようになります。
    """)
    
    # テーブルデータの作成
    data = {
        '': ['従来のAI', 'AGI', 'ASI'],
        'タスクの特化': [
            '画像認識や音声認識など、特定の領域に限定してタスクを実行',
            '複数タスクに対応できる汎用的な能力がある',
            '未知のタスクや複雑な問題も自己進化により解決できる'
        ],
        '学習能力': [
            'あらかじめプログラムされた膨大なデータからルールやパターンを学習',
            'データや経験から学習し、新たな情報を踏まえて適切な判断を行う',
            '自己学習と自己進化が可能で、どんな知識も効率的に獲得し応用する'
        ],
        '柔軟性': [
            'あらかじめ設計された手法に基づいてタスクを実行',
            '新しい問題へのアプローチや解決策を見出すことができる',
            '未知の状況や問題に立ち向かう能力がある'
        ],
        '自己進化': [
            '範囲内でのタスクを実行（自己進化はしない）',
            '経験から学び、新たな情報を取り入れて能力を向上させる（自己進化は限定的）',
            '人間の監督なしに自己改善と自己進化を遂行することができる'
        ]
    }
    
    # データをデータフレームに変換
    df = pd.DataFrame(data)
    
    # テーブルの表示
    st.table(df)

# Streamlitレイアウト
st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>生成AIのリスク</h1>
""", unsafe_allow_html=True)

with st.expander("詳細を表示"):
    # 説明文
    st.write("""
生成AIのリスクは、利用者、提供者、社会全体のそれぞれの立場から異なる視点で発生します。
利用者はプライバシーや誤情報のリスクに直面し、提供者は責任の所在や知的財産問題を考慮する必要があります。
さらに、社会全体としては、デジタル・デバイドの拡大や労働市場への影響、社会的な偏見の再生産が懸念されます。
これらのリスクを適切に管理するためには、技術開発に合わせたガバナンスと教育が求められます。
    """)
# データを辞書で作成
    data = {
        "リスクの種類": ["誤情報", "情報漏洩", "依存とスキル低下", "責任不明確", "権利侵害（知的財産権）", "セキュリティリスク", "偏見強化", "労働市場への影響", "規制の遅れ"],
        "利用者の立場からのリスク": [
            "誤った情報を信じてしまうリスク", 
            "個人情報や機密データの漏洩リスク", 
            "AIへの依存による人間のスキル低下", 
            "-", 
            "-", 
            "-", 
            "偏見や差別的な情報を無意識に受け入れるリスク", 
            "-", 
            "-"
        ],
        "提供者の立場からのリスク": [
            "誤情報に対する法的責任が問われるリスク", 
            "データの不正利用による責任", 
            "-", 
            "有害情報や誤情報の責任が不明確", 
            "AIが他者の著作権を侵害するリスク", 
            "AIシステムがハッキングされるリスク", 
            "バイアスのあるモデル提供リスク", 
            "AIによる業務自動化の影響", 
            "規制の遅れによる対策不足"
        ],
        "社会の立場からのリスク": [
            "社会全体での情報混乱リスク", 
            "プライバシー保護規制の遅れ", 
            "クリエイティブ力の低下リスク", 
            "法的責任の曖昧さ", 
            "著作権問題の社会的影響", 
            "セキュリティ事故による社会的混乱", 
            "社会的偏見や分断の強化", 
            "失業や職業の変化リスク", 
            "法的枠組みが追いつかないリスク"
        ]
    }

    # DataFrameを作成
    df = pd.DataFrame(data)
    
    # Streamlitで表を表示
    st.title("生成AIに関連するリスク一覧")
    st.table(df)
