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

st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>生成AIにおけるオプトアウトとサニタイズの重要性</h1>
""", unsafe_allow_html=True)

with st.expander("詳細を表示"):
    # オプトアウトのセクション
    st.header("1. オプトアウト")
    st.write("""
    **定義**: ユーザーが、自分のデータが生成AIシステムで利用されることを拒否する権利。
    
    **重要性**: 個人情報が無断で使用されると、プライバシーが侵害されるリスクが高まります。オプトアウトにより、データの透明性と倫理的な使用を確保できます。
    
    **効果**: ユーザーが自分のデータがAIにどのように使用されるかを理解し、拒否する権利を行使することで、情報漏洩やプライバシー侵害のリスクを軽減できます。
    """)
    
    # サニタイズのセクション
    st.header("2. サニタイズ（データサニタイズ）")
    st.write("""
    **定義**: サニタイズは、データから個人を特定できる情報（PII）や機密情報を削除・無効化するプロセスです。
    
    **重要性**: AIの訓練データに個人情報が含まれている場合、そのデータが生成物に影響を与え、権利侵害やプライバシーリスクを引き起こす可能性があります。
    
    **効果**: データを適切にサニタイズすることで、生成AIがプライバシーに配慮したデータを使用し、誤用や漏洩を防ぎます。これにより、AIが出力する情報の信頼性も高まります。
    """)
    
    # まとめのセクション
    st.header("まとめ")
    st.write("""
    オプトアウトは、ユーザーがデータ利用を拒否する権利を行使する仕組みであり、プライバシー保護のために重要です。サニタイズは、AIが使用するデータから個人を特定できる情報を削除し、安全性を確保するプロセスです。これらの手法を導入することで、生成AIに関わるリスクを大幅に軽減し、倫理的かつ安全なAI利用が可能になります。
    """)

    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
情報を消す、情報を抽象化する、そして表現の適正化は、特にデータ保護や生成AIの使用において非常に重要なプロセスです。
これらの要素は、プライバシー保護や情報の正確さを保つために不可欠です。それぞれの役割についてもう少し詳しく見てみましょう。

<strong>1. 情報を消す</strong><br>
重要性: 不必要な個人情報や機密データを削除することは、セキュリティやプライバシー保護において最も基本的な措置です。データが意図せず公開されたり、AIの訓練データとして使われたりするリスクを防ぐために、適切なタイミングで情報を消すことが必要です。
具体例: クレジットカード番号や個人の住所など、不要となった情報を安全に消去することで、悪用や漏洩のリスクを回避します。<br><br>
<strong>2. 情報を抽象化する</strong><br>
重要性: 情報の抽象化は、個人や特定の事象を特定できないようにデータを加工するプロセスです。これにより、情報の本質を保ちながらもプライバシーを守ることができます。AIが個別のデータに基づいてではなく、パターンや傾向に基づいた判断を行うための手法です。
具体例: 個人の詳細な履歴を使用する代わりに、統計的なデータや一般化された情報を使用して分析を行うことで、個人を特定するリスクを減らします。<br><br>
<strong>3. 表現の適正化</strong><br>
重要性: 生成AIがアウトプットする情報の表現が適切であることは、誤解を避け、正確な情報伝達を確保するために必要です。特に、生成された情報が不正確であったり、誤解を招く表現であった場合、利用者や社会に悪影響を与える可能性があります。
具体例: AIが生成するテキストやレポートが誤解を招かないように、分かりやすく、かつ適切なコンテキストで表現されているかを確認・修正するプロセスです。
""", unsafe_allow_html=True)

st.markdown("---")
# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>野良GPT</h1>
""", unsafe_allow_html=True)

with st.expander("詳細を表示"):
    st.markdown("""
「野良GPT」という概念が指すのは、正式な管理や規制を受けていない生成AIモデルのことを意味します。
このようなAIは、正式なプラットフォームや信頼できる組織によって運営されておらず、リスクが多く存在します。具体的には、以下のようなリスクが考えられます。

1. 情報漏洩のリスク
個人情報や機密情報の漏洩: 野良GPTは、適切なセキュリティ対策が取られていない可能性が高く、利用者が入力した個人情報や機密情報が不正に利用されたり、外部に漏洩するリスクがあります。
データ保護の欠如: 信頼できる管理体制がない場合、データ保護規制（GDPRなど）に違反する可能性も高まります。これにより、個人データが不適切に収集・保存されるリスクがあります。
2. 誤情報の生成
精度の低い情報: 野良GPTは、適切に訓練されていなかったり、メンテナンスが不十分である可能性があるため、誤った情報や偏りのあるコンテンツを生成することが考えられます。これにより、誤情報が拡散し、利用者が誤解を招く行動を取るリスクが高まります。
悪意のあるコンテンツ: 生成AIが意図せず攻撃的なコンテンツや有害なメッセージを生成することがあり、それが意図的に拡散される可能性も存在します。
3. 知的財産権侵害のリスク
著作権侵害: 野良GPTが訓練に使用したデータが適切にライセンスされていなかったり、コンテンツ生成において他者の知的財産権を侵害するリスクがあります。このようなモデルを利用すると、著作権や商標権の侵害に巻き込まれる可能性があります。
法的責任の不明確さ: 野良GPTは運営者が不透明であったり、利用規約が不十分なことが多いため、問題が発生した際に誰が責任を負うのかが不明確です。これにより、ユーザーが法的なリスクを負う可能性があります。
4. セキュリティリスク
マルウェアやハッキングのリスク: 野良GPTは、悪意のある攻撃者によって利用される可能性があり、ユーザーがモデルを使用する際にマルウェアが仕込まれたり、データが盗まれるリスクがあります。
サービス停止や不安定性: 野良GPTは、信頼できるインフラを持たないことが多く、突然のサービス停止やデータ消失など、信頼性の欠如が問題となります。
5. 倫理的なリスク
偏見や差別の拡散: 野良GPTは、正式なチェックやフィルタリングが行われないため、学習データに含まれる偏見や差別的な要素がそのまま生成され、社会に悪影響を与える可能性があります。
フェイクニュースの生成と拡散: 野良GPTが誤情報やフェイクニュースを生成し、それが拡散されることで、社会全体に混乱や誤解を招く危険性があります。<br><br>
まとめ
「野良GPT」は、管理が不十分であるため、情報漏洩、誤情報の生成、知的財産権の侵害、セキュリティリスク、倫理的問題といった複数のリスクを抱えています。
こうしたリスクを軽減するためには、信頼できるプラットフォームで管理されたAIモデルを使用し、適切な規制とガイドラインに従うことが重要です。
""", unsafe_allow_html=True)
    st.markdown("---")

st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>参考サイト</h1>
""", unsafe_allow_html=True)

st.markdown("""
1. [経済産業省 AI事業者ガイドライン(1.0版)]
(https://www.meti.go.jp/press/2024/04/20240419004/20240419004.html) （更新日：
2024年4月19日）
""")
from PIL import Image
# 画像を読み込む
image = Image.open("AI事業者ガイドラインの位置づけ.PNG")

# 画像を表示する
st.image(image, caption="AI事業者ガイドラインの位置づけ.jpg", use_column_width=True)

# データを辞書形式で作成
data = {
    "役割": ["AI 開発者（AI Developer）", "AI 提供者（AI Provider）", "AI 利用者（AI Business User）"],
    "説明": [
        "AI システムを開発する事業者。AI モデル・アルゴリズムの開発、データ収集、前処理、AI モデル学習および検証を行う。",
        "AI システムをアプリケーション、製品、ビジネスプロセス等に組み込んでサービスを提供する事業者。AI 利用者への運用サポートも担う。",
        "事業活動において AI システムまたは AI サービスを利用する事業者。適正な利用を行い、AI 提供者と連携しながら運用する。"
    ]
}

# データフレームに変換
df = pd.DataFrame(data)
st.table(df)


st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        AI事業者に向けたガイドラインでは、AI開発者、提供者、利用者が果たすべき役割や責任について説明しています。主な内容を要約すると以下の通りです。

1. AI開発者 (AI Developer)
役割: AIシステムの開発を担当し、モデルの設計、データの収集、前処理、学習、検証などを行う。
目的: AIシステムの基盤構築や入出力機能の実装など、AI全体の開発プロセスに関わる。
2. AI提供者 (AI Provider)
役割: 開発されたAIシステムを製品やサービスに組み込み、ビジネスプロセスやシステムに統合してAI利用者に提供する。
目的: AIシステムの実装、サービス提供、他のシステムとの連携、サポートなどを担い、様々なステークホルダーとのコミュニケーションも必要。
3. AI利用者 (AI Business User)
役割: 事業活動でAIシステムやサービスを利用する企業。提供者と連携し、AIシステムの正常な運用を維持する役割を担う。
目的: 適切なAIの活用を行い、環境変化などの情報を共有しながら運用する。AIが業務外の利用者に影響を与える場合、その影響を最小限に抑えるよう努める。
このガイドラインは、AIの開発・提供・利用における適正な行動やリスク管理を促進し、安全かつ信頼性の高いAIの運用を目指しています。また、AIに伴う社会的リスクへの対策や、AIを利用する事業者が自主的にリスク管理を行うことが強調されています。
        </div>
    </div>
    """, unsafe_allow_html=True)

# データを辞書形式で作成
data = {
    "リスク": [
        "バイアスのある結果や差別的な結果の出力", 
        "フィルターバブル及びエコーチェンバー現象*<sup>1</sup>",  # 注釈を追加
        "多様性の喪失", 
        "不適切な個人情報の取扱い", 
        "生命、身体、財産の侵害", 
        "データ汚染攻撃", 
        "ブラックボックス化、判断に関する説明の要求", 
        "エネルギー使用量及び環境負荷の増加",
        "説明", 
        "機密情報の流出", 
        "ハルシネーション", 
        "偽情報、誤情報を含めること", 
        "操作、認識を誤らせること", 
        "データ権利者との摩擦", 
        "バイアスの再生成"
    ],
    "事例": [
        "IT企業が開発したAI人材採用システムが女性を排除するという報道が話題になった。",
        "SNS等におけるレコメンド機能において社会の分断が起こる。",
        "社会全体で同じモデルを使うと同じ意思決定がなされ、差がなくなる現象が起こる。",
        "退学を覚悟で個人情報が利用及び侵害され問題提起がされている。",
        "AIが自動車を運転することで、誤った認識が引き金となり、命を奪う事件が発生している。",
        "AIの判断に対して意図的な妨害によってデータが汚染される可能性がある。",
        "AIがブラックボックス化し、意思決定理由が説明できない場合があり、透明性が欠けている。",
        "AIの運用には莫大な電力消費が伴っており、環境への影響も大きい。",
        "AIの判断の説明を求める声が高まっている。",
        "AIの利用において、個人や機密情報がプロンプトとして入力され、その内容が流出するリスクがある。",
        "AIが架空の事実を言うこともあり、虚偽を与える「ハルシネーション」に関する問題がある。",
        "AIが生成する情報が誤情報であることによる危険性がある。",
        "AIが人間に過度な影響を与え誤認させることによりリスクが生じる。",
        "生成AIが自らデータ権利者を侵害する可能性がある。",
        "生成AIがバイアスを再生成し、不公平な処理が拡大する可能性がある。"
    ]
}

# データフレームに変換
df = pd.DataFrame(data)

# キャプションを表示
st.markdown("**出典: AI事業者ガイドライン[生成AIの課題]**")

# テーブルを表示
st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

# 注釈を表示
st.markdown("""
フィルターバブル<sup>1</sup>:  
フィルターバブルとは、ネット上のアルゴリズムが個人の興味に基づいた情報のみを表示することで、異なる意見や視点が排除され、情報や価値観が一方的に偏る現象です。これにより、利用者が自己の価値観に閉じ込められる危険性があります。
""", unsafe_allow_html=True)

st.markdown("""
AIと著作権について
""", unsafe_allow_html=True)
st.markdown("""[文化審議会著作権分科会法制度小委員会「AIと著作権に関する考え方について」](https://www.bunka.go.jp/
seisaku/bunkashingikai/chosakuken/pdf/94037901_01.pdf) 更新日：
令和5年6月）""", unsafe_allow_html=True)

st.markdown("""[AI時代の知的財産権検討会「AI時代の知的財産権検討会 中間とりまとめ」](https://www.kantei.go.jp/jp/singi/titeki2/
chitekizaisan2024/0528_ai.pdf) 更新日：
令和6年5月）""", unsafe_allow_html=True)

st.markdown("""
[総務省. (2024). 情報通信白書2024年版. 総務省. 取得先: ](https://www.soumu.go.jp/johotsusintokei/whitepaper/r06.html)更新日：
令和6年5月）""", unsafe_allow_html=True)

#################################################################
st.markdown("---")

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>著作権法</h1>
""", unsafe_allow_html=True)

st.markdown("""
<details>
  <summary>詳細を表示</summary>
  <p><strong>著作権制度の概要</strong></p>
  <details>
    <summary>1. 著作権法の基本的な考え方</summary>
    <p>著作権法第1条（目的）には、著作物の公正な利用に留意しつつ、著作者等の権利の保護を図ることで、新たな創作活動を促し、文化の発展に寄与することが目的とされています。
    そのため、著作権法では、著作者等の権利利益を保護することと、著作物を円滑に利用できること、この両者のバランスを取ることが重要と考えられています。</p>
  </details>
  <details>
    <summary>2. 著作権法が保護する対象</summary>
    <p>著作権法は、著作物を保護するものです。では、著作物とは何でしょうか。
    著作権法では、「思想または感情を創作的に表現したものであって、文芸、学術、美術または音楽の範囲に属するもの」と定義されています。
    この定義から外れる、例えば単なるデータ、事実、ありふれた表現、表現とは言えないアイデアにあたる作風や画風などは、著作権法による保護の対象には含まれません。
    つまり、一つの作品の中でも、著作物性のある部分（著作権で保護される部分）と、著作物性のない部分が存在しているということです。
    アイデアは著作物に当たらず、著作権法上は保護されません。これは、著作権の権利の性質と関係しています。
    著作物に当たる場合、著作権者はその利用を独占できます。その保護期間は、創作されてから著作者の死後70年が経過するまで及びます。
    アイデアを著作権法で保護してしまうと、保護の程度が強すぎ、後発の新たな創作や表現活動を妨げてしまう恐れがあります。
    そのため、アイデアは自由に利用させた方が、創作や表現の多様化・豊富化につながると考えられています。</p>
  </details>
  <details>
    <summary>3. 著作権・著作権者とは</summary>
    <p>著作者とは、「著作物を創作する者」と規定されています。この「創作する者」が誰なのかという点ですが、
    著作物を創作した時点で、著作者は何ら手続きを取らなくても自動的に著作権を取得します。これにより、著作者が著作権者となります。</p>
  </details>
  <details>
    <summary>4. 著作者の権利</summary>
    <p>著作権は、複製や上演、演奏、上映など、著作物の利用形態ごとに権利が定められています。これを「支分権」と言います。
    注意していただきたいのは、著作物を利用する行為すべてが著作権の対象となるわけではないということです。
    著作権は、複製権、上映権など、一定の利用行為に対応する支分権が限定的に規定されており、それ以外の方法で著作物を利用することについては支分権が設けられていません。
    支分権の対象とならない行為、例えば著作物を閲覧したり記憶に残すといった行為には、著作権は及びません。そのため、著作権者の許諾を得ることなく行うことが可能です。
    複数の利用行為がある場合には、それぞれの利用行為ごとに、それが著作権法上どの支分権が及ぶ行為なのか、著作権者の許諾を得る必要があるのかを検討する必要があります。
  </details>
  <details>
    <summary>5.著作権侵害の要件</summary>
    <p>他人の著作物を権利者から許諾を得ず、また権利制限規定に該当しないにもかかわらず利用した場合、これは著作権侵害となります。
    著作権侵害の要件として、裁判例では以下の2つの要件を満たすことが必要とされています：<br><br>
    ●類似性：後発の作品が既存の著作物と同一または類似していること。<br>
    ●依拠性：既存の著作物に依拠して複製等がされたこと。<br><br>
    類似性とは、他人の著作物の表現上の本質的な特徴を直接感得できることが必要です。
    アイデアなど、表現でない部分や創作性がない部分が共通しているだけでは、類似性は否定されます。
    依拠性とは、既存の著作物に接してそれを自己の作品の中に用いることです。
    既存の著作物を知らず、偶然に一致した独自創作の場合、依拠性は認められません。
    </p>
   </details>
   <details>
    <summary>6.著作権侵害に対する措置</summary>
    <p>著作権侵害が認められた場合、民事上の損害賠償請求や差し止め請求が可能です。
                    また、故意による侵害の場合、刑事罰の対象ともなります。</p>
   </details>
   <details>
    <summary>7.権利の制限（許諾を得ず著作物を利用できる場合）</summary>
    <p>著作権法には、公益性の高い利用など一定の場合に、著作物の利用を認める「権利制限規定」が設けられています。
                        これに該当する場合、著作権者の許諾なく著作物を利用可能です。
                        主な権利制限規定として、私的使用のための複製、引用などがあります。</p>
   </details>                     
</details>
""", unsafe_allow_html=True)

# タイトル
st.markdown("""
<h1 style='font-size:18px; margin-bottom: 5px;'>AIと著作権</h1>
""", unsafe_allow_html=True)

st.markdown("""
<details>
  <summary>詳細を表示</summary>
  <p><strong>AIと著作権</strong></p>
  <details>
    <summary>1. AIと著作権についての基本的な考え方</summary>
    <p>準備中</p>
  </details>
  <details>
    <summary>2. ＡＩ開発・学習段階での著作物の利用</summary>
    <p>準備中</p>
  </details>
  <details>
    <summary>3. 法第30条の4導入の経緯</summary>
    <p>準備中</p>
  </details>
  <details>
    <summary>4. ＡＩ開発・学習段階での著作物の利用</summary>
    <p>準備中</p>
  </details>
  <details>
    <summary>5.生成・利用段階での著作物の利用</summary>
    <p>準備中</p>
   </details>
   <details>
    <summary>6.既存著作物の権利者側の対応</summary>
    <p>準備中</p>
   </details>
   <details>
    <summary>7.AI利用者側の対応</summary>
    <p>準備中</p>
   </details>
   <details>
    <summary>8.AI生成物は「著作物」に当たるか</summary>
    <p>準備中</p>
   </details>   
</details>
""", unsafe_allow_html=True)

st.markdown("---")
#################################################################
import bibtexparser

# BibTeX形式の文字列を直接使用
bibtex_str = """
@article{kamoi2024can,
  title={When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},
  author={Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},
  journal={arXiv preprint arXiv:2406.01297},
  year={2024}
}
"""

# BibTeX文字列を解析する関数
def parse_bibtex(bibtex_str):
    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database.entries

# 参考文献を整形して表示する関数
def display_references(bib_entries):
    for entry in bib_entries:
        title = entry.get('title', 'No Title')
        author = entry.get('author', 'No Author')
        year = entry.get('year', 'No Year')
        journal = entry.get('journal', '')
        st.markdown(f"**{title}** ({year})  \n{author}  \n*{journal}*")

# Streamlitのタイトル
st.title("最新論文紹介")

# BibTeXエントリをパース
bib_entries = parse_bibtex(bibtex_str)

# 参考文献の表示
display_references(bib_entries)
st.markdown("""
(https://arxiv.org/pdf/2406.01297)
""", unsafe_allow_html=True)

with st.expander("詳細を表示"):
    st.markdown(
        """
    この文書は、「LLM（大規模言語モデル）はいつ実際に自分自身の誤りを修正できるのか？LLMの自己修正に関する批判的調査」と題された論文で、LLMが自身の回答における誤りをどのように修正できるかについての調査を行っています。以下に主要なポイントを日本語で解説します。
    
    1. 自己修正の概念
    自己修正とは、LLMが自身の初期回答を生成し、その後にフィードバックを用いて回答を改善するプロセスを指します。このプロセスは主に以下の3段階で構成されます：
    
    初期回答生成：LLMが最初の回答を生成します。
    フィードバック生成：LLM自身または外部のツールや知識を用いてフィードバックを生成します。
    回答の改良：生成されたフィードバックを基に、初期回答を修正・改善します。
    2. 主要な研究課題（RQs）
    論文では、LLMが自己修正を効果的に行える条件を明らかにするために、以下の3つの主要な研究課題（Research Questions）が設定されています：
    
    RQ1：LLMは外部のツールやフィードバックなしに、自身の内在的な能力のみで誤りを自己修正できるか？
    RQ2：外部のフィードバック（ツールや知識など）を利用することで、LLMは初期回答をより効果的に自己修正できるか？
    RQ3：自己修正によって得られた最終的な回答は、他の手法（例えば、生成と評価の方法）よりも優れているか？
    3. 主要な発見
    RQ1に関して：外部のフィードバックを用いない自己修正は、特に複雑な推論やコーディングを必要とするタスクでは一般的に困難であることが判明しました。ただし、回答が分解可能で検証が容易なタスク（例：算数問題や閉じた質問応答）では、自己修正の可能性が示されています。
    
    RQ2に関して：信頼性の高い外部フィードバック（例：コードインタープリターや外部知識）を利用することで、自己修正はより効果的に機能することが確認されました。特に、コード生成や証明生成などのタスクで顕著な効果が見られます。
    
    RQ3に関して：大規模なファインチューニング（モデルの微調整）を行うことで、自己修正の能力が向上します。ただし、少量のトレーニングデータでは効果が限定的であることが分かりました。
    
    4. 先行研究の問題点
    多くの先行研究では、研究課題が明確に定義されておらず、実験の設定が不公平または非現実的であるため、自己修正の効果が過大評価されている可能性があります。例えば、正解データ（オラクル情報）をフィードバックとして使用したり、初期回答生成において弱いプロンプトを使用したりすることで、実際の性能よりも高い評価がなされているケースがあります。
    
    5. フレームワークと評価の提案
    論文では、自己修正研究における適切なフレームワークと実験デザインを提案し、今後の研究がより正確に自己修正の能力を評価できるようにするためのチェックリストを提供しています。これには、研究課題を明確に定義し、公平かつ現実的な実験設定を採用することが含まれます。
    
    6. まとめと今後の方向性
    総じて、LLMの自己修正能力は、外部フィードバックや大規模なファインチューニングが存在する場合に限り、特定のタスクで有効であることが示されています。しかし、現時点では自己修正のフィードバック生成がボトルネックとなっており、LLM自身の内在的な能力のみでの効果的な自己修正は限定的です。今後の研究では、フィードバック生成の質を向上させる方法や、より多様なタスクにおける自己修正の可能性を探ることが期待されています。
        """, unsafe_allow_html=True)



#######################################################################################################
# -------- タイトル部分 --------
# Horizontal line before title
st.markdown("---")
# Title
st.markdown("""
<h1 style='font-size:18px;'>J.1.1 組織の状況及びその状況の理解 (4.1) </h1>
""", unsafe_allow_html=True)
#st.markdown("---")
#st.title("概要")

# Collapsible section for main content
with st.expander("詳細を表示"):
    # Main content text
    st.markdown("""
    **事業の実施状況を踏まえて、適切なPMSの構築・運用に影響を与える可能性のある外部および内部の課題を特定することを求めるもの。**
    """)

    # Subheader
    #st.subheader("■実施のポイント")

    st.markdown("""
<h2 style='font-size:18px;'>■ 実施のポイント</h2>
""", unsafe_allow_html=True)
    
    # Bullet points
    st.markdown("""
    ◇ 本項は、J1.14 個人情報保護マネジメントシステムの適用範囲の決定、J.3.1.2 リスク及び機会に対処する活動、J.6.3 マネジメントレビュー等を実施する際に必要となる考え方。<br>
    ◇ 課題の特定は、PMSに影響を与える可能性のある課題の中から、<span style="color:red;">事業者にとってできるだけ重要なものが漏れないように継続的に行われていればよい。</span><br>
    ◇ もし外部または内部の内容が変わる可能性がある場合は、適宜見直すことが望ましい。<br>
    """, unsafe_allow_html=True)

    # # Note or Important Section
    # st.info("""【構築・運用計画改定による変更点】
    # \n● 指導項目の修正（「課題の把握」「外部及び内部の課題を特定すること」）
    # \n● 指針の項目No.10の表現に合わせたもので、実務内容に変更はない
    # """)
    
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

# Horizontal line before table
st.markdown("---")
########################################################################################################################################
#######################################################################################################
# -------- タイトル部分 --------
# Horizontal line before title
st.markdown("---")
# Title
st.markdown("""
<h1 style='font-size:18px;'>個人情報の第三者提供ルールについて </h1>
""", unsafe_allow_html=True)
#st.markdown("---")

# Collapsible section for main content
with st.expander("詳細を表示"):
    # Main content text
    st.markdown("""
    **原則：個人情報取扱事業者は、個人データを第三者に提供する場合、原則としてあらかじめ本人の同意を得なければなりません（法27条1項）。**
    """)
    st.markdown("""
<h2 style='font-size:18px;'>■ 第三者の定義は？</h2>
""", unsafe_allow_html=True)
    st.markdown("""
    「第三者」とは、個人データの保護に関する法律のガイドラインに基づき、
    ①その個人データによって特定される本人、
    ②その個人データを提供しようとする個人情報取扱事業者以外のすべての者を指します（ガイドラインQ&A 7-1）。
    これは、自然人、法人、その他の団体を問いません。

個人データを「第三者」に提供する場合、原則として本人の同意が必要です（通則編GL3-6-1）。以下は「第三者提供」とされる事例ですが、委託、事業承継、または共同利用の場合を除きます：

親会社と子会社、兄弟会社、グループ会社間での個人データの交換
フランチャイズ組織における本部と加盟店間での個人データの交換
同業者間で特定の個人データを交換する場合
一方、「第三者提供」とされない事例としては、同一業者内で他部門へ個人データを提供する場合があります。ただし、この場合でも利用目的に基づく制限が適用されることがあります。
    """)
    st.markdown("""
<h2 style='font-size:18px;'>■ 提供の定義は？</h2>
""", unsafe_allow_html=True)
    st.markdown("""
    提供の定義
「提供」とは、個人データ等を自己以外の者が利用可能な状態に置くことを指します。物理的に個人データが移動していなくても、ネットワーク等を通じてアクセス可能な状態（利用権限が付与されている状態）であれば、「提供」に該当します（通則編GL2-17参照）。

クラウドサービスの利用と「提供」の判断基準
クラウドサービスを利用する際に、これが第三者への「提供」に当たるかどうかは、クラウドサービス提供事業者が個人データを取り扱うか否かが判断基準となります（Q&A7-53）。クラウド事業者が個人データを取り扱う場合には、本人の同意が必要となる可能性があります。

「提供」に該当しない場合
クラウドサービス提供事業者が個人データを取り扱わない場合、個人情報取扱事業者は第三者提供を行ったことにはなりません。そのため、この場合は本人の同意を得る必要はありません（Q&A7-53）。例えば、契約条項において外部事業者がサーバに保存された個人データを取り扱わない旨が定められ、適切なアクセス制御が行われている場合が該当します（Q&A7-53）。
    """)
<h2 style='font-size:18px;'>■ 本人の同意について</h2>
""", unsafe_allow_html=True)
 st.markdown("""
   個人情報取扱事業者は、個人データを第三者に提供する際、原則として本人の同意を事前に取得しなければなりません（法18条1項）。「本人の同意」とは、個人情報が指定された方法で取り扱われることを本人が承諾する意思表示のことであり、本人確認が前提です（通則編GL2-16）。同意を取得する際には、事業の規模や個人データの取扱状況に応じて、本人が判断するために必要な合理的かつ適切な情報を明確に提示する必要があります（通則編GL2-16）。提供先を具体的に明示する必要はありませんが、提供先の範囲や属性を示すことが望ましいとされています（Q&A7-9）。

本人の同意取得方法としては以下のような事例が挙げられます：

口頭での同意意思表示
書面や電磁的記録による同意の受領
メールでの同意の受信
確認欄へのチェック
ホームページ上のボタンのクリック
音声入力やタッチパネル、ボタン、スイッチによる入力
このように、さまざまな手段で本人の同意を取得することが求められています。
 """)
# Horizontal line before table
st.markdown("---")
########################################################################################################################################

