#  Task Manager CLI

Gestor de tareas simple desarrollado en Python. Permite agregar, listar, actualizar, eliminar y cambiar el estado de tareas directamente desde la línea de comandos. Las tareas se almacenan en un archivo JSON (`tasks.json`) de forma persistente.

---

##  Características

- Agregar nuevas tareas con descripción.
- Listar todas las tareas o filtrarlas por estado: `todo`, `in-progress`, `done`.
- Actualizar la descripción de una tarea existente.
- Eliminar tareas por su ID.
- Marcar tareas como `done` o `in-progress`.
- Soporte para comando `--help` con guía rápida.
- Manejo de errores si se intenta operar sobre un ID inexistente.

---

##  Requisitos

- Python 3.6 o superior

---

##  Uso
###  Ejecutar desde la terminal

```bash
python main.py <comando> [argumentos]
```

---

###  Comandos disponibles

| Comando | Descripción |
|---------|-------------|
| `add <description>` | Agrega una nueva tarea con la descripción indicada. |
| `list [status]` | Lista tareas. Opcional: `status` = `done`, `in-progress`, `todo`. |
| `update <id> <description>` | Actualiza la descripción de la tarea con el ID especificado. |
| `delete <id>` | Elimina la tarea con el ID especificado. |
| `mark-done <id>` | Marca la tarea como `done`. |
| `mark-in-progress <id>` | Marca la tarea como `in-progress`. |
| `--help` | Muestra esta guía de comandos. |

---

###  Ejemplos de uso

Agregar tareas:

```bash
python main.py add "Correr 5km"
python main.py add "Comprar comida"
```

Listar todas las tareas:

```bash
python main.py list
```

Listar tareas completadas:

```bash
python main.py list done
```

Actualizar una tarea:

```bash
python main.py update 1 "Correr 10km"
```

Eliminar una tarea:

```bash
python main.py delete 2
```

Marcar como completada:

```bash
python main.py mark-done 1
```

Marcar como en progreso:

```bash
python main.py mark-in-progress 1
```

---
