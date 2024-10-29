import streamlit as st

def display_page():
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 8px; border-radius: 5px; border-left: 5px solid #2196f3; margin-top: 15px; margin-bottom: 0px;">
        <div style="font-size:12px; line-height:1.5;">
        <h1 style='font-size:18px; margin-bottom: 5px;'>管理策 7.4 物理的セキュリティの監視</h1>
        <details>
          <summary style='font-size:16px; font-weight: bold;'>1. 管理策 7.4 の概要</summary>
          <p>
          管理策 7.4は「物理的セキュリティ監視」に関するもので、物理的管理策に属します。
          この管理策では、組織が物理的な敷地を継続的に監視することが求められています。目的は、敷地内での監視を通じて、怪しい行動を抑止し、検知することです。
          </p>
        </details>
        <details>
           <summary style='font-size:16px; font-weight: bold;'>2. 物理的セキュリティ監視の手法</summary>
          <p>
          物理的な敷地の監視には、ガード、犬、不審者アラーム、CCTV（閉回路テレビ）などの手段が含まれます。
          これらの要素を組み合わせることで、重要なシステムの保護と不正行為の検知が可能になります。
          監視システムは、要塞のように敷地全体を監視し、組織のセキュリティの要として機能します。
          </p>
        </details>
        <details>
          <summary>3. 監視システムの主要要素</summary>
          <p><strong>1. CCTV（閉回路テレビ）</strong></p>
          <p>
          CCTVは、施設内外のアクセスポイントを監視する「目」の役割を果たします。
          門やドアなどの出入口を記録し、セキュリティ侵害や不審な行動の調査に役立ちます。
          ただし、特にヨーロッパではデータ保持の規制が厳しく、敷地外を撮影する場合には注意が必要です。
          </p>
          <p><strong>2. 不審者アラーム</strong></p>
          <p>
          不審者アラームには、接触検出器やモーションセンサー、音響センサーなどがあり、不正な侵入やガラス破損などの際にアラームを鳴らして警告を発します。
          これにより、不審者を抑止し、セキュリティチームに潜在的な脅威を通知します。
          </p>
        </details>
        <details>
          <summary>4. 監視システムの設計とセキュリティ</summary>
          <p>
          監視システムの設計は、内部の人間に限られた秘密情報として扱われるべきです。
          カメラやセンサーの位置が公開されると、不審者がそれらを回避する手がかりとなる可能性があるため、できるだけ隠し、選ばれた人のみが知るようにします。
          </p>
        </details>
        <details>
          <summary>5. 監視システムの保護</summary>
          <p>
          監視システム自体も改ざんや不正アクセスから保護する必要があります。システムのネットワークとハードウェアを保護し、映像の機密性を維持し、リモートで無効化されないようにします。
          アラームシステムのコントロールパネルは、緊急時にアクセス可能でありながら、改ざんから守られるように設計されるべきです。
          </p>
        </details>
        <details>
          <summary>6. プライバシー法とデータ保護規制の遵守</summary>
          <p>
          監視と録画ツールを使用する際には、特に従業員の監視やビデオ保持に関して、プライバシー法やデータ保護規制を遵守することが重要です。
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
