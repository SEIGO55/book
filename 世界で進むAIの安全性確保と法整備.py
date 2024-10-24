import streamlit as st

def display_page():
    st.markdown("""
    <h1 style='font-size:18px; margin-bottom: 5px;'>世界で進むAIの安全性確保と法整備</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <details>
      <summary>AIセーフティ・インスティテュート（AISI）の取り組み</summary>
      <p>日本では、AIセーフティ・インスティテュート（AISI）がその中心的な役割を担っています。AISIは、安全で安心なAIの実現に向けて、AIの安全性に関する評価手法や基準の検討・推進を行うために設立された機関です。関係省庁や国内外の関係機関と連携しながら、AI技術の安全性確保に向けて、積極的に活動しています。具体的には、評価手法の標準化やガイドラインの策定を通じて、安全で信頼性のあるAIシステムの開発を促進しています。</p>
      <a href='https://aisi.example.com' target='_blank'>AISIの詳細についてはこちらをご覧ください。</a>
    </details>

    <details>
      <summary>ヨーロッパにおけるAI規制と国際協力</summary>
      <p>ヨーロッパでは、European AI OfficeがEUのAI規制法「AI Act」の実施や、信頼できるAIの開発・利用の促進、国際協力において重要な役割を果たしています。AI Actは特に汎用AI（AGI: Artificial General Intelligence）に対する規制や評価基準の策定を進めており、信頼性のあるAIシステムの構築に向けた取り組みが行われています。これにより、ヨーロッパはAI技術の安全性と倫理性の両立を目指し、国際的な協力の推進にも力を入れています。</p>
      <a href='https://european-ai-office.example.com' target='_blank'>詳細は、European AI Officeをご覧ください。</a>
    </details>

    <details>
      <summary>アメリカ・カリフォルニア州のAI規制の動向</summary>
      <p>AI業界の中心地であるアメリカ、特にシリコンバレーを擁するカリフォルニア州でも、AI規制に向けた法案が進行中です。現在、州議会で審議されている「SB 1047（フロンティアAIモデルの安全とセキュアなイノベーション法）」では、AIのリスクによる危害に対する責任を開発者に負わせる方針が議論されています。この法案はAI業界を二分し、開発者の責任範囲をどこまでとするかについて、最終的な判断が州知事に委ねられています。</p>
      <p>この法案は州法であるにもかかわらず、成立すれば世界中に影響を与える可能性があると注目されています。AI技術の急速な進展に対応しつつ、リスク管理と安全性をどう両立させるかが、今後の大きな課題となっています。</p>
      <a href='https://california-ai-regulation.example.com' target='_blank'>この法案に関する詳細はこちらの記事をご参照ください。</a>
    </details>

    <details>
      <summary>まとめ</summary>
      <p>AI技術の進化は私たちの生活に大きな変革をもたらしますが、その一方でリスク管理や規制の整備が急務です。各国の政府や機関が連携し、安全性や倫理性を確保するための取り組みが進められており、AI技術が社会に与える影響を最小限に抑えるための努力が続いています。AIの未来は、技術の発展だけでなく、それを支える安全基準や倫理的ガイドラインによっても形作られていくでしょう。</p>
    </details>
    """, unsafe_allow_html=True)

# 関数を呼び出してページを表示
display_page()
