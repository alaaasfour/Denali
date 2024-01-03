while True:
    user_action = input("Type add, edit, show, complete or exit ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].title() + "\n"
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

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

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo item: ").title()
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo was updated to: '{new_todo}'"
            print(message)
        except ValueError:
            print("Command is not valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo '{todo_to_remove}' was removed from the list!"
            print(message)
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Unknown Command, please enter a valid command 'add', 'show', 'edit', 'complete' or 'exit'")

print("Exiting the program... Thank you!")