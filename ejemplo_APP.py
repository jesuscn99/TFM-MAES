import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("APP para combatir conductas suicidas")
        self.master.geometry("550x400")
        self.master.configure(bg="#f2f2f2")
        self.master.resizable(False, False)

        # Crear el objeto de estilo
        style = ttk.Style()
        # Definir el estilo deseado
        style.configure('Color.TLabelframe', background="#f2f2f2")

        # Crear el Label con la frase motivadora
        motivational_text = "Si sientes que te estás ahogando, no tengas miedo de pedir ayuda, ¡hay personas dispuestas a escucharte y a ayudarte!"
        motivational_label = tk.Label(self.master, text=motivational_text, font=("Arial", 12), fg="navy", bg="#f2f2f2", wraplength=420, justify="center")
        motivational_label.pack(pady=20)

        # Crear el LabelFrame principal
        self.main_frame = ttk.LabelFrame(self.master, text="Recursos de ayuda", padding="20 20 20 20", style='Color.TLabelframe')
        self.main_frame.pack()

        # Añadir el Combobox al Frame
        resources_label = ttk.Label(self.main_frame, text="Selecciona un recurso:")
        resources_label.grid(column=0, row=0, sticky=tk.W, pady=10)
        self.resources_cb = ttk.Combobox(self.main_frame, values=["Email", "Teléfono", "Fundaciones"])
        self.resources_cb.current(0)
        self.resources_cb.grid(column=1, row=0, sticky=tk.W)

        # Añadir el Textbox al Frame
        self.info_textbox = tk.Text(self.main_frame, height=5, width=50)
        self.info_textbox.grid(column=0, row=1, columnspan=2, pady=10)

        # Añadir un botón para obtener la información
        get_info_button = ttk.Button(self.main_frame, text="Obtener información", command=self.get_info)
        get_info_button.grid(column=0, row=2, columnspan=2, pady=10)

    def get_info(self):
        # Obtener la opción seleccionada en el Combobox
        selected_resource = self.resources_cb.get()

        # Obtener la información correspondiente
        if selected_resource == "Email":
            info = "Puedes enviar un correo electrónico para cualquiercuestión a: \n             pideAyuda@animo.com"
        elif selected_resource == "Teléfono":
            info = "Puedes llamar a los siguientes nºs de teléfonos: \n \n   Opción 1: 024 \n   Opción 2: 900 20 20 10 \n   Opción 3: 116 111"
        elif selected_resource == "Fundaciones":
            info = "Estas son algunas de las fundaciones que pueden   ayudarte:\n \n   Opción 1: Fundación ANAR\n   Opción 2: Fundación APSAS"

        # Mostrar la información en el Textbox
        self.info_textbox.delete('1.0', tk.END)
        self.info_textbox.insert(tk.END, info)

# Crear la ventana principal y ejecutar la aplicación
root = tk.Tk()
app = App(root)
root.mainloop()
