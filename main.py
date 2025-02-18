import tkinter as tk
from tkinter import END, messagebox, ttk

dict_regsitros = {}

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
    tk.Label(ventana, text="Ingrese Id del Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_buscar = tk.Entry(ventana, width=20)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    btn_buscar = tk.Button(ventana, text="Buscar")
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)

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
    btn_nuevo = tk.Button(ventana, text="Nuevo")
    btn_nuevo.grid(row=5, column=0, padx=5, pady=10)

    btn_guardar = tk.Button(ventana, text="Guardar")
    btn_guardar.grid(row=5, column=1, padx=5, pady=10)

    btn_cancelar = tk.Button(ventana, text="Cancelar")
    btn_cancelar.grid(row=5, column=2, padx=5, pady=10)

    btn_editar = tk.Button(ventana, text="Editar")
    btn_editar.grid(row=5, column=3, padx=5, pady=10)

    btn_eliminar = tk.Button(ventana, text="Eliminar")
    btn_eliminar.grid(row=5, column=4, padx=5, pady=10)

def ventana_reservaciones():
    ventana = tk.Tk()
    ventana.title("Gestión de Reservaciones")
    ventana.geometry("550x250")

    # Etiqueta y entrada para buscar reservación
    tk.Label(ventana, text="Ingrese Reservación:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_buscar = tk.Entry(ventana, width=20)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    btn_buscar = tk.Button(ventana, text="Buscar Reservación")
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)

    # Campos de entrada
    tk.Label(ventana, text="Reservación ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_id = tk.Entry(ventana, width=5)
    entry_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Cliente ID:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    combo_cliente = ttk.Combobox(ventana, values=[1, 2, 3, 4, 5], width=5)
    combo_cliente.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    combo_cliente.current(0)

    tk.Label(ventana, text="Habitación ID:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    combo_habitacion = ttk.Combobox(ventana, values=[10, 11, 12, 13, 14], width=5)
    combo_habitacion.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    combo_habitacion.current(0)

    tk.Label(ventana, text="Costo:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entry_costo = tk.Entry(ventana, width=10)
    entry_costo.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Fechas y Hora
    tk.Label(ventana, text="Fecha Reservación:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
    entry_fecha_res = tk.Entry(ventana, width=15)
    entry_fecha_res.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Fecha Salida:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
    entry_fecha_salida = tk.Entry(ventana, width=15)
    entry_fecha_salida.grid(row=2, column=3, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Hora Reservación:").grid(row=3, column=2, padx=5, pady=5, sticky="e")
    entry_hora = tk.Entry(ventana, width=15)
    entry_hora.grid(row=3, column=3, padx=5, pady=5, sticky="w")

    # Botones
    btn_nueva = tk.Button(ventana, text="Nueva Reservación")
    btn_nueva.grid(row=5, column=0, padx=5, pady=10)

    btn_reservar = tk.Button(ventana, text="Reservar")
    btn_reservar.grid(row=5, column=1, padx=5, pady=10)

    btn_cancelar = tk.Button(ventana, text="Cancelar Reservación")
    btn_cancelar.grid(row=5, column=2, padx=5, pady=10)

    btn_editar = tk.Button(ventana, text="Editar")
    btn_editar.grid(row=5, column=3, padx=5, pady=10)

def ventana_habitacion():
    ventana = tk.Tk()
    ventana.title("Gestión de Habitaciones")
    ventana.geometry("400x200")

    # Buscar habitación por ID
    tk.Label(ventana, text="Ingrese Habitación ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_buscar = tk.Entry(ventana, width=15)
    entry_buscar.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    btn_buscar = tk.Button(ventana, text="Buscar Habitación")
    btn_buscar.grid(row=0, column=2, padx=5, pady=5)

    # Campos de entrada
    tk.Label(ventana, text="Habitación ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_id = tk.Entry(ventana, width=10)
    entry_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Número:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_numero = tk.Entry(ventana, width=10)
    entry_numero.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    tk.Label(ventana, text="Estado:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    combo_estado = ttk.Combobox(ventana, values=["Libre", "Ocupada"], width=10)
    combo_estado.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    combo_estado.current(0)

    # Botones
    btn_nueva = tk.Button(ventana, text="Nueva Habitación")
    btn_nueva.grid(row=4, column=0, padx=5, pady=10)

    btn_editar = tk.Button(ventana, text="Editar")
    btn_editar.grid(row=4, column=1, padx=5, pady=10)

def guardar():
    confirmation = messagebox.askyesno("¿Desea continuar?", "¿Desa agregar al Registro?")
    
    if confirmation:
        if txId.get() in dict_regsitros:
            messagebox.showerror("Registro no ingresado", "Ya hay un registro con ese ID")
            return
        
        dict_regsitros[int(txId.get())] = [txId.get(), txNombre.get(), txPeso.get(), txTalla.get(), txEdad.get()]
        messagebox.showinfo("Registro ingresado", "Se ha ingresado al registro")
        
    else:
        messagebox.showinfo("Registro no ingresado", "No se ha ingresado al registro")

def ventana_ver_imc():
    ventana = tk.Tk()
    ventana.config(width=300, height=200)
    ventana.title("Ver IMC")

    lbIngresarId = tk.Label(ventana, text="Ingresar ID: ")
    lbIngresarId.place(x=10, y=20)

    txIngresarId = tk.Entry(ventana, width=20)
    txIngresarId.place(x=10, y=50)

    btCalcular=tk.Button(ventana,text="Calcular", command=lambda: calcula_imc())
    btCalcular.place(x=10, y=80)
    
    lbNombre2 = tk.Label(ventana, text="Nombre: ")
    lbNombre2.place(x=10, y=100)
    
    lbIMC2 = tk.Label(ventana, text="IMC: ")
    lbIMC2.place(x=10, y=130)
    
    lbClasificacion = tk.Label(ventana, text="Clasificacion: ")
    lbClasificacion.place(x=10, y=150)
    
    def calcula_imc():
        id = int(txIngresarId.get())
        
        if not (id in dict_regsitros):
            messagebox.showerror("Registro no encontrado", "No hay un registro con el ID ingresado.")
            return
        else:
            
            nombre = dict_regsitros[id][1]
            peso = float(dict_regsitros[id][2])
            talla = float(dict_regsitros[id][3])

            
            imc = (peso/(talla*talla))
            clasificacion = "NA"
            
            if imc <= 18.5:
                clasificacion = "Bajo de peso"
            elif (imc > 18.5) and (imc < 25):
                clasificacion = "Normal"
            elif (imc >= 25) and (imc < 30):
                clasificacion = "Sobrepeso"
            elif (imc >= 30) and (imc < 35):
                clasificacion = "Obesidad I"
            elif (imc >= 35) and (imc < 40):
                clasificacion = "Obesidad II"
            elif (imc >= 40):
                clasificacion = "Obesidad III"
            
            
            lbNombre2.config(text="Nombre: " + nombre)
            lbIMC2.config(text="IMC: " + str(imc))
            lbClasificacion.config(text="Clasificacion: "+ clasificacion )
            
        



root.mainloop()