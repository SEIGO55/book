import streamlit as st

def display_page():
    st.markdown("# Page 2")
    ########################################################################################################################################
    st.markdown(
        """
        <details>
          <summary>詳細を表示　10/22のマナビ</summary>
          <p><strong>10/22のマナビ</strong></p>
          <details>
            <summary>1. ゴールドラッシュ本当に儲けたのは？生成AIブームのチャンスはどこにある？</summary>
            <p>
            タイトル: 「ゴールドラッシュ戦略から見る生成AI時代のビジネス成功術」
            はじめに
            ビジネスの世界では、ゴールドラッシュ戦略という考え方があります。
            これは、金鉱を掘り当てることで一攫千金を狙うのではなく、金を掘り当てようとする人々に必要な道具やサービスを提供することで利益を得る戦略です。
            この戦略は、リーバイス（Levi's）やつるはしやシャベルを作っていた企業がゴールドラッシュ時代に成功した例からも学べます。

            ゴールドラッシュ戦略の成功例
            リーバイス（Levi's） リーバイ・ストラウスは、ゴールドラッシュ時代に採掘労働者のために丈夫なデニムの作業ズボンを開発しました。
            これが現在のジーンズの原型であり、彼のビジネスは世界的な成功を収めました。

            つるはしやシャベルの供給企業 金鉱を掘るために必要な道具や生活必需品を供給する企業もまた、継続的な需要を取り込むことで成功を収めました。
            採掘の成功は不確実でしたが、道具やサービスの需要は常に存在していました。

            現代の「ゴールドラッシュ戦略」: 生成AIのエコシステム
            現代のテクノロジーの世界でも同様の戦略が見られます。
            生成AI（Generative AI）の分野においても、AIそのものを提供する企業だけでなく、AIの開発や利用を支援するインフラやツール、サービスを提供する企業が成功しています。
            以下にいくつかの有望な分野と企業を紹介します。

            クラウドプロバイダー

            Amazon Web Services (AWS)、Microsoft Azure、Google Cloud Platform (GCP) などは、生成AIモデルの訓練や実行に必要なインフラを提供し、企業がAIを利用するための基盤を支えています。
            GPU・ハードウェアメーカー

            NVIDIA や AMD など、高性能なGPUやAIチップを製造する企業は、生成AI市場の成長とともに需要が高まっています。特にNVIDIAは、AIハードウェア市場での影響力が大きいです。
            データセットおよびデータマーケットプレイス

            Scale AI や Figure Eight のような企業がAIモデルのトレーニングに必要なデータセットやデータラベリングサービスを提供し、データ管理の面で収益を上げています。
            AI開発プラットフォームとツール

            Hugging Face のようなプラットフォームは、生成AIモデルを簡単に利用できる環境を提供し、開発者が迅速に製品を開発できるよう支援しています。
            APIおよびソフトウェアプラットフォーム

            OpenAI や Stability AI など、生成AI技術をAPIとして提供する企業が増えています。これにより、他社がAI技術を自社のサービスに組み込むことができ、広範囲にわたる利用が可能になっています。
            セキュリティとコンプライアンスサービス

            生成AIが扱う大量のデータに関するリスク管理を支援する企業（例：BigID、OneTrust）も、セキュリティやプライバシー保護の面で重要な役割を果たしています。
            教育・トレーニングプラットフォーム

            Udacity、Coursera、edX などの教育プラットフォームが生成AI技術を学ぶコースを提供し、スキル習得の面で成長を支援しています。
            カスタムAIソリューション

            AIコンサルティングやカスタムソリューションを提供する企業（例：Accenture AI や C3.ai）は、企業のニーズに合わせて生成AI技術をカスタマイズし、導入を支援することで利益を上げています。
            まとめ
            生成AIのゴールドラッシュにおいて成功するためには、AIそのものを提供するだけでなく、AIのエコシステム全体を支えるインフラやツール、サービスを提供することが重要です。このような戦略は、現代のテクノロジー業界でも多くの成功事例を生んでおり、将来的にもさらなる成長が見込まれます。

            おわりに
            リーバイスがジーンズを開発し、つるはしを売る企業が継続的な需要を取り込んだように、生成AIのエコシステムにおいても、「ツールを売る」戦略が成功の鍵となるでしょう。
            </p>
          </details>
        </details>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

# 関数を呼び出して内容を表示
display_page()


