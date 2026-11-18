import streamlit as st
import pandas as pd
from database import create_tables, get_connection
from admin_login import admin_login

st.set_page_config(
    page_title="Bus Pass Admin Dashboard",
    page_icon="🚌",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}
h1, h2, h3 {
    color: #17365d;
}
</style>
""", unsafe_allow_html=True)

create_tables()

if not admin_login():
    st.warning("Please login to access Admin Dashboard.")
    st.stop()

st.title("🚌 Bus Pass Admin Dashboard")
st.caption("Manage Student Bus Pass Applications")

if st.button("Logout"):
    st.session_state["admin_logged_in"] = False
    st.rerun()

st.markdown("---")

conn = get_connection()

df = pd.read_sql_query("""
    SELECT
        bus_passes.id AS Application_ID,
        students.name AS Student_Name,
        students.roll_number AS Roll_Number,
        students.email AS Email,
        bus_passes.route AS Route,
        bus_passes.pass_type AS Pass_Type,
        bus_passes.status AS Status
    FROM bus_passes
    JOIN students
    ON bus_passes.student_id = students.id
    ORDER BY bus_passes.id DESC
""", conn)

conn.close()

# Dashboard Metrics
total = len(df)
pending = len(df[df["Status"] == "Pending"])
approved = len(df[df["Status"] == "Approved"])
rejected = len(df[df["Status"] == "Rejected"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Applications", total)
col2.metric("Pending", pending)
col3.metric("Approved", approved)
col4.metric("Rejected", rejected)

st.markdown("---")

# Applications Table
st.subheader("📋 All Bus Pass Applications")

if not df.empty:
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.subheader("⚙️ Manage Applications")

    app_id = st.selectbox(
        "Select Application ID",
        df["Application_ID"].tolist()
    )

    new_status = st.selectbox(
        "Select New Status",
        ["Pending", "Approved", "Rejected"]
    )

    if st.button("Update Application Status"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE bus_passes SET status = ? WHERE id = ?",
            (new_status, app_id)
        )

        conn.commit()
        conn.close()

        st.success("Application status updated successfully!")
        st.rerun()

else:
    st.info("No bus pass applications available yet.")