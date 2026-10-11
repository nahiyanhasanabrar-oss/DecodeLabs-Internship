tasks =[]
task_id =1

while True:
    new_task = input("enter a task and to finish the program write exit:")
    if new_task =="exit":
        print("work saved successfully")
        break
    task_row ={
        "id":task_id,
        "title":new_task
    }
    tasks.append(task_row)
    task_id +=1
    print("\n--- list of recent work ---")
    for row in tasks:
        print(f"[{row['id']}] {row['title']}")
    print("---------------------------\n")
