# Import necessary modules
import streamlit as st
import functions

# Get the list of todos using the functions module
todos = functions.get_todos()

# Function to add a new todo to the list
def add_todo():
    todo = st.session_state["new_todo"].title() + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# Streamlit app title and subheader
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your <b>productivity</b>", unsafe_allow_html=True)

# Function to save an edited todo
def save_todo():
    # Get the edited todo and its original index
    edited_todo = st.session_state["edit_todo"].title() + "\n"
    original_index = st.session_state["edit_index"]

    # Update the todo in the list and write back to the file
    todos[original_index] = edited_todo
    functions.write_todos(todos)

    # Remove the edit state and rerun to refresh the page
    del st.session_state["edit_index"], st.session_state["edit_todo"]
    st.experimental_rerun()

# Input box to add a new todo
st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")

# Display todos with buttons for editing and completing
for index, todo in enumerate(todos):
    col1, col2, col3 = st.columns([0.8, 0.3, 0.5])
    with col1:
        st.write(todo.strip())
    with col2:
        # Button to initiate the editing process
        if st.button("Edit", key=f"edit{index}"):
            st.session_state["edit_index"] = index
            st.session_state["edit_todo"] = todo.strip()
    with col3:
        # Button to initiate the completion process
        if st.button("Complete", key=f"del{index}"):
            st.session_state["to_delete"] = index

# Confirmation dialog for deletion
if "to_delete" in st.session_state:
    st.write(f"Are you sure you want to delete: {todos[st.session_state['to_delete']].strip()}?")

    # Confirm delete button
    if st.button("Confirm Delete"):
        # Delete the item and remove the deletion marker
        todos.pop(st.session_state["to_delete"])
        functions.write_todos(todos)
        del st.session_state["to_delete"]
        st.experimental_rerun()

    # Cancel button
    if st.button("Cancel"):
        # Remove the deletion marker without deleting
        del st.session_state["to_delete"]

# Input box to edit a todo
if "edit_index" in st.session_state:
    st.text_input("Edit your todo:", value=st.session_state["edit_todo"], on_change=save_todo, key="edit_todo")
