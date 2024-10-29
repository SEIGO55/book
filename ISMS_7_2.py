import streamlit as st

def display_page():
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        <h1 style='font-size:18px; margin-bottom: 5px;'>管理策 7.2 物理的な入室管理</h1>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>1. 管理策 7.2 の概要</summary>
          <p>
          管理策 7.2は「物理的な入室管理」に関するもので、附属書Aの物理的管理策に属します。
          この管理策では、適切な入室管理とアクセスポイントの設定を求めています。
          目的は、無許可の人がセキュリティ境界を越えてセキュアエリアに侵入するのを防ぐことです。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>2. 入室管理の実施方法</summary>
          <p><strong>認可された人員のみのアクセス</strong></p>
          <p>アクセスカード、バイオメトリクス、カードとPINを組み合わせた二要素認証などのツールを使用して、認可された人員のみがアクセスできるようにします。
          定期的にアクセス権を確認し、必要に応じて更新するプロセスを確立します。</p>
          <p><strong>ログと監査記録の保持</strong></p>
          <p>施設に誰が出入りしたかを記録するため、ログブックや電子監査記録を維持します。これにより、アクセスの追跡や機密認証情報の保護が可能になります。</p>
          <p><strong>追加のセキュリティ対策</strong></p>
          <p>機密情報が含まれるエリアには、二重扉や玄関ホールなどの追加対策が必要になる場合があります。ただし、これはリスクに基づいて決定するため、必須ではありません。</p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>3. 受付と訪問者管理</summary>
          <p><strong>受付エリアの監視</strong></p>
          <p>監視された受付エリアは、訪問者が識別・認証され、許可を得るためのコントロールされた入室ポイントとして機能します。特に機密性の高い組織では、スタッフに対しても同様の管理が適用される場合があります。</p>
          <p><strong>身分証の確認と持ち物検査</strong></p>
          <p>身分証（運転免許証や社員証など）を確認し、訪問者の本人確認を行います。また、個人の持ち物を検査することで、無許可の物品が敷地内に持ち込まれるのを防ぎます。</p>
          <p><strong>IDバッジの使用</strong></p>
          <p>すべての職員と訪問者は、識別可能なIDバッジを着用し、従業員、サプライヤー、訪問者でデザインを区別します。これにより、各エリアに誰が属しているか、また不審者や迷子の訪問者を簡単に識別できます。</p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>4. 物理キーとロックコードの管理</summary>
          <p>物理キーとロックコードを管理するプロセスを実施し、キーが安全に保管され、追跡され、定期的に監査されるようにします。</p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>5. 訪問者管理の実践</summary>
          <p><strong>訪問者の身元確認</strong></p>
          <p>訪問者の身元を確認するために、運転免許証や社員証などをチェックします。</p>
          <p><strong>訪問時間の記録</strong></p>
          <p>訪問者の入室・退室時間を記録し、氏名、訪問日時、会う相手を記録します。</p>
          <p><strong>訪問者用バッジの発行</strong></p>
          <p>訪問者には明確に識別されたバッジを発行し、訪問者が組織内でどのエリアにアクセスできるかを管理します。</p>
          <p><strong>アクセス制御と緊急時手順の説明</strong></p>
          <p>訪問者には、必要なエリアにのみアクセスを許可し、セキュリティ要件や立入禁止エリアについて説明します。また、緊急時の手順（出口、集合場所、その他の安全情報）についても説明します。</p>
          <p><strong>訪問者への同行</strong></p>
          <p>必要に応じて、スタッフが訪問者に同行することで、さらなる管理と監督を行い、不正なアクセスを防止します。</p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>6. 配達エリアのセキュリティ</summary>
          <p><strong>配達エリアへのアクセス制限</strong></p>
          <p>配達エリアには、外部からのアクセスを制限し、識別された認可された人員のみが入室できるようにします。</p>
          <p><strong>分離されたエリアでの配達管理</strong></p>
          <p>配達品が建物の他の部分に広がらないよう、配達エリアを分離されたエリアとして設計します。これにより、配達員が他のエリアに迷い込んだり、組織に損害を与えたりすることを防ぎます。</p>
          <p><strong>外部扉のセキュリティ強化</strong></p>
          <p>配達エリアの外部扉、特に制限エリアに繋がる扉が開いている場合は、無許可の侵入を防止するために外部扉のセキュリティを強化します。</p>
          <p><strong>配達物の検査</strong></p>
          <p>脅威に応じて、配達物の検査を行い、爆発物、化学物質、危険物が含まれていないかを確認します。ただし、すべての組織に適用されるわけではありません。</p>
        </details>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        <details>
          <summary style='font-size:16px; font-weight: bold;'>"実施手順（例）"</summary>
          <p>
          XXXX
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>"ワンポイントアドバイス"</summary>
          <p>
          XXXX
          </p>
        </details>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 関数を呼び出してページを表示
display_page()
