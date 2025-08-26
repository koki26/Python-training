import json

try:
    with open("todos.json", "r", encoding="utf-8") as f:
        todos = json.load(f)
except FileNotFoundError:
    todos = []

    

start = 10
while start != "0":
    print(f"TODO LIST \n ======================================= \n")
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo['name']} | {todo['completion_date']} | {todo['complete']}")
    print("\n ======================================= \n [0] EXIT \n [1] New tast \n [2] Finish task \n [3] Delte task")
    start = input()

    if start == "1":
        todos.append({
            "name": "Task name: " + input("Task name: "),             
            "completion_date": "Date: " + input("Date: "),       
            "complete": False
            })
        with open("todos.json", "w", encoding="utf-8") as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)
    
    if start == "2":
        index = input("Number of the task: ")
        try:
            index = int(index)
            if 1 <= index <= len(todos):
                todos[index-1]["complete"] = not todos[index-1]["complete"]
                with open("todos.json", "w", encoding="utf-8") as f:
                    json.dump(todos, f, ensure_ascii=False, indent=4)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid number!")

    if start == "3":
        index = input("Number of the task: ")
        try:
            index = int(index)
            if 1 <= index <= len(todos):
                del todos[index-1]
                with open("todos.json", "w", encoding="utf-8") as f:
                    json.dump(todos, f, ensure_ascii=False, indent=4)
            else:
                print("Invalid task number!")
        except ValueError:
            print("Invalid number!")