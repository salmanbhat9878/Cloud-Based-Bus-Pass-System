import streamlit as st
from database import create_tables, get_connection

st.set_page_config(
    page_title="Cloud Bus Pass System",
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
.stButton > button {
    background-color: #1769aa;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
}
.stButton > button:hover {
    background-color: #0d4778;
    color: white;
}
</style>
""", unsafe_allow_html=True)

create_tables()

st.title("🚌 Cloud-Based Bus Pass System")

st.markdown("""
<div style="background-color:#17365d;padding:20px;border-radius:12px;color:white;text-align:center;">
<h2 style="color:white;">Welcome to Smart Bus Pass Portal</h2>
<p>Register • Apply • Track Your Bus Pass</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Student Registration
with st.container(border=True):
    st.subheader("🎓 Student Registration")
    st.caption("Register your details to apply for a bus pass.")

    with st.form("student_form"):
        name = st.text_input("Student Name")
        roll = st.text_input("Roll Number")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")

        submit = st.form_submit_button("Register Student")

        if submit:
            if name and roll and email and phone:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    "INSERT INTO students (name, roll_number, email, phone) VALUES (?, ?, ?, ?)",
                    (name, roll, email, phone)
                )

                conn.commit()
                conn.close()

                st.success("Student registered successfully!")
            else:
                st.warning("Please fill all fields.")

st.markdown("---")

# Bus Pass Application
with st.container(border=True):
    st.subheader("🚌 Apply for Bus Pass")

    with st.form("bus_pass_form"):
        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        route = st.text_input("Bus Route")

        pass_type = st.selectbox(
            "Pass Type",
            ["Monthly", "Quarterly", "Yearly"]
        )

        apply_pass = st.form_submit_button("Apply for Bus Pass")

        if apply_pass:
            if route:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT id FROM students WHERE id = ?",
                    (student_id,)
                )

                student = cursor.fetchone()

                if student:
                    cursor.execute(
                        "INSERT INTO bus_passes (student_id, route, pass_type) VALUES (?, ?, ?)",
                        (student_id, route, pass_type)
                    )

                    conn.commit()
                    st.success("Bus pass application submitted!")
                else:
                    st.error("Student ID not found.")

                conn.close()
            else:
                st.warning("Please enter a bus route.")

st.markdown("---")

# Bus Pass Status
with st.container(border=True):
    st.subheader("📋 Check Bus Pass Status")

    check_id = st.number_input(
        "Enter Application ID",
        min_value=1,
        step=1,
        key="check_id"
    )

    if st.button("Check Status"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT route, pass_type, status FROM bus_passes WHERE id = ?",
            (check_id,)
        )

        result = cursor.fetchone()
        conn.close()

        if result:
            st.write("Route:", result[0])
            st.write("Pass Type:", result[1])
            st.write("Status:", result[2])
        else:
            st.error("Application not found.")