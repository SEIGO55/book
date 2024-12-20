import streamlit as st

def display_page():
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        <h1 style='font-size:18px; margin-bottom: 5px;'>管理策 7.3 オフィス、部屋及び施設のセキュリティ</h1>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>1. 管理策 7.3 の概要</summary>
          <p>
          管理策 7.3は「オフィス、部屋、および施設のセキュリティ」に関するもので、附属書Aの物理的管理策に属します。
          この管理策は、組織の重要な情報や関連資産を物理的に保護するためのセキュリティ対策の策定と実行を目的としています。
          無許可の人物の侵入を防ぎ、資産への潜在的な損害や業務の妨害を防止することが主な目標です。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>2. 重要施設の立地選定（ロケーションの重要性）</summary>
          <p>
          価値ある施設を安全に保護するために、組織は施設を公共エリアから離れた場所に設置します。
          これにより、無許可の人が近づきにくくなり、リスクが軽減されます。具体的には、目立たない場所に設置することで、不正なアクセスの可能性を低くすることが目的です。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>3. 施設の可視性を抑える（目立たない設計）</summary>
          <p>
          施設の外観を目立たないようにデザインすることで、外部からの注目を避けます。
          大きな看板や派手な表示を避け、一般のオフィスビルや倉庫のように見せることで、重要な情報処理が行われていることを知られないようにします。
          これにより、不正行為を目的とした者からの標的化を防ぎます。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>4. 施設内部の配置（プライバシーの確保）</summary>
          <p>
          施設内部の配置も、機密情報の保護を目的として設計します。例えば、窓を高い位置に配置したり、着色ガラスで外から見えないようにする、音漏れ防止のための防音壁や電子的な盗聴を防ぐための電磁シールドを活用するなどの対策を講じます。
          これにより、情報が物理的にも、視覚的・聴覚的にも安全に保たれます。
          </p>
        </details>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>5. 施設情報の管理</summary>
          <p>
          施設の位置や内部情報が公開されないようにします。内部の電話帳やオンライン地図などで機密施設が指摘されると、その機密性が損なわれます。
          大規模なサービスプロバイダーのデータセンターなどでは、場所が非公開にされており、施設名や位置は公式ディレクトリに掲載されないことが多いです。
          このように、必要な人だけがアクセスできるよう情報の管理を徹底します。
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
