todos = []

while True:
    user_action = input("Type add, edit, show or exit ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo item: ")
            todos[number] = new_todo

        case 'exit':
            break
        case _:
            print("Unknown Command, please enter 'add' or 'show' or 'exit'")

print("Bye!")