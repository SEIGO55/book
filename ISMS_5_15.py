import streamlit as st

def display_page():
    st.markdown("""
    <h1 style='font-size:18px; margin-bottom: 5px;'>5.15 アクセス制御</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <details>
      <summary>詳細を表示　アクセス制御</summary>
      <p><strong>アクセス制御</strong></p>

      <details>
        <summary>1. アクセス制御の重要性</summary>
        <p>アクセス制御は、情報セキュリティの重要な要素であり、認可されたアクセスを確保し、不正なアクセスから情報および関連資産を保護する役割を果たします。アクセス制御に関連する情報セキュリティおよびビジネスの要件を特定するためには、情報および資産の所有者がトピック別のポリシーを定義する必要があります。</p>
      </details>

      <details>
        <summary>2. アクセス制御ポリシーの要点</summary>
        <p>どのエンティティ（人、機械、デバイス、サービス）がどの種類のアクセスを必要とするかを決定します。また、アプリケーションのセキュリティ、物理的アクセスを適切な出入り管理でサポートし、情報の拡散、権限のあるアクセスへの制限、職務の分離、データまたはサービスへのアクセス制限に関する法的、規制上および契約上の義務を考慮します。</p>
      </details>

      <details>
        <summary>3. アクセス制御機能の分離と管理</summary>
        <p>ポリシーには、アクセス制御機能の分離、アクセス要求の正式な承認、アクセス権の管理、そしてログの記録に関する指針が含まれるべきです。</p>
      </details>

      <details>
        <summary>4. アクセス権と制限の実装</summary>
        <p>アクセス制御ルールを実装するためには、適切なアクセス権と制限を人間のユーザー、機械、デバイス、サービスなどの関連エンティティに定義し、対応付ける必要があります。また、アクセス制御の管理を簡素化するために、特定の役割をエンティティグループに割り当てることも有効です。</p>
      </details>

      <details>
        <summary>5. アクセス制御ルールの整合性と要素の考慮</summary>
        <p>アクセス制御ルールを定義・実装する際には、以下の点を考慮することが重要です。</p>
        <ul>
          <li>アクセス権と情報の分類の一貫性</li>
          <li>アクセス権と物理的な境界の一貫性</li>
          <li>セキュリティの必要性と要件</li>
          <li>利用可能な接続の種類と分散環境</li>
          <li>動的なアクセス制御に関する関連する要素や要因</li>
        </ul>
      </details>

      <details>
        <summary>6. 適切なポリシーの策定による効果</summary>
        <p>これらの要素を考慮し、適切なポリシーを定義することで、エンティティは情報および関連資産に対して認可されたアクセスを確保し、不正なアクセスを防止することができます。</p>
      </details>

    </details>
    """, unsafe_allow_html=True)

# ページ表示の関数を呼び出す
display_page()
