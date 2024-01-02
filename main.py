while True:
    user_action = input("Type add, edit, show, complete or exit ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:].title() + "\n"
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        # List comprehension method to remove the new line between the tasks
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo item: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo '{todo_to_remove}' was removed from the list!"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Unknown Command, please enter a valid command 'add', 'show', 'edit', 'complete' or 'exit'")

print("Bye!")