import streamlit as st

def run_task_page():
    st.subheader("Post and Update Task")

    col1, col2 = st.columns(2)

    with col1:
        task_doer = st.text_input("Task Doer")
        task_name = st.text_area("Task")
    with col2:
        task_status = st.selectbox("Status",["ToDo", "Done", "Doing", "uncertain"])
        task_due_date = st.date_input("Task Due Date")
    
    if st.button("Add Task"):
        st.success("Added:: {}".format(task_name))