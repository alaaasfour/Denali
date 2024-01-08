# Import necessary modules
import functions
import PySimpleGUI as sg
import time
import os

# Ensure the existence of the 'todos.txt' file
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# Create a clock element to display the current time
clock = sg.Text('', key='clock')

# Define GUI layout components
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Create the main window
window = sg.Window("My To-Do APP",
                       layout=[
                           [clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                       ],
                       font=("Helvetica", 20)
                   )

# Main event loop
while True:
    # Read events with a timeout to update the clock periodically
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # Event handling using match-case (requires Python 3.10+)
    match event:
        case "Add":
            # Get current todos and the new todo from the input
            todos = functions.get_todos()
            new_todo = values['todo'].title() + "\n"

            # Check for duplicate todos
            if new_todo in todos:
                user_response = sg.popup_yes_no(f"The todo ['{new_todo}'] already exists. Do you want to add it again?", font=("Helvetica", 20))
                if user_response == "No":
                    continue

            # Add the new todo and update the display
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                # Get the todo to edit and the new edition
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].title() + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)

                # Update the todo and display
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo item to edit!", font=("Helvetica", 20))

        case "Complete":
            try:
                # Get the todo to complete and update the todos list
                to_do_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(to_do_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a todo item to complete!", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            # Display the selected todo in the input box
            window['todo'].update(value=values['todos'][0].strip('\n'))

        case sg.WINDOW_CLOSED:
            break

# Close the window when the loop ends
window.close()