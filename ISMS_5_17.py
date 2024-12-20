import streamlit as st

def display_page():
    st.markdown("""
    <h1 style='font-size:18px; margin-bottom: 5px;'>5.17 認証情報管理</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <details>
      <summary>詳細を表示　認証情報管理</summary>
      
      <details>
        <summary>1. ガイダンスの目的</summary>
        <p>このガイダンスの目的は、適切なエンティティ認証を確保し、認証プロセスにおける失敗を防ぐことです。</p>
      </details>

      <details>
        <summary>2. 認証情報の割り当てと管理</summary>
        <p>認証情報の割り当てと管理プロセスでは、登録プロセス中に生成されるパスワードや個人識別番号が一意であり、簡単に解読できないことを保証し、初回使用後には変更を求める必要があります。</p>
      </details>

      <details>
        <summary>3. 認証情報の提供と確認手続き</summary>
        <p>新しい認証情報や一時的な認証情報を提供する前に、ユーザーの身元を確認する手続きが確立されている必要があります。認証情報（特に一時的なもの）は安全に送信され、保護されていない電子メールでは送信しないようにします。</p>
      </details>

      <details>
        <summary>4. 認証情報の受領確認とベンダー情報の変更</summary>
        <p>ユーザーは認証情報の受領を確認する必要があります。ベンダーから提供されたデフォルトの認証情報は、インストール後すぐに変更して機密性を維持する必要があります。</p>
      </details>

      <details>
        <summary>5. 認証情報管理に関する記録</summary>
        <p>認証情報の割り当てと管理に関する重要なイベントの記録は機密扱いとし、承認されたパスワードボールトツールを使用して管理する必要があります。</p>
      </details>

      <details>
        <summary>6. 認証情報へのアクセス制限</summary>
        <p>認証情報へのアクセスは、認可された人員のみに限定し、ユーザーは認証情報を許可されていない者と共有してはなりません。</p>
      </details>

      <details>
        <summary>7. パスワードの使用と管理</summary>
        <p>パスワードが認証情報として使用される場合、強力なパスワードを選択し、妥協の兆候がある場合はすぐに変更する必要があります。パスワード管理システムは、ユーザーが自分のパスワードを選択・変更できるようにし、初回ログイン時にパスワードの変更を強制し、以前のパスワードの再利用を防止します。</p>
      </details>

      <details>
        <summary>8. パスワードの表示と保護</summary>
        <p>パスワードは入力中に画面に表示されてはならず、保存および送信時には保護される必要があります。パスワードの暗号化とハッシュ化は、承認された暗号技術を使用して行われるべきです。</p>
      </details>

    </details>
    """, unsafe_allow_html=True)
        
    st.markdown("<h2 style='font-size:16px; margin-top: 20px;'>チェックポイント</h2>", unsafe_allow_html=True)
    
    # チェックポイントのチェックボックス
    checkpoint1 = st.checkbox("1. 認証情報に関するポリシーおよび手順が適切に策定され、文書化されていますか？")
    checkpoint2 = st.checkbox("2. 認証情報が適切に割り当てられ、管理されていますか？")
    checkpoint3 = st.checkbox("3. 認証メカニズム(例: 一要素認証、二要素認証、多要素認証）がリスクに応じて適切に選択されていますか？")
    
    # チェックが全て完了したか確認
    if checkpoint1 and checkpoint2 and checkpoint3:
        st.success("すべてのチェックポイントが完了しました。")

# 関数を呼び出してページを表示
display_page()
