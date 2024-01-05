def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a text file and return the list of to-do. """
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

while True:
    user_action = input("Type add, edit, show, complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        if len(user_action) < 5:
            print("Please enter a todo item")
            continue
        else:
            todo = user_action[4:].strip().title() + "\n"
            todos = get_todos()
            todos.append(todo)
            write_todos(todos)
            message = f"Todo '{todo.strip('\n')}' was added to the list!"
            print(message)

    elif user_action.startswith('show'):
        todos = get_todos()

        # List comprehension method to remove the new line between the tasks
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter a new todo item: ").title()
            todos[number] = new_todo + '\n'
            write_todos(todos)
            message = f"Todo was updated to: '{new_todo}'"
            print(message)
        except ValueError:
            print("Command is not valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos, 'todos.txt')
            message = f"Todo '{todo_to_remove}' was removed from the list!"
            print(message)
        except IndexError:
            print("There is no item with that number!")
            continue
        except ValueError:
            print("Please, enter the number of the todo you want to complete!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Unknown Command, please enter a valid command 'add', 'show', 'edit', 'complete' or 'exit'")

print("Exiting the program... Thank you!")