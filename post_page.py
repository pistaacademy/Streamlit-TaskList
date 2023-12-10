import streamlit as st

from db_fxns import create_table, add_data, view_all_tasks,view_all_task_names,get_task_by_task_name

def run_task_page():
    create_table()
    submenu = st.sidebar.selectbox("SubMenu",['Add Task', 'Edit Task'])

    col1, col2 = st.columns(2)

    if submenu == 'Add Task':
        st.subheader("Add Task")
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

    elif submenu == 'Edit Task':

        st.subheader("Update/Edit Task")

        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Task", list_of_tasks)
        task_result = get_task_by_task_name(selected_task)

        if task_result:
            task_doer = task_result[0][0]
            task_name = task_result[0][1]
            task_status = task_result[0][2]
            task_due_date = task_result[0][1]

            col1, col2 = st.columns(2)
            with col1:
                new_task_doer = st.text_input("Task Doer",task_doer)
                new_task_name = st.text_area("Task",task_name)
            with col2:
                new_task_status = st.text_input("Status",task_status)
                new_task_due_date = st.date_input(task_due_date)
    
            if st.button("Update Task"):
                st.success("Added:: {}".format(task_name))
