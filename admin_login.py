import streamlit as st

def admin_login():
    st.title("🔐 Admin Login")

    username = st.text_input("Admin Username")
    password = st.text_input("Admin Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state["admin_logged_in"] = True
            st.success("Admin Login Successful!")
        else:
            st.error("Invalid Username or Password")

    return st.session_state.get("admin_logged_in", False)