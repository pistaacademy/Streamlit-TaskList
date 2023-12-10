import streamlit as st

from db_fxns import create_table, add_data, view_all_tasks

def run_task_page():
    st.subheader("Post and Update Task")
    create_table()
    col1, col2 = st.columns(2)

    with col1:
        task_doer = st.text_input("Task Doer")
        task_name = st.text_area("Task")
    with col2:
        task_status = st.selectbox("Status",["ToDo", "Done", "Doing", "uncertain"])
        task_due_date = st.date_input("Task Due Date")
    
    if st.button("Add Task"):
        add_data(task_doer, task_name, task_status, task_due_date)
        st.success("Added:: {}".format(task_name))

    results = view_all_tasks()
    st.write(results)