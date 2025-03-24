import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AgendaAPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Variable para almacenar los datos
        def crear_interfaz(self):
            # Treeview para mostrar eventos
            self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
            self.tree.heading("Fecha", text="Fecha")
            self.tree.heading("Hora", text="Hora")
            self.tree.heading("Descripción", text="Descripción")
            self.tree.pack(pady=8)

            ttk.Label(self.root, text="Fecha (YYYY-MM-DD):").pack()
            self.fecha_entry = ttk.Entry(self.root)
            self.fecha_entry.pack()

            ttk.Label(self.root, text="Hora (HH:MM):").pack()
            self.hora_entry = ttk.Entry(self.root)
            self.hora_entry.pack()

            ttk.Label(self.root, text="Descripción:").pack()
            self.descripcion_entry = ttk.Entry(self.root)
            self.descripcion_entry.pack()

            # Botones
            ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento).pack()
            ttk.Button(self.root, text="Eliminar Evento", command=self.eliminar_evento).pack()
            ttk.Button(self.root, text="Salir", command=self.root.quit).pack()

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            self.fecha.delete(0, tk.END)
            self.hora.delete(0, tk.END)
            self.descripcion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", " complete todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            respuesta = messagebox.askyesno("Confirmar", "¿desea eliminar el evento seleccionado?")
            if respuesta:
                for item in seleccion:
                    self.tree.delete(item)
        else:
            messagebox.showerror("Error", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaAPersonal(root)
    root.mainloop()