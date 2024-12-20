import streamlit as st

def display_page():
    st.markdown("""
    <h1 style='font-size:18px; margin-bottom: 5px;'>5.12 情報の分類</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <details>
      <summary>詳細を表示　5.12 情報の分類</summary>
      <p><strong>5.12 情報の分類</strong></p>
      <details>
        <summary>1. 管理策の概要</summary>
        <p>管理策 5.12は、情報を機密性、完全性、可用性、および関連する利害関係者の要求に基づいて分類することを求めています。</p>
      </details>
      <details>
        <summary>2. 情報の分類の目的</summary>
        <p>情報には機密性の異なるものがあり、より高いレベルの保護が必要な情報とそうでない情報があります。組織は情報分類の具体的なポリシーを策定し、関連する利害関係者に伝達する必要があります。</p>
      </details>
      <details>
        <summary>3. 情報分類の例</summary>
        <p>情報分類の概念を説明するため、アメリカ政府の分類制度を例に挙げます。アメリカ政府は情報を「機密情報（classified）」と「非機密情報（unclassified）」に分け、機密情報はさらに「機密（confidential）」、「秘密（secret）」、「極秘（top secret）」に分類されています。</p>
      </details>
      <details>
        <summary>4. 一貫性と他の資産の分類</summary>
        <p>分類制度は組織全体で一貫して使用される必要があります。情報以外の資産も、その中に保存されている情報の分類に従って分類されるべきです。</p>
      </details>
      <details>
        <summary>5. 情報分類ポリシーの作成</summary>
        <p>情報分類ポリシーのテンプレートを使用して、組織に合わせた情報分類ポリシーを作成し、編集することができます。このテンプレートは、ISO 27001標準および情報セキュリティのベストプラクティスに基づいています。</p>
      </details>
      <details>
        <summary>6. ポリシーの構成</summary>
        <p>情報分類ポリシー文書には、目的、範囲、用語と定義、関連文書、ポリシー、コンプライアンスの6つのセクションがあります。各セクションには簡単な説明とサンプルテキストが含まれており、必要に応じて編集可能です。</p>
      </details>
      <details>
        <summary>7. 情報分類スキームの例</summary>
        <p>情報分類スキームには、「公開（public）」、「内部（internal）」、「機密（confidential）」、「秘密（secret）」の分類レベルが含まれます。組織に合わせて分類名や基準を変更することが可能です。</p>
      </details>
      <details>
        <summary>8. テンプレートのカスタマイズと活用</summary>
        <p>テンプレートをダウンロードし、組織名や情報分類レベルなどを埋めて編集します。フォーマットも自由にカスタマイズして、よりプロフェッショナルで組織に適した文書に仕上げることが重要です。</p>
      </details>
    </details>
    """, unsafe_allow_html=True)

    # 折りたたみセクションの作成
    with st.expander("実施手順（例）"):
        st.write("""
        情報は一般・社外秘・関係者外秘で分類する。
        情報セキュリティ委員会は、情報の分類を最低年1回見直す。
        """)
    
        # 情報分類の表をMarkdownで記述
        st.markdown("""
        | 分類     | 内容                                                                                     |
        |----------|------------------------------------------------------------------------------------------|
        | 一般     | 下記以外                                                                                 |
        | 社外秘   | 関係者外秘以外の機密事項であり、組織の従業者に対してのみ開示が許されるもの。（取引先に開示する必要があるものは除く。）または情報セキュリティに関わる規定・手順書。 |
        | 関係者外秘 | 情報が外部に漏れることによって、当組織が重大な損失もしくは不利益を受ける恐れがあるもの。業務提携先に対してのみ開示が許される機密事項などを含む。関係者が明示的に定められていない場合、関係者とは、情報を正確に知る権利を有する者を指す。 |
        """)
    
    # ワンポイントアドバイスのセクション
    with st.expander("ワンポイントアドバイス"):
        st.write("""
        分類は、情報の侵害が組織に与える影響のレベルによって決定できます。分類体系で定義されたレベルには、分類体系の適用において意味をなすような名称を付けることが大切です。
        """)

display_page()
