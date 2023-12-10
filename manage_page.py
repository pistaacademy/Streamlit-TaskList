import streamlit as st

from db_fxns import create_table, add_data, view_all_tasks,view_all_task_names,get_task_by_task_name,edit_task_data,delete_data

import pandas as pd
import plotly.express as px

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def run_manage_page():
    submenu = ["Delete Task", "Analytics"]
    choice = st.sidebar.selectbox("SubMenu", submenu)

    if choice == "Delete Task":
        result = view_all_tasks()
        df = pd.DataFrame(result, columns=['Task Doer', 'Task', 'Task Status', 'Task Due Date'])
        st.dataframe(df)
        unique_list = [i[0] for i in view_all_task_names()]
        delete_task_by_name = st.selectbox("Task to Delete", unique_list)
        st.warning("Deleting {}".format(delete_task_by_name))
        if st.button("Delete"):
            delete_data(delete_task_by_name)
            st.info("Deleted {}".format(delete_task_by_name))
        with st.expander("Current Database"):
            result2 = view_all_tasks()
            new_df = pd.DataFrame(result2, columns=['Task Doer', 'Task', 'Task Status', 'Task Due Date'])
            st.dataframe(new_df)