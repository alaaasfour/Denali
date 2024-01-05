# from functions import write_todos, get_todos
import functions
while True:
    user_action = input("Type add, edit, show, complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        if len(user_action) < 5:
            print("Please enter a todo item")
            continue
        else:
            todo = user_action[4:].strip().title() + "\n"
            todos = functions.get_todos()
            todos.append(todo)
            functions.write_todos(todos)
            message = f"Todo '{todo.strip('\n')}' was added to the list!"
            print(message)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # List comprehension method to remove the new line between the tasks
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            if 1<= number <= len(todos):
                number = number - 1
                new_todo = input("Enter a new todo item: ").title()
                todos[number] = new_todo + '\n'
                functions.write_todos(todos)
                message = f"Todo was updated to: '{new_todo}'"
                print(message)
            else:
                print("There is no item with that number!")
        except ValueError:
            print("Please, enter the number of the todo you want to edit!")
            continue
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos, 'todos.txt')
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