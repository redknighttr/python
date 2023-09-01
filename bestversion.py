Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def view_notes():
...     try:
...         with open("calculator_notes.txt", "r") as file:
...             notes = file.read()
...             if notes:
...                 print("Calculator Notes:")
...                 print(notes)
...             else:
...                 print("No notes found.")
...     except FileNotFoundError:
...         print("No notes found.")
... 
... def clear_notes():
...     try:
...         open("calculator_notes.txt", "w").close()
...         print("Notes cleared successfully.")
...     except FileNotFoundError:
...         print("No notes found.")
... 
...  def main():
...     previous_result = None
...     while True:
...         print("Select operation:")
...         print("1. Add")
...         print("2. Subtract")
...         print("3. Multiply")
...         print("4. Divide")
...         print("5. View Calculator Notes")
...         print("6. Clear Calculator Notes")
...         print("7. Exit")
... 
...         choice = input("Enter choice (1/2/3/4/5/6/7): ")
... 
...         if choice == '7':
...             break
...         elif choice == '5':
...             view_notes()
...         elif choice == '6':
...             clear_notes()
...         else:
...             num_count = int(input("How many numbers do you want to calculate with? "))
...             numbers = []
...             for i in range(num_count):
...                 num = float(input(f"Enter number {i + 1}: "))
...                 numbers.append(num)

            result = None
            if choice == '1':
                result = add(numbers)
            elif choice == '2':
                result = subtract(numbers)
            elif choice == '3':
                result = multiply(numbers)
            elif choice == '4':
                result = divide(numbers)
            else:
                print("Invalid input")
                continue
            
            print("Result:", result)
            if previous_result is not None:
                print("Previous Result:", previous_result)

            note = input("Would you like to add a note about this calculation? (y/n): ")
            if note.lower() == 'y':
                with open("calculator_notes.txt", "a") as file:
                    file.write(f"Calculation: {numbers} -> Result: {result}\n")
                print("Note added successfully.")

            previous_result = result

if __name__ == "__main__":
    main()
