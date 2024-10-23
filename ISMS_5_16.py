import streamlit as st

def display_page():
    # ページタイトル
    st.title("5.16 識別情報の管理")

    # 1. アイデンティティ管理の目的
    st.subheader("1. 識別情報の管理の目的")
    st.write("""
    識別情報の管理は、組織の情報および関連資産にアクセスする個人やシステムを認識し、検証するプロセスです。
    その目的は、個人の識別情報に基づいて適切なアクセス権を付与することです。
    """)

    # 2. アイデンティティの一貫性と責任
    st.subheader("2. 識別情報の管理の一貫性と責任")
    with st.expander("詳細を表示"):
        st.write("""
        識別情報管理プロセスでは、各個人に割り当てられた識別情報が一人の個人にのみリンクされることを保証し、行動の責任追及が可能になるようにします。
        共有識別情報は、ビジネスや運用上必要な場合にのみ許可され、承認および文書化される必要があります。
        """)

    # 3. 非人的エンティティのアイデンティティ管理
    st.subheader("3. 非人的エンティティのアイデンティティ管理")
    with st.expander("詳細を表示"):
        st.write("""
        非人的エンティティに対するアイデンティティは、分離された承認と独立した監督が必要です。また、アイデンティティが不要になった場合には迅速に削除または無効化される必要があります。同じコンテキスト内での重複するアイデンティティは避けるべきです。
        """)

    # 4. 重要なイベントの記録
    st.subheader("4. 重要なイベントの記録")
    with st.expander("詳細を表示"):
        st.write("""
        ユーザーアイデンティティおよび認証情報に関連する重要なイベントは記録される必要があります。これにより、アイデンティティ管理の透明性と追跡可能性が確保されます。
        """)

    # 5. アイデンティティ変更の管理
    st.subheader("5. アイデンティティ変更の管理")
    with st.expander("詳細を表示"):
        st.write("""
        組織は、ユーザーアイデンティティに関連する変更を管理するプロセスを持つ必要があります。これには、信頼された文書の再確認などが含まれます。
        """)

    # 6. 第三者のアイデンティティ管理
    st.subheader("6. 第三者のアイデンティティ管理")
    with st.expander("詳細を表示"):
        st.write("""
        ソーシャルメディアの資格情報など第三者のアイデンティティを使用する場合、組織はそのアイデンティティが必要な信頼レベルを提供することを保証し、適切な管理策によって関連するリスクを管理する必要があります。
        """)
    # 折りたたみセクションの作成
    with st.expander("実施手順（例）"):
        st.markdown("""
a.情報システムの利用者登録およ び登録削除は、当該利用者の属する部門長が申請し、情報システム管理者の承認を得る。

b.利用者登録は業務上必要な範囲で従業者に付与する。
        """)
    
    # ワンポイントアドバイスのセクション
    with st.expander("ワンポイントアドバイス"):
        st.write("""
        識別情報が不要になった場合、識別情報は時機を失せずに無効化または削除することが大切です。
        """)
# 関数を呼び出してページを表示
display_page()