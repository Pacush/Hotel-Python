import tkinter as tk
from tkinter import END, messagebox, ttk

clientes = {}
reservaciones = {}
habitaciones = {}

root = tk.Tk()
root.config(width=300, height=350)
root.title("Hotel")

btn_clientes=tk.Button(root, text="Clientes", command=lambda: ventana_clientes())
btn_clientes.place(x=100, y=70)

btn_reservaciones=tk.Button(root, text="Reservaciones", command=lambda: ventana_reservaciones())
btn_reservaciones.place(x=100, y=100)

btn_habitacion=tk.Button(root, text="Habitaciones", command=lambda: ventana_habitacion())
btn_habitacion.place(x=100, y=130)

def ventana_clientes():
    ventana = tk.Tk()
    ventana.title("Gestión de Clientes")
    ventana.geometry("800x300")

    # Etiqueta y entrada para buscar cliente
    tk.Label(ventana, text="Ingrese ID del Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_buscar = tk.Entry(ventana, width=20)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    

    # Campos de entrada
    tk.Label(ventana, text="ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_id = tk.Entry(ventana, width=5)
    entry_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Nombre:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Email:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
    entry_email = tk.Entry(ventana, width=30)
    entry_email.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Dirección:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_direccion = tk.Entry(ventana, width=30)
    entry_direccion.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Teléfono:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entry_telefono = tk.Entry(ventana, width=30)
    entry_telefono.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Botones
    
    btn_buscar = tk.Button(ventana, text="Buscar", command=lambda: buscar_cliente())
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)
    
    btn_guardar = tk.Button(ventana, text="Guardar", command=lambda: guardar_cliente())
    btn_guardar.grid(row=5, column=0, padx=5, pady=10)

    btn_editar = tk.Button(ventana, text="Editar", command=lambda: editar_cliente())
    btn_editar.grid(row=5, column=1, padx=5, pady=10)

    btn_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: eliminar_cliente())
    btn_eliminar.grid(row=5, column=2, padx=5, pady=10)
    
    def guardar_cliente():
        try:
            id = int(entry_id.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingresar un dato válido.")
            ventana.focus()
            return
        if entry_id.get() == "" or entry_nombre.get() == "" or entry_email.get() == "" or entry_direccion.get() == "" or entry_telefono.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro")
            ventana.focus()
        elif id in clientes:
            messagebox.showerror("ID existente", "Ya existe un cliente con dicho ID. Favor de ingresar otro")
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Desea agregar al cliente?")
            if confirmation:
                clientes[int(entry_id.get())] = [entry_id.get(), entry_nombre.get(), entry_email.get(), entry_direccion.get(), entry_telefono.get()]
                messagebox.showinfo("Registro exitoso", "Se ha guardado correctamente al cliente en los registros.")
                ventana.focus()
                print(clientes)
                
    def buscar_cliente():
        try:
            id = int(entry_buscar.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingrsar un dato válido.")
            ventana.focus()
            return
        if not (id in clientes):
            messagebox.showerror("ID no existente", "No existe ningún cliente con dicho ID.")
            ventana.focus()
        else:
            nombre, email, direccion, telefono = clientes[id][1], clientes[id][2], clientes[id][3], clientes[id][4]
            entry_id.delete(0, END)
            entry_id.insert(0, str(id))
            entry_nombre.delete(0, END)
            entry_nombre.insert(0, nombre)
            entry_email.delete(0, END)
            entry_email.insert(0, email)
            entry_direccion.delete(0, END)
            entry_direccion.insert(0, direccion)
            entry_telefono.delete(0, END)
            entry_telefono.insert(0, telefono)
            
    def editar_cliente():
        try:
            id = int(entry_id.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingrsar un dato válido.")
            ventana.focus()
            return
        if not (id in clientes):
            messagebox.showerror("ID no existente", "No existe ningún cliente con dicho ID.")
            ventana.focus()
            
        elif entry_id.get() == "" or entry_nombre.get() == "" or entry_email.get() == "" or entry_direccion.get() == "" or entry_telefono.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro")
            ventana.focus()
        
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Deseas modificar los datos del cliente "+ str(id)+"?")
            if confirmation:
                nombre, email, direccion, telefono = entry_nombre.get(), entry_email.get(), entry_direccion.get(), entry_telefono.get()
                clientes[id][1] = nombre
                clientes[id][2] = email
                clientes[id][3] = direccion
                clientes[id][4] = telefono
                messagebox.showinfo("Edición exitosa", "Se ha editado correctamente al cliente con el id "+str(id))
                print(clientes)
                
    def eliminar_cliente():
        try:
            id = int(entry_id.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingrsar un dato válido.")
            ventana.focus()
            return
        if not (id in clientes):
            messagebox.showerror("ID no existente", "No existe ningún cliente con dicho ID.")
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Deseas eliminar del registro al cliente "+ str(id)+"?")
            if confirmation:
                clientes.pop(id)
                messagebox.showinfo("Eliminación exitosa", "Se ha eliminado correctamente al cliente con el id "+str(id))
                print(clientes)
                ventana.focus()


def ventana_reservaciones():
    ventana = tk.Tk()
    ventana.title("Gestión de Reservaciones")
    ventana.geometry("650x250")
    
    habitaciones_libres = [key for key, value in habitaciones.items() if value[2] == "Libre"]

    # Etiqueta y entrada para buscar reservación
    tk.Label(ventana, text="Ingrese Reservación:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_buscar = tk.Entry(ventana, width=20)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Campos de entrada
    tk.Label(ventana, text="Reservación ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_id = tk.Entry(ventana, width=5)
    entry_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Cliente ID:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    combo_cliente = ttk.Combobox(ventana, values=list(clientes.keys()), width=5)
    combo_cliente.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Habitación ID:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    combo_habitacion = ttk.Combobox(ventana, values=habitaciones_libres, width=5)
    combo_habitacion.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Costo:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entry_costo = tk.Entry(ventana, width=10)
    entry_costo.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Fechas y Hora
    tk.Label(ventana, text="Fecha Reservación (DD/MM/AAAA):").grid(row=1, column=2, padx=5, pady=5, sticky="e")
    entry_fecha_res = tk.Entry(ventana, width=15)
    entry_fecha_res.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Fecha Salida (DD/MM/AAAA):").grid(row=2, column=2, padx=5, pady=5, sticky="e")
    entry_fecha_salida = tk.Entry(ventana, width=15)
    entry_fecha_salida.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Hora Reservación:").grid(row=3, column=2, padx=5, pady=5, sticky="e")
    entry_hora = tk.Entry(ventana, width=15)
    entry_hora.grid(row=3, column=3, padx=5, pady=5, sticky="w")

    # Botones
    btn_buscar = tk.Button(ventana, text="Buscar Reservación", command=lambda: buscar_reservacion())
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)
    
    btn_reservar = tk.Button(ventana, text="Reservar", command=lambda: guardar_reservacion())
    btn_reservar.grid(row=5, column=0, padx=5, pady=10)

    btn_cancelar = tk.Button(ventana, text="Cancelar Reservación", command=lambda: cancelar_reservacion())
    btn_cancelar.grid(row=5, column=1, padx=5, pady=10)

    btn_editar = tk.Button(ventana, text="Editar", command=lambda: editar_reservacion())
    btn_editar.grid(row=5, column=2, padx=5, pady=10)
    
    def guardar_reservacion():
        try:
            id = int(entry_id.get())
            id_cliente = int(combo_cliente.get())
            id_habitacion = int(combo_habitacion.get())
        except:
            messagebox.showerror("IDs incorrectos", "Los IDs ingresados no son correcto. Favor de ingresar datos válidos.")
            ventana.focus()
            return
        try:
            costo = float(entry_costo.get())
        except:
            messagebox.showerror("Valor de costo inválido", "El valor para el costo es inválido. Favor de ingresar datos válidos.")
        if (entry_id.get() == "") or (combo_cliente.get() == "") or (combo_habitacion.get()) == "" or (entry_costo.get() == "") or (entry_fecha_res.get() ==  "") or (entry_fecha_salida.get() == "") or (entry_hora.get() == ""):
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
            ventana.focus()
        elif id in reservaciones:
            messagebox.showerror("ID existente", "Ya existe una reservación con dicho ID. Favor de ingresar otro.")
            ventana.focus()
        elif not ((id_cliente in clientes) or (id_habitacion in habitaciones)):
            messagebox.showerror("Cliente o habitación inválida", "Favor de elegir un ID de cliente y habitación que se encuentre en la lista.")
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Desea agregar esta reservación?")
            if confirmation:
                reservaciones[id] = [id, id_cliente, id_habitacion, costo, entry_fecha_res.get(), entry_fecha_salida.get(), entry_hora.get()]
                
                habitaciones[id_habitacion][2] = "Reservado"
                
                messagebox.showinfo("Registro exitoso", "Se ha guardado correctamente la reservación en los registros.")
                ventana.focus()
                print(reservaciones)
        
    def buscar_reservacion():
        try:
            id = int(entry_buscar.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingresar un dato válido.")
            ventana.focus()
            return
        if not (id in reservaciones):
            messagebox.showerror("ID no existente", "No existe ninguna reservación con dicho ID.")
            ventana.focus()
        else:
            id_cliente, id_habitacion, costo, fecha_res, fecha_salida, hora  = reservaciones[id][1], reservaciones[id][2], reservaciones[id][3], reservaciones[id][4], reservaciones[id][5], reservaciones[id][6]
            entry_id.delete(0, END)
            entry_id.insert(0, str(id))
            combo_cliente.delete(0, END)
            combo_cliente.insert(0, id_cliente)
            combo_habitacion.delete(0, END)
            combo_habitacion.insert(0, id_habitacion)
            entry_costo.delete(0, END)
            entry_costo.insert(0, costo)
            entry_fecha_res.delete(0, END)
            entry_fecha_res.insert(0, fecha_res)
            entry_fecha_salida.delete(0, END)
            entry_fecha_salida.insert(0, fecha_salida)
            entry_hora.delete(0, END)
            entry_hora.insert(0, hora)
            
    def cancelar_reservacion():
        try:
            id = int(entry_id.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingresar un dato válido.")
            ventana.focus()
            return
        if not (id in reservaciones):
            messagebox.showerror("ID no existente", "No existe ninguna reservación con dicho ID.")
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Desea eliminar la reservación con el ID " + str(id) + "?")
            if confirmation:
                habitaciones[reservaciones[id][2]][2] = "Libre"
                reservaciones.pop(id)
                messagebox.showinfo("Eliminación exitosa", "Se ha eliminado correctamente la reservación con el ID" + str(id))
                ventana.focus()
                print(reservaciones)
                
    def editar_reservacion():
        try:
            id = int(entry_id.get())
            id_cliente = int(combo_cliente.get())
            id_habitacion = int(combo_habitacion.get())
        except:
            messagebox.showerror("IDs incorrectos", "Los IDs ingresados no son correcto. Favor de ingresar datos válidos.")
            ventana.focus()
            return
        try:
            costo = float(entry_costo.get())
        except:
            messagebox.showerror("Valor de costo inválido", "El valor para el costo es inválido. Favor de ingresar datos válidos.")
        if (entry_id.get() == "") or (combo_cliente.get() == "") or (combo_habitacion.get()) == "" or (entry_costo.get() == "") or (entry_fecha_res.get() ==  "") or (entry_fecha_salida.get() == "") or (entry_hora.get() == ""):
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro.")
            ventana.focus()
        elif not ((id_cliente in clientes) or (id_habitacion in habitaciones_libres)):
            messagebox.showerror("Cliente o habitación inválida", "Favor de elegir un ID de cliente y habitación que se encuentre en la lista.")
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Desea editar la reservación con ID " + str(id) + "?")
            if confirmation:
                
                habitaciones[reservaciones[id][2]][2] = "Libre"
                reservaciones[id] = [id, id_cliente, id_habitacion, costo, entry_fecha_res.get(), entry_fecha_salida.get(), entry_hora.get()]
                habitaciones[id_habitacion][2] = "Reservado"
                
                messagebox.showinfo("Edición exitosa", "Se ha editado correctamente la reservación.")
                ventana.focus()
                print(reservaciones)
                
        
        

def ventana_habitacion():
    ventana = tk.Tk()
    ventana.title("Gestión de Habitaciones")
    ventana.geometry("400x200")

    # Buscar habitación por ID
    tk.Label(ventana, text="Ingrese Habitación ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_buscar = tk.Entry(ventana, width=15)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
    # Campos de entrada
    tk.Label(ventana, text="Habitación ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_id = tk.Entry(ventana, width=10)
    entry_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Número:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_numero = tk.Entry(ventana, width=10)
    entry_numero.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Estado:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    combo_estado = ttk.Combobox(ventana, values=["Libre", "Reservado", "Cancelado"], width=10)
    combo_estado.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    combo_estado.current(0)

    # Botones
    btn_buscar = tk.Button(ventana, text="Buscar Habitación", command=lambda: buscar_habitacion())
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)
    
    btn_nueva = tk.Button(ventana, text="Nueva Habitación", command=lambda: guardar_habitacion())
    btn_nueva.grid(row=4, column=0, padx=5, pady=10)

    btn_editar = tk.Button(ventana, text="Editar", command=lambda: editar_habitacion())
    btn_editar.grid(row=4, column=1, padx=5, pady=10)
    
    def guardar_habitacion():
        try:
            id = int(entry_id.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingrsar un dato válido.")
            ventana.focus()
            return
        if entry_id.get() == "" or entry_numero.get() == "" or combo_estado.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro")
            ventana.focus()
        elif id in habitaciones:
            messagebox.showerror("ID existente", "Ya existe una habitación con dicho ID. Favor de ingresar otro")
            ventana.focus()
        elif not ((combo_estado.get() == "Libre") or (combo_estado.get() == "Reservado") or (combo_estado.get() == "Cancelado")):
            messagebox.showerror("Estado inválido", "Favor de elegir un estado de la habitación válido")
            print(combo_estado.get())
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Desea agregar esta habitación?")
            if confirmation:
                habitaciones[int(entry_id.get())] = [entry_id.get(), entry_numero.get(), combo_estado.get()]
                messagebox.showinfo("Registro exitoso", "Se ha guardado correctamente la habitación en los registros.")
                ventana.focus()
                print(habitaciones)
    
    def editar_habitacion():
        try:
            id = int(entry_id.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingresar un dato válido.")
            ventana.focus()
            return
        if not (id in habitaciones):
            messagebox.showerror("ID no existente", "No existe ninguna habitación con dicho ID.")
            ventana.focus()
        elif entry_id.get() == "" or entry_numero.get() == "" or combo_estado.get() == "":
            messagebox.showerror("Campos faltantes", "Faltan campos por llenar para guardar el registro")
            ventana.focus()
        elif not ((combo_estado.get() == "Libre") or (combo_estado.get() == "Reservado") or (combo_estado.get() == "Cancelado")):
            messagebox.showerror("Estado inválido", "Favor de elegir un estado de la habitación válido")
            print(combo_estado.get())
            ventana.focus()
        else:
            confirmation = messagebox.askyesno("¿Desea continuar?", "¿Deseas modificar los datos de la habitación con el id " + str(id)+"?")
            if confirmation:
                numero, estado = entry_numero.get(), combo_estado.get()
                habitaciones[id][1] = numero
                habitaciones[id][2] = estado
                messagebox.showinfo("Edición exitosa", "Se ha editado correctamente a la habitación con el id " + str(id))
                print(habitaciones)
                
    def buscar_habitacion():
        try:
            id = int(entry_buscar.get())
        except:
            messagebox.showerror("ID incorrecto", "El ID ingresado no es correcto. Favor de ingresar un dato válido.")
            ventana.focus()
            return
        if not (id in habitaciones):
            messagebox.showerror("ID no existente", "No existe ninguna habitación  con dicho ID.")
            ventana.focus()
        else:
            numero, estado = habitaciones[id][1], habitaciones[id][2]
            entry_id.delete(0, END)
            entry_id.insert(0, str(id))
            entry_numero.delete(0, END)
            entry_numero.insert(0, numero)
            combo_estado.delete(0, END)
            combo_estado.insert(0, estado)
        


root.mainloop()