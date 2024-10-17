# -------- 初期化部分 --------
import streamlit as st
import pandas as pd
import random

# -------- タイトル部分 --------
## タイトルを表示
st.title('Training Site')

# -------- タイトル部分 --------
# Horizontal line before title
st.markdown("---")

# Title
st.markdown("""
<h1 style='font-size:18px;'>J.1.1 組織の状況及びその状況の理解 (4.1) </h1>
""", unsafe_allow_html=True)

# Collapsible section for main content
with st.expander("詳細を表示"):
    # Main content text
    st.markdown("""
    **事業の実施状況を踏まえて、適切なPMSの構築・運用に影響を与える可能性のある外部および内部の課題を特定することを求めるもの。**
    """)

    st.markdown("""
<h2 style='font-size:18px;'>■ 実施のポイント</h2>
""", unsafe_allow_html=True)
    
    # Bullet points
    st.markdown("""
    ◇ 本項は、J1.14 個人情報保護マネジメントシステムの適用範囲の決定、J.3.1.2 リスク及び機会に対処する活動、J.6.3 マネジメントレビュー等を実施する際に必要となる考え方。<br>
    ◇ 課題の特定は、PMSに影響を与える可能性のある課題の中から、<span style="color:red;">事業者にとってできるだけ重要なものが漏れないように継続的に行われていればよい。</span><br>
    ◇ もし外部または内部の内容が変わる可能性がある場合は、適宜見直すことが望ましい。<br>
    """, unsafe_allow_html=True)
    
    # Custom styled info box using st.markdown
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px; border-left: 5px solid #2196f3;">
        <div style="font-size:18px;">
            【構築・運用計画改定による変更点】<br>
            ● <span style="color:red;">指導項目の修正</span>（「課題の把握」「外部及び内部の課題を特定すること」）<br>
            ⇒指針の項目No.10の表現に合わせたもので、実務内容に変更はない
        </div>
    </div>
    """, unsafe_allow_html=True)

# Horizontal line before table
st.markdown("---")

# -------- 初期化部分 --------
import streamlit as st
import pandas as pd
import random

# -------- タイトル部分 --------
## タイトルを表示
st.title('Training Site')

# -------- タイトル部分 --------
# Horizontal line before title
st.markdown("---")

# Title
st.markdown("""
<h1 style='font-size:18px;'>J.1.1 組織の状況及びその状況の理解 (4.1) </h1>
""", unsafe_allow_html=True)

# Collapsible section for main content
with st.expander("詳細を表示"):
    # Main content text
    st.markdown("""
    **事業の実施状況を踏まえて、適切なPMSの構築・運用に影響を与える可能性のある外部および内部の課題を特定することを求めるもの。**
    """)

    st.markdown("""
<h2 style='font-size:18px;'>■ 実施のポイント</h2>
""", unsafe_allow_html=True)
    
    # Bullet points
    st.markdown("""
    ◇ 本項は、J1.14 個人情報保護マネジメントシステムの適用範囲の決定、J.3.1.2 リスク及び機会に対処する活動、J.6.3 マネジメントレビュー等を実施する際に必要となる考え方。<br>
    ◇ 課題の特定は、PMSに影響を与える可能性のある課題の中から、<span style="color:red;">事業者にとってできるだけ重要なものが漏れないように継続的に行われていればよい。</span><br>
    ◇ もし外部または内部の内容が変わる可能性がある場合は、適宜見直すことが望ましい。<br>
    """, unsafe_allow_html=True)
    
    # Custom styled info box using st.markdown
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px; border-left: 5px solid #2196f3;">
        <div style="font-size:18px;">
            【構築・運用計画改定による変更点】<br>
            ● <span style="color:red;">指導項目の修正</span>（「課題の把握」「外部及び内部の課題を特定すること」）<br>
            ⇒指針の項目No.10の表現に合わせたもので、実務内容に変更はない
        </div>
    </div>
    """, unsafe_allow_html=True)

# Horizontal line before table
st.markdown("---")
