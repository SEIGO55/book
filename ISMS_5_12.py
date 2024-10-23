import streamlit as st

def display_page():
    st.markdown("""
    <h1 style='font-size:18px; margin-bottom: 5px;'>8. 情報セキュリティ管理策</h1>
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

display_page()
