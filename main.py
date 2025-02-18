import tkinter as tk
from tkinter import END, messagebox, ttk

root = tk.Tk()
root.config(width=300, height=350)
root.title("IMC")
lbId = tk.Label(root, text="ID: ")
lbId.place(x=10, y=20)
txId=tk.Entry(root, width=20)
txId.place(x=10, y=50)
lbNombre=tk.Label(root, text="Nombre: ")
lbNombre.place(x=10, y=80)
txNombre=tk.Entry(root, width=20)
txNombre.place(x=10, y=110)
lbPeso = tk.Label(root, text="Peso: ")
lbPeso.place(x=10, y=130)
txPeso = tk.Entry(root, width=20)
txPeso.place(x=10, y=150)
lbTalla = tk.Label(root, text="Talla: ")
lbTalla.place(x=10, y=170)
txTalla = tk.Entry(root, width=20)
txTalla.place(x=10, y=200)
lbEdad = tk.Label(root, text="Edad: ")
lbEdad.place(x=10, y=230)
txEdad = tk.Entry(root, width=20)
txEdad.place(x=10, y=250)

btGuardar=tk.Button(root, text="Guardar", command=lambda: guardar())
btGuardar.place(x=10, y=280)

btVerIMC=tk.Button(root, text="Ver IMC", command=lambda: ventana_ver_imc())
btVerIMC.place(x=10, y=310)



dict_regsitros = {}



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