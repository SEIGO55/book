import streamlit as st

def display_page():
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        <h1 style='font-size:18px; margin-bottom: 5px;'>7.1 物理的セキュリティ境界（Physical Security Parameters）</h1>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>1. 管理策 7.1 の概要</summary>
          <p>
          管理策 7.1は「物理的セキュリティ境界（Physical Security Parameters）」に関するもので、附属書Aの物理的セキュリティ管理策に属します。
        　この管理策の目的は、情報を含むエリアを保護するためにセキュリティ境界を定義し、無許可の人が侵入するのを防ぎ、情報や関連する資産が損傷や改ざんを受けないようにすることです。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>2. セキュリティ境界とセキュアエリアの違い</summary>
          <p>
          <strong>セキュリティ境界</strong><br>
            セキュリティ境界は、セキュアエリアと非セキュアまたはセキュリティが低いエリアを区別するための境界です。この境界はアクセスを管理し、機密情報や資産を保護するために設けられます。
            <br><br>
            <strong>セキュアエリア</strong><br>
            セキュアエリアは、情報や資産を保護するために特定のセキュリティ対策が実施されている環境を指します。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>3. セキュリティ境界とセキュアエリアの実例</summary>
          <p>
          セキュリティ境界は建物の周りにあるフェンスや、部屋を分ける壁のような外側の保護シェルのようなもので、セキュリティ境界内には重要で機密性の高い情報や資産を保管するセキュアエリアが設置されています。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>4. セキュアエリアの例とフロアプランの活用</summary>
          <p>
          オフィスビルのフロアプランを例に挙げ、4つのセキュアエリア（緑、黄、オレンジ、赤）を設定します。
            <ul>
              <li><strong>緑エリア:</strong> 最も重要度が低く、建物の外の公共エリアに相当します。このエリアは組織の管理が行き届かず、外部の人々や通行人が自由に出入りできます。</li>
              <li><strong>黄エリア:</strong> 建物の内部に位置し、緑エリアよりもセキュリティ要件が少し高くなります。ここではドアを通過してセキュリティ境界内に入る必要があります。</li>
              <li><strong>オレンジエリア:</strong> 建物内のオフィスエリアやその他のセキュアエリアで、より高い保護が求められます。</li>
              <li><strong>赤エリア:</strong> データセンター、アーカイブ、CEOオフィスなどの最も高い保護が必要なエリアです。このエリアには、より厳格で包括的なセキュリティ対策が施され、アクセスが難しくなっています。</li>
            </ul>
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>5. セキュリティ境界の定義と実装</summary>
          <p>
          この標準の目的は、建物のために必要なセキュアエリアを定義し、それぞれのセキュアエリアをどのように区別するかのパラメーターを設定することです。フロアプランを使用して、公共エリアからデータセンターやサーバールームのような機密性が高くアクセスが制限されたエリアまで、必要な場所をハイライトし、適切なセキュリティ基準を設けることが推奨されます。
          </p>
        </details>
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


