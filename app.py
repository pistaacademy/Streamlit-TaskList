import streamlit as st
from post_page import run_task_page
from manage_page import run_manage_page

def main():
    st.title("Simple CRUD Task List App")

    menu = ["Home", "Task", "Manage", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Task":
        st.subheader("Post&Update Task")
        run_task_page()
    elif choice == "Manage":
        st.subheader("Manage Task")
        run_manage_page()
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()