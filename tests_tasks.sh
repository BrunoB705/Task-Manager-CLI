#EJECUTAR CON GIT BASH
#EJECUTAR CON GIT BASH
#EJECUTAR CON GIT BASH
#EJECUTAR CON GIT BASH
echo "Limpiando tasks.json..."
rm -f tasks.json  # Borra el archivo si existía

echo "Agregando tareas..."
python main.py add "Correr"
python main.py add "Comida"

echo "Mostrando todas las tareas..."
python main.py list

echo "Actualizando tarea 1..."
python main.py update 1 "Correr 5km"

echo "Mostrando todas las tareas..."
python main.py list

echo "Eliminando tarea 2..."
python main.py delete 2

echo "Mostrando todas las tareas..."
python main.py list
#EJECUTAR CON GIT BASH
#EJECUTAR CON GIT BASH
#EJECUTAR CON GIT BASH
#EJECUTAR CON GIT BASH

