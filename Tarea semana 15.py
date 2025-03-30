import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Listas de tareas")

        # Listas de tareas
        self.tareas = []

        # Campo de entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(root, width=40)
        self.entrada_tarea.pack(pady=10)

        # Botones
        self.boton_agregar = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack()

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack()

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack()

        # Lista de tareas (Listbox)
        self.lista_tareas = tk.Listbox(root, width=50)
        self.lista_tareas.pack(pady=10)

        #vinculacion de botones
        self.entrada_tarea.bind("<Return>",lambda event: self.agregar_tarea())
        self.lista_tareas.bind("<Double-Button-1>",lambda event: self.marcar_completada())

        self.actualizar_lista()

    def agregar_tarea(self):
        tarea=self.entrada_tarea.get()
        if tarea:
            self.tareas.append({"tarea":tarea,"completada":False})
            self.entrada_tarea.delete(0,tk.END)
            self.actualizar_lista()

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice=seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0,tk.END)
        for tarea in self.tareas:
             estado="[✓]" if tarea ["completada"] else "[]"
             self.lista_tareas.insert(tk.END,estado+tarea["tarea"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()

