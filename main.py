while True:
    user_action = input("Type add, edit, show, complete or exit ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ").title() + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # List comprehension method to remove the new line between the tasks
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.title().strip('\n')
                row = f"{index + 1}. {item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo item: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
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

        case 'exit':
            break
        case _:
            print("Unknown Command, please enter 'add' or 'show' or 'exit'")

print("Bye!")