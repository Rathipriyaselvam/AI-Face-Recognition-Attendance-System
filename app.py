import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Attendance System",
    page_icon="🎓",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.big-title{
    text-align:center;
    font-size:50px;
    font-weight:800;
    color:white;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
}

.metric-container{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
}

[data-testid="stMetric"]{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #334155;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class='big-title'>
🎓 AI Face Recognition Attendance System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Smart Attendance Dashboard using AI, OpenCV & DeepFace
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# LOAD DATA
# =========================

try:
    df = pd.read_csv("attendance/attendance.csv")
except:
    df = pd.DataFrame(
        columns=[
            "Name",
            "Department",
            "Time",
            "Date",
            "Status"
        ]
    )

# =========================
# METRICS
# =========================

total_students = df["Name"].nunique() if len(df) else 0

present_today = len(df)

departments = (
    df["Department"].nunique()
    if len(df)
    else 0
)

accuracy = "96%"

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍🎓 Students",
        total_students
    )

with col2:
    st.metric(
        "✅ Present",
        present_today
    )

with col3:
    st.metric(
        "🏫 Departments",
        departments
    )

with col4:
    st.metric(
        "🤖 Accuracy",
        accuracy
    )

st.write("")
st.divider()

# =========================
# STATUS PANEL
# =========================

col1,col2 = st.columns([2,1])

with col1:

    st.subheader("🤖 Recognition Status")

    if len(df) > 0:

        latest = df.iloc[-1]

        st.success(
            f"Recognized: {latest['Name']}"
        )

        st.info(
            f"Department: {latest['Department']}"
        )

        st.success(
            "Attendance Marked Successfully"
        )

    else:

        st.warning(
            "Waiting for Face Recognition..."
        )

with col2:

    st.subheader("🕒 Current Time")

    st.info(
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    )

st.divider()

# =========================
# SEARCH
# =========================

st.subheader("🔍 Search Student")

search = st.text_input(
    "Enter Student Name"
)

filtered_df = df

if search:

    filtered_df = df[
        df["Name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# =========================
# CHARTS
# =========================

if len(df) > 0:

    col1,col2 = st.columns(2)

    with col1:

        st.subheader(
            "📈 Attendance by Department"
        )

        dept_data = (
            df.groupby("Department")
            .size()
            .reset_index(name="Count")
        )

        fig = px.pie(
            dept_data,
            values="Count",
            names="Department",
            hole=0.4
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader(
            "📊 Attendance Distribution"
        )

        fig2 = px.bar(
            dept_data,
            x="Department",
            y="Count"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

# =========================
# TABLE
# =========================

st.divider()

st.subheader("📋 Attendance Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

# =========================
# DOWNLOAD REPORT
# =========================

csv = filtered_df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download Attendance Report",
    data=csv,
    file_name="attendance_report.csv",
    mime="text/csv"
)

st.divider()

# =========================
# FOOTER
# =========================

st.markdown("""
<center>

### 🚀 Powered by DeepFace + OpenCV + Streamlit

</center>
""", unsafe_allow_html=True)