import tkinter as tk
from tkinter import messagebox
from airport import *

lista_trabajo = []

def btn_cargar_click():
    global lista_trabajo
    lista_trabajo = LoadAirports("Airports.txt")
    actualizar_pantalla()

def btn_anadir_click():
    c = entrada_cod.get().upper()
    lat = entrada_lat.get()
    lon = entrada_lon.get()
    if c != "":
        nuevo = Airport(c, lat, lon)
        AddAirport(lista_trabajo, nuevo)
        actualizar_pantalla()

def btn_borrar_click():
    c = entrada_cod.get().upper()
    RemoveAirport(lista_trabajo, c)
    actualizar_pantalla()

def btn_guardar_click():
    SaveSchengenAirports(lista_trabajo, "Schengen_Only.txt")

def actualizar_pantalla():
    caja.delete(1.0, tk.END)
    for a in lista_trabajo:
        SetSchengen(a)
        res = "SI" if a.schengen else "NO"
        caja.insert(tk.END, f"Cod: {a.code} | Schengen: {res}\n")

ventana = tk.Tk()
ventana.title("Airport Manager - V1")

tk.Label(ventana, text="Código ICAO:").grid(row=0, column=0)
entrada_cod = tk.Entry(ventana)
entrada_cod.grid(row=0, column=1)

tk.Label(ventana, text="Latitud:").grid(row=1, column=0)
entrada_lat = tk.Entry(ventana)
entrada_lat.grid(row=1, column=1)

tk.Label(ventana, text="Longitud:").grid(row=2, column=0)
entrada_lon = tk.Entry(ventana)
entrada_lon.grid(row=2, column=1)

tk.Button(ventana, text="Cargar Archivo", command=btn_cargar_click).grid(row=3, column=0)
tk.Button(ventana, text="Añadir", command=btn_anadir_click).grid(row=3, column=1)
tk.Button(ventana, text="Borrar por Código", command=btn_borrar_click).grid(row=4, column=0)
tk.Button(ventana, text="Guardar Schengen", command=btn_guardar_click).grid(row=4, column=1)
tk.Button(ventana, text="Ver Gráfico", command=lambda: PlotAirports(lista_trabajo)).grid(row=5, column=0)

caja = tk.Text(ventana, height=20, width=60)
caja.grid(row=6, column=0, columnspan=2)

ventana.mainloop()