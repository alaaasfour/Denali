# Import necessary modules
import functions
import time

# Get the current date and time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is:", now)

# Main loop for the todo application
while True:
    # Get user action input
    user_action = input("Type add, edit, show, complete or exit ")
    user_action = user_action.strip()

    # Handle user actions
    if user_action.startswith('add'):
        # Check if the user entered a todo item
        if len(user_action) < 5:
            print("Please enter a todo item")
            continue
        else:
            # Extract and format the todo from user input
            todo = user_action[4:].strip().title() + "\n"
            todos = functions.get_todos()

            # Check for duplicate todos
            if todo in todos:
                user_response = input(f"The todo [{todo.strip('\n')}] already exists. Do you want to add it again? (yes/no): ").lower()
                if user_response != "yes":
                    continue

            # Add the new todo and display a message
            todos.append(todo)
            functions.write_todos(todos)
            message = f"Todo '{todo.strip('\n')}' was added to the list!"
            print(message)

    elif user_action.startswith('show'):
        # Display the list of todos
        todos = functions.get_todos()

        # List comprehension method to remove the new line between the tasks
        # new_todos = [item.strip('\n') for item in todos]

        # Iterate over todos and print each with an index
        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            # Get the todo number to edit
            number = int(user_action[5:])
            todos = functions.get_todos()

            # Check if the todo number is valid
            if 1 <= number <= len(todos):
                number = number - 1
                # Get the new todo item and update the todos list
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
            # Get the todo number to complete
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            # Remove the todo and update the todos list
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
        # Exit the program if the user enters 'exit'
        break

    else:
        # Display a message for unknown commands
        print("Unknown Command, please enter a valid command 'add', 'show', 'edit', 'complete' or 'exit'")

# Print a final message when exiting the program
print("Exiting the program... Thank you!")