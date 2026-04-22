from issue_tracker import *
import streamlit as st


st.title("Test App")
name = st.text_input("Subject")

initialize_database()

if st.button("Submit"):
    add_issue(name=name, description="Test", due_date="2026-04-26", priority=1)

    st.write(get_issues())
