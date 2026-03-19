class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed to stack")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(removed, "popped from stack")
        else:
            print("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty!")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


def stack_menu():
    s = Stack()

    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            val = int(input("Enter value: "))
            s.push(val)

        elif choice == 2:
            s.pop()

        elif choice == 3:
            s.peek()

        elif choice == 4:
            s.display()

        elif choice == 5:
            break

        else:
            print("Invalid choice!")
