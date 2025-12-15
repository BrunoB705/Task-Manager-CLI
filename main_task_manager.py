import json
import sys
from datetime import datetime

def read_json():
    with open("tasks.json","r",encoding="utf-8") as f:
        tasks = json.load(f)
    return tasks

def write_json(content):
    tasks = read_json()
    tasks.append(content)
    with open("tasks.json","w",encoding="utf-8") as f:
        json.dump(tasks, f, indent= 4)

def id_function():
    tasks = read_json()
    existing_ids = sorted(task["id"] for task in tasks)
    id_task = 1
    for id_ in existing_ids:
        if id_ == id_task:
            id_task += 1
        else:
            break
    return id_task


def add_task(description):
    created_time = datetime.now()
    new_task = {
        "id":id_function(),
        "description":f"{description}",
        "status":"in-progress", #todo, in-progress, done
        "createdAt":f"{created_time}",
        "updatedAt":f"{created_time}"
    }
    write_json(new_task)

def list_tasks(status=""):
    tasks  = read_json()
    for task in tasks:
        if status == "" or task.get("status") == status:
            print("Tarea: ",task.get("description")," Estado: ",task.get("status"))

def update_task(id_task, description):
    tasks = read_json()
    updated_time = datetime.now().isoformat() #Convierte en string
    found = False
    for task in tasks:
        if task.get("id") == int(id_task):
            task["description"] = description
            task["updatedAt"] = updated_time 
            found = True
    if not found:
        print(f"No existe tarea con el id: {id_task}")
        return
    
    with open("tasks.json",'w',encoding="utf-8") as f:
        json.dump(tasks,f,indent= 4)

def mark_task_as(id_task, status):
    tasks = read_json()
    updated_time = datetime.now().isoformat()#Convierte en string
    found = False
    for task in tasks:
        if task.get("id") == int(id_task):
            task["status"] = status
            task["updatedAt"] = updated_time
            found = True
    if not found:
        print(f"No existe tarea con el id: {id_task}")
        return  
    
    with open("tasks.json",'w',encoding="utf-8") as f:
        json.dump(tasks,f,indent=4)

def delete_task(id_task):
    found = False
    tasks = read_json()
    for i,task in enumerate(tasks, start=0):
        if task.get("id") == int(id_task):
            tasks.pop(i)
            found = True
            break
    if not found:
        print(f"No existe tarea con el id: {id_task}")
        return
    with open("tasks.json",'w',encoding="utf-8") as f:
        json.dump(tasks,f,indent=4)
def show_help():
    help_text = """
        Gestor de tareas - Comandos disponibles:

        add <description>              : Agrega una nueva tarea con la descripción indicada.
        list [status]                  : Lista tareas. Opcional: status = done, in-progress, todo
        update <id> <description>      : Actualiza la descripción de la tarea con id especificado.
        delete <id>                    : Elimina la tarea con el id especificado.
        mark-done <id>                 : Marca la tarea como 'done'.
        mark-in-progress <id>          : Marca la tarea como 'in-progress'.
        --help                         : Muestra esta ayuda.
        """
    print(help_text)       
    

def main():
    try:
        with open("tasks.json",'r',encoding='utf-8') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        with open("tasks.json",'w',encoding='utf-8') as f:
            json.dump([],f)

    if len(sys.argv) < 2:
        print("No ejecutaste correctamente el comando.")
        return
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Falta descripcion o id para el cmd 'update'")
            return
        description = sys.argv[2]
        add_task(description)

    if command == "list":
        status = ""
        if len(sys.argv) > 2:
            status = sys.argv[2]
        list_tasks(status)

    if command == "update":
        if len(sys.argv) < 3:
            print("Falta descripcion o id para el cmd 'update'")
            return
        id_task = sys.argv[2]
        description = sys.argv[3]
        update_task(id_task, description)

    if command == "delete":
        if len(sys.argv) < 3:
            print("Falta descripcion o id para el cmd 'update'")
            return
        id_task = sys.argv[2]
        delete_task(id_task)
    
    if command == "mark-done":
        if len(sys.argv) < 3:
            print("Falta descripcion o id para el cmd 'update'")
            return
        status = "done"
        id_task = sys.argv[2]
        mark_task_as(id_task,status)
    
    if command =="mark-in-progress":
        if len(sys.argv) < 3:
            print("Falta descripcion o id para el cmd 'update'")
            return
        status = "in-progress"
        id_task = sys.argv[2]
        mark_task_as(id_task,status)
    
    if command =="--help":
        show_help()

main()
