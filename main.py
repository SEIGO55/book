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

import streamlit as st
import matplotlib.pyplot as plt

# Function to plot the pie chart
def plot_pie_chart():
    # Data for the PIE theory
    labels = ['Performance (10%)', 'Image (30%)', 'Exposure (60%)']
    sizes = [10, 30, 60]
    colors = ['#ff9999','#66b3ff','#99ff99']

    # Plotting the pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.set_title("PIE Theory of Career Progress (Harvey Coleman)")
    return fig

# Streamlit layout: one column for the pie chart, one for the explanation
st.title("Harvey Coleman's PIE Theory of Career Progress")

# Creating a 2-column layout
col1, col2 = st.columns(2)

# Display pie chart in the left column
with col1:
    st.pyplot(plot_pie_chart())

# Add explanation in the right column
with col2:
    st.subheader("Explanation")
    st.write("""
    **Performance: The Foundation of Success (10%)**
    - Performance plays a vital role, accounting for 10% of your overall career progress.
    - It ensures you meet expectations and deliver results, but it's just the starting point.

    **Image: Perception is Powerful (30%)**
    - How others perceive you contributes 30% to your career growth.
    - Building a positive image by demonstrating your skills and leadership is key.

    **Exposure: Showcasing Your Abilities (60%)**
    - Exposure accounts for 60% of your career progress.
    - It's essential to showcase your abilities, be seen in action, and build a strong network.
    """)

# Display the app using Streamlit

